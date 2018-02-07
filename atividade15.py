""" Faça um Programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a.salário bruto.
b.quanto pagou ao INSS.
c.quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$ """

print("*-- Cálculo de salário --*")

def horaTrabalhada():
    valor = input("Digite o valor por hora: ")
    hora = input("Digite quantas horas trabalhadas por dia: ")
    subtotal = valor * hora
    return subtotal

def horaMes(subtotal):
    valorTotal = subtotal * 23
    return valorTotal

def porcentagem(nporcento,salario):
    total = (salario * nporcento) / 100
    return total

def holerite(valorTotal):
    ir = porcentagem(11,valorTotal)
    inss = porcentagem(8,valorTotal)
    sindicato = porcentagem(5,valorTotal)
    print("Salário Bruto: R$"+str(valorTotal))
    print("Imposto de Renda (11%): R$"+str(ir))
    print("INSS (8%): R$"+str(inss))
    print("Sindicato (5%): R$"+str(sindicato))
    total = valorTotal - (ir+inss+sindicato)
    print("*-----------------------------------*")
    return "Salário líquido: R$"+str(total)

valorTotal = horaMes(horaTrabalhada())
print(holerite(valorTotal))
