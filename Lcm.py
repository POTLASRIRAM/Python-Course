def lcm(x, y):
  if x > y:
      z = x
  else:
      z = y
  while(True):
      if((z % x == 0) and (z % y == 0)):
          lcm = z
          break
      z += 1
  return lcm
n1=int(input("Enter first value "))
n2=int(input("Enter second value "))
print(lcm(n1, n2))


