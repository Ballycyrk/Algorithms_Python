import random

def bubble_sort(list):
  ending_index = len(list)-1
  while ending_index > 0:
    for index in range(0, ending_index):
      if list[index] > list[index +1]:
        temp = list[index]
        list[index] = list[index+1]
        list[index+1] = temp
    ending_index -= 1
  print list

def random_list():
  newList = []
  for times in range(0, 100):
    number = random.randint(1, 10000)
    newList.append(number)
  return newList

numbers = random_list()
bubble_sort(numbers)

name = "Ballycyrk"
othername = name[3:5]
print othername
print name
