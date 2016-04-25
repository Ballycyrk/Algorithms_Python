def fibonacci(number):
  fib = [0,1]
  if number < 0:
    print "Only postive numbers are accepted please try again."
  elif number <= 1:
    print fib[number]
  else:
    calculate = number
    while calculate > 1:
      next = len(fib)
      fib.append(fib[next-1] + fib[next-2])
      calculate -= 1
    print fib[number]

fibonacci(5)
fibonacci(-2)
fibonacci(10)
