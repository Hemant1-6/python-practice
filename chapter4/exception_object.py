#locals() and exception_object as argument
# try:
#  data = open('missing.txt','r')
#  print(data.readline(),end='')
# except IOError as err:
#     print('File Error :' + str(err))
# finally:
#     if 'data' in locals():
#      data.close()

# use of with

try:
    with open('missing.txt','r') as data :
     print(data.readline(),end='')
except IOError as err:
    print("File Error :" + str(err))


