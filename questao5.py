"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

# questão 5

def string_invertida(string):
    stringInvertida = ""
    i = len(string)-1
    while i > -1:
        stringInvertida += string[i]
        i -= 1
    
    return stringInvertida 


#string = "Ruan Heleno Correa da Silva"
string = input("Que string deseja inverter? ")
stringInvertida = string_invertida(string)
print(f"String inicial: {string}")
print(f"String invertida: {stringInvertida}")