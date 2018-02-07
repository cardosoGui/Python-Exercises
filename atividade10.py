""" Faça um Programa que peça a temperatura em graus Celsius, t
ransforme e mostre em graus Farenheit. """

C = input("Digite o Grau Celsius: ")

def grauFarenheit(grau):
    F = (grau * 2) + 32
    return F
print("Graus Farenheit: "+str(grauFarenheit(C)))
