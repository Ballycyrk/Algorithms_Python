def multiTable12():
  for base in range (1, 13):
    row = " "
    for multiplier in range (1, 13):
      result = base * multiplier
      if result < 10:
        row += "  " + str(result) + " "
      elif result < 100:
        row += " " + str(result) + " "
      else:
        row += str(result) + " "
    print row

multiTable12()
