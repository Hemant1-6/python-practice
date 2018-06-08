# Custom Class to access Coach's data
# class Athlete:
#     def __init__(self,Aname=None,Adob=None,Atime=[]):
#         self.name = Aname
#         self.dob = Adob
#         self.time = Atime
#
#     def top_3(self):
#         return sorted(set([self.sanitize(t) for t in self.time]))[0:3]
#
#
#     def sanitize(self,data):
#         if '-' in data:
#             splitter = '-'
#         elif ':' in data:
#             splitter = ':'
#         else:
#             return data
#         (min, sec) = data.split(splitter)
#         return (min + '.' + sec)
#
#     def get_coach_data(self,filename):
#         try:
#             with open(filename) as fname:
#                 data = fname.readline().strip().split(',')
#                 self.name = data.pop(0)
#                 self.dob =  data.pop(0)
#                 self.time = data
#                 return self
#         except IOError:
#             print("File Error")
#             return (None)
#
#     def add_time(self,time):
#         self.time.append(time)
#
#     def add_times(self,times):
#         self.time.extend(times)

# Inherites class to access Coach's data

class AthleteList(list):
    def __init__(self,a_name=None,a_dob=None,a_list=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_list)

    def sanitize(self, data):
      if '-' in data:
            splitter = '-'
      elif ':' in data:
            splitter = ':'
      else:
        return data
      (min, sec) = data.split(splitter)
      return (min + '.' + sec)

    def top_3(self):
        return sorted(set([self.sanitize(t) for t in self]))[0:3]

    def get_coach_data(self,filename):
        try:
            with open(filename) as fname:
                data = fname.readline().strip().split(',')
                self.name = data.pop(0)
                self.dob = data.pop(0)
                self.extend(data)
                return self
        except IOError:
            print("File Error")
            return (None)



james = AthleteList();james = james.get_coach_data('james2.txt')
julie = AthleteList();julie = julie.get_coach_data('julie2.txt')
mikey = AthleteList();mikey = mikey.get_coach_data('mikey2.txt')
sarah = AthleteList();sarah = sarah.get_coach_data('sarah2.txt')

print(james.name + " " + james.dob + " " + str(james.top_3()))
print(julie.name + " " + julie.dob + " " + str(julie.top_3()))
print(mikey.name + " " + mikey.dob + " " + str(mikey.top_3()))
print(sarah.name + " " + sarah.dob + " " + str(sarah.top_3()))

# john = Athlete('john')
# john.add_time('2.10')
# john.add_times(['2-25','2:54','2.30'])
# print(john.top_3())