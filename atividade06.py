#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

def calcPi(num_termos):
    """Calculando o valor de Pi Segundo Leibiniz."""
    acum = 0.0
    den = 1
    for i in range(num_termos):
        acum = acum + (1.0/den) * (-1)**i
        den = den + 2
    return 4 * acum
print(calcPi(input("Digite um valor: ")))
