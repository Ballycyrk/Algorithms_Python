def reverseString(string):
  stringList = list(string)
  last = len(stringList) - 1
  for idx in range (0, (last+1)/2):
    first = string[idx]
    stringList[idx] = stringList[last-idx]
    stringList[last-idx] = first
  return ''.join(stringList)

def reversedString(string):
  newString = ""
  letter = len(string)-1
  while letter >= 0:
    newString += string[letter]
    letter -= 1
  return newString

print "Please type a string you'd like to see reversed."
newString = input()
print reverseString(newString)
print reversedString(newString)

