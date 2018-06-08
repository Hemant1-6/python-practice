from nester import nester
import pickle

man_file = []
try:
 data = open('sketch.txt')
 man = []
 other = []
 for each_line in data:
    try:
     (role, line_spoken) = each_line.split(":", 1)
     line_spoken = line_spoken.strip()
     if role == "Man":
         man.append(line_spoken)
     else:
         other.append(line_spoken)
    except ValueError:
        pass
 data.close()
except IOError:
    print("The file is not available")
# for man_line in man:
#     # print("Man said :" , end='')
#     print(man_line,end='')
# print()
# for other_line in other:
#     #print("Other said :",end='')
#     print(other_line,end='')

# try:
#     man_data = open('man_data.txt','w')
#     print(man,file=man_data)
#     man_data.close()
# except IOError:
#     print("Unable to Write data as file doesn't exist")
#
# try:
#     other_data = open('other_data.txt','w')
#     print(other,file=other_data)
#     close in finally block
# except:
#     print("Unable to write the data as file doesn't exist")
# finally:
#     other_data.close()

# try:
#     with open("man_data.txt",'w') as man_data:
#         nester.print_lol(man,fh=man_data)
# except IOError as err:
#      print("file error" + str(err))
#
# try:
#     with open("other_data.txt",'w') as other_data:
#         nester.print_lol(other,fh=other_data)
# except IOError as err:
#      print("file error" + str(err))



# try:
#     with open("man_data.txt",'w') as man_data , open("other_data.txt",'w') as other_data:
#         nester.print_lol(man,fh=man_data)
#         nester.print_lol(other,fh=other_data)
# except IOError as err:
#      print("file error" + str(err))


# Using Pickle for persistance data
try:
    with open("man_data.txt",'wb') as man_data , open("other_data.txt",'wb') as other_data:
        pickle.dump(man,man_data)
        pickle.dump(other,other_data)
except pickle.PickleError as perr:
     print("file error" + str(perr))

try:
    with open('man_data.txt','rb') as man_file:
        man_file = pickle.load(man_file)
except IOError as err:
    print("file error "+ str(err))
except pickle.PickleError as perr :
    pickle("pickle error "+ str(perr))

nester.print_lol(man_file)

