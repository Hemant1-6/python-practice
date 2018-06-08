# jamesct = []
# juliect = []
# mikeyct = []
# sarahct = []

unique_james = []
unique_julie = []
unique_mickey = []
unique_sarah = []

#to filter the list
def sanitize(data):
    if '-' in data:
        splitter = '-'
    elif ':' in data:
        splitter = ':'
    else:
        return data
    (min , sec) = data.split(splitter)
    return (min + '.' + sec)

try:
    with open('james.txt', 'r') as james, open('julie.txt', 'r') as julie, open('mikey.txt', 'r') as mikey, open(
                'sarah.txt', 'r') as sarah:
        try:
                # james_time = james.readline()
                jamest = james.readline().strip().split(',')

                # julie_time = julie.readline()
                juliet = julie.readline().strip().split(',')

                # mikey_time = mikey.readline()
                mikeyt = mikey.readline().strip().split(',')

                # sarah_time = sarah.readline()
                saraht = sarah.readline().strip().split(',')

# replacing ':' and '-' from list to '.'

                 # for each_time in jamest:
                #   jamesct.append(sanitize(each_time))
                # for each_time in juliet:
                #    juliect.append(sanitize(each_time))
                # for each_time in mikeyt:
                #     mikeyct.append(sanitize(each_time))
                # for each_time in saraht:
                #     sarahct.append(sanitize(each_time))

# replacing the duplicates and filtering the list

                # jamesct = [sanitize(t) for t in jamest]
                # jamesct.sort()
                # for each_t in jamesct:
                #  if each_t not in unique_james :
                #      unique_james.append(each_t)
                #
                #  juliect = [sanitize(t) for t in juliet]
                #  juliect = sorted(juliect)
                # for each_t in juliect:
                #  if each_t not in unique_julie:
                #      unique_julie.append(each_t)
                #
                #  mikeyct = [sanitize(t) for t in mikeyt]
                #  mikeyct = sorted(mikeyct)
                # for each_t in mikeyct:
                #     if each_t not in unique_mickey:
                #         unique_mickey.append(each_t)
                #
                # sarahct = sorted([sanitize(t) for t in saraht])
                # for each_t in sarahct:
                #     if each_t not in unique_sarah:
                #         unique_sarah.append(each_t)

# removing duplicates using  "set" :
                unique_james = sorted(set([sanitize(t) for t in jamest]))
                unique_julie = sorted(set([sanitize(t) for t in juliet]))
                unique_mickey = sorted(set([sanitize(t) for t in mikeyt]))
                unique_sarah = sorted(set([sanitize(t) for t in saraht]))
        except:
                pass
except IOError as err:
      print("File Error " + str(err))

# Co-pied Sorting
print(unique_james[0:3])
print(unique_julie[0:3])
print(unique_mickey[0:3])
print(unique_sarah[0:3])

# In-place Sorting
# print(james.sort())
# print(julie.sort())
# print(mikey.sort())
# print(sarah.sort())
