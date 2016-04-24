import random

def random_list():
  newList = []
  for times in range(0, 100):
    number = random.randint(1, 10000)
    newList.append(number)
  return newList

def insertion_sort(list):
  for unsortedPortion in range(1, len(list)):
    element = list[unsortedPortion]
    sortedPortion = unsortedPortion
    while sortedPortion > 0 and list[sortedPortion-1] > element:
      list[sortedPortion] = list[sortedPortion-1]
      sortedPortion -= 1
    list[sortedPortion] = element
  return list

numbers = random_list()
print insertion_sort(numbers)
