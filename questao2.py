"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""


numero = int(input("Que termo deseja encontrar: "))
a_0=0 ; a_1=1
fib = a_0 + a_1
encontrado = False

if a_0 == numero:
  encontrado = True

while numero > fib and encontrado == False:
  a_0 = a_1
  a_1 = fib
  fib = a_0 + a_1
  #print(f"fib = {fib}")

  if numero == fib:
    encontrado = True
    print(f"O número {numero} encontrado na sequência de Fibonacci. {a_0} + {a_1} = {fib}")

if encontrado == False:
  print(f"O número {numero} não encontrado na sequência de Fibonacci.")