import random

def random_list():
  newList = []
  for times in range(0, 100):
    number = random.randint(1, 10000)
    newList.append(number)
  return newList

def selection_sort(list):
  startingIndex = 0
  while startingIndex < len(list)-1:
    minValue = startingIndex
    for index in range(startingIndex+1, len(list)):
      if list[index] < list[minValue]:
        minValue = index
    if minValue != startingIndex:
      temp = list[minValue]
      list[minValue] = list[startingIndex]
      list[startingIndex] = temp
    startingIndex += 1
  return list

numbers = random_list()
print selection_sort(numbers)
