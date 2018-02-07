"""Faça um Programa que peça a temperatura em graus Farenheit,
transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9)."""

F = input("Digite um valor em Farenheit: ")
def conversor(graus):
    c = ((F-32) / 2)
    return c
print("Graus Celsius = "+str(conversor(F)))
