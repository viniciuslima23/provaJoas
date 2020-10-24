import random

ben = [3, 3, 2, 4, 2, 3, 5, 2]
weight = [5, 4, 7, 8, 4, 4, 6, 8]

def getcromos( size ):
  cromos = []
  i = 0
  while i < size:
    gene = random.randint(0, 1)
    cromos.append(gene)
    i = i + 1
  return cromos

size = 8
cromos = getcromos( size )

def fitness( cromos ):
  i = 0
  benf = 0
  peso = 0
  while i < size:
    gene = cromos[i]
    if gene == 1:
      benf = benf + ben[i]
      peso = peso + weight[i]
    i = i + 1
  if peso > 25:
    benf = -1
  return benf      

benf = -1
sizePop = 10

while benf < 13:
  cromos = getcromos( size )
  benf = fitness( cromos ) 
  print(cromos)  
  print(benf)
