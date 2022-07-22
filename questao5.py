"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

def string_reverse(string):
    stringReverse = ""
    i = len(string)-1
    while i > -1:
        stringReverse += string[i]
        i -= 1
  
    return stringReverse 


#string = "Ruan Heleno Correa da Silva"
string = input("Que string deseja tornar reversa? ")
stringReverse = string_reverse(string)
print(f"String inicial: {string}")
print(f"String reversa: {stringReverse}")