"""Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês."""

valor = input("Digite quantas horas trabalhadas: ")
hora = input("Digite o valor por hora: ")


def horaTrabalhada(a,b):
    subtotal = a * b
    return subtotal

def horaMes(subtotal):
    dias = input("Quantos dias trabalhados no mês: ")
    horaMes = subtotal * dias
    return horaMes
print("Valor Total Mensal: "+ str(horaMes(horaTrabalhada(valor,hora))))
