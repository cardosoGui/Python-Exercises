""" Fa�a um Programa que pergunte quanto voc� ganha por hora
e o n�mero de horas trabalhadas no m�s.
Calcule e mostre o total do seu sal�rio no referido m�s,
sabendo-se que s�o descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, fa�a um programa que nos d�:
a.sal�rio bruto.
b.quanto pagou ao INSS.
c.quanto pagou ao sindicato.
o sal�rio l�quido.
calcule os descontos e o sal�rio l�quido, conforme a tabela abaixo:
+ Sal�rio Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Sal�rio Liquido : R$ """

print("*-- C�lculo de sal�rio --*")

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
    print("Sal�rio Bruto: R$"+str(valorTotal))
    print("Imposto de Renda (11%): R$"+str(ir))
    print("INSS (8%): R$"+str(inss))
    print("Sindicato (5%): R$"+str(sindicato))
    total = valorTotal - (ir+inss+sindicato)
    print("*-----------------------------------*")
    return "Sal�rio l�quido: R$"+str(total)

valorTotal = horaMes(horaTrabalhada())
print(holerite(valorTotal))
