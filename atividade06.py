#Fa�a um Programa que pe�a o raio de um c�rculo, calcule e mostre sua �rea.

def calcPi(num_termos):
    """Calculando o valor de Pi Segundo Leibiniz."""
    acum = 0.0
    den = 1
    for i in range(num_termos):
        acum = acum + (1.0/den) * (-1)**i
        den = den + 2
    return 4 * acum
print(calcPi(input("Digite um valor: ")))
