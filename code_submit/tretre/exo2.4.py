#exo fibo
def fibo(n):
  a, b = 0, 1
  i=1
  if n >= 0:
    print(a, end=' ')
  if n >= 1:
    print(b, end=' ')
  while i >= 1 and i < n:
    output = a + b
    print(output,end=' ')
    a, b = b, output
    i+=1
fibo(5)

#exo bigrams
def bigrams():
  x = str(input())
  y = ''
  for i in x:
    if i != ' ':
      y = y + i
  for j in range(len(y)-1):
    print(y[j],y[j+1])
bigrams()





