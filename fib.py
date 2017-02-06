def fib(n) :
   if n == 1:
      print (0)
   elif n == 2:
      print (0, 1)
   else :
      print("Hello World: first Fibonacci ", n)

   i = 0
   j = 1
#   print (i, j)
   for k in range(0, n):
     tmp = i + j
     print (i+j, " " , k)
     i = j
     j = tmp


def sum(n):
  j = 0
  for i in range(0, n):
    j= j + i + 1
  print (j)

  return j
  
  


print ("Hello World")

print ("Happy World")
fib(10)

print(sum(4))

"""
1) Given a matrix with each cell containing each number of candies, and a constraint that you can move only right or down, from the top left corner to the bottom right corner, find the path that gets you maximum candies.

2) Convert a Binary tree to its mirror in-place
"""
