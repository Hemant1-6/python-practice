import os
#print(os.getcwd())

try:
 data = open('sketch.txt')
# print(data.readline(),end='')
# print(data.readline(),end='')
# data.seek(0)

#method 1 to excess data by adding more code :

# for each_line in data:
#     if not each_line.find(':') == -1:
#      (role, line_spoken) = each_line.split(":", 1)
#      print(role,end='')
#      print(' said :',end='')
#      print(line_spoken,end='')
# data.close()

#method 2 to express data using exception handling
 for each_line in data:
    try:
     (role, line_spoken) = each_line.split(":", 1)
     print(role,end='')
     print(' said :',end='')
     print(line_spoken,end='')
    except ValueError:
        print(each_line,end='')
 data.close()
except IOError:
    print("The file is not available")