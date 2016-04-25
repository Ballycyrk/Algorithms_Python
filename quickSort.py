import random

def random_list():
  newList = []
  for times in range(0, 10):
    number = random.randint(1, 100)
    newList.append(number)
  return newList

def quick_sort(list, low=None, high=None):
  print list, low, high
  if low is None:
    low = 0
  if high is None:
    high = len(list)
  if low >= high:
    return
  else:
    pivot = list[low]
    print pivot
    for idx in range(low+1, high):
      if list[idx] <= pivot:
        list[low] = list[idx]
        low += 1
        list[idx] = list[low]
    list[low] = pivot
    quick_sort(list, 0, low-1)
    quick_sort(list, low+1, high)
    return list

numbers = random_list()
print quick_sort(numbers)


