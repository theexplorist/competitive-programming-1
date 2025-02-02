'''
   math > combinatorics > fibonacci numbers
   difficulty: medium
   date: 19/Feb/2020 
   solution: compute (n+2)-th fibonnaci number
   by: @brnpapa
'''

fib = [0]*1010
fib[1] = 1
for i in range(2, 1010):
   fib[i] = fib[i-1]+fib[i-2]

while (1):
   try:
      n = int(input())
      print(fib[n+2])
   except EOFError:
      break