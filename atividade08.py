"""Fa�a um Programa que pergunte quanto voc� ganha por hora e o
n�mero de horas trabalhadas no m�s.
Calcule e mostre o total do seu sal�rio no referido m�s."""

valor = input("Digite quantas horas trabalhadas: ")
hora = input("Digite o valor por hora: ")


def horaTrabalhada(a,b):
    subtotal = a * b
    return subtotal

def horaMes(subtotal):
    dias = input("Quantos dias trabalhados no m�s: ")
    horaMes = subtotal * dias
    return horaMes
print("Valor Total Mensal: "+ str(horaMes(horaTrabalhada(valor,hora))))
