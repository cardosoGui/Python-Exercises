""" Tendo como dados de entrada a altura e o sexo de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
a.Para homens: (72.7*h) - 58
b.Para mulheres: (62.1*h) - 44.7 (h = altura)
c.Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso. """


print("*-- Qual é a sua altura? --*")
altura = input("Digite sua altura (Ex.: '1.80'cm): ")
print("*-- Qual é o seu peso --*")
peso = input("Digite seu peso (EX.: '72.8'kg): ")
print("Qual é a o seu sexo")
print("1----- Masculino")
print("2----- Feminino")
sexo = input("Digite o valor correspondente: ")
def pesoIdealHomem(altura,peso):
    pesoM = (peso*altura) - 58
    if pesoM <= 64.0:
        print(str(pesoM)+" Abaixo do peso!")
    elif pesoM > 64.0:
        print(str(pesoM)+" Peso ideal!")
    elif pesoM > 84.0:
        print(str(pesoM)+" A cima do peso ideial!")
    else:
        print(str(pesoM)+" Fora do peso ideal!")

def pesoIdealMulher(altura,peso):
    pesoF = (peso*altura) - 44.7
    if pesoF <= 34.0:
        print(str(pesoF)+" IMC Abaixo do peso!")
    elif pesoF > 34.0:
        print(str(pesoF)+" IMC Peso ideal!")
    elif pesoF > 60.0:
        print(str(pesoF)+" IMC A cima do peso ideial!")
    else:
        print(str(pesoF)+"Fora do peso ideal!")

if sexo == 1:
    pesoIdealHomem(altura,peso)
elif sexo == 2:
    pesoIdealMulher(altura,peso)
