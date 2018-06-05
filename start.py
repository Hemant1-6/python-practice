# movies = ['"The holy grail"', 1975, '"The life of Brain"', 1979, '"The Meaning of Life"', 1983]
# print(movies)
# print(len(movies))
# movies.pop();
# print(len(movies))
# movies.insert(1,"The Marvel Avengers")
# print(movies)
# movies.extend("Black Hawk Dawn")
# print(len(movies))

# for x in movies: print(x)
# print()
# count = 0
# while (count < len(movies)):
#     print(movies[count])
#     count = count + 1
from typing import List, Union

movies = ["The holy grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
           ["Michael Palin", "John Clease", "Terry Gilliam", "Terry Jones"]]]

# for each_list in movies :
#      if isinstance(each_list,list):
#       for list_inlist in each_list :
#          print(list_inlist)
#      else:
#          print(each_list)


def print_lol(list_item):
    for each_list in list_item:
        if isinstance(each_list, list):
            print_lol(each_list)
        else:
            print(each_list)
print_lol(movies)