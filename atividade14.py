""" João Papo-de-Pescador, homem de bem,
comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido
pelo regulamento de pesca do estado de São Paulo (50 quilos)
deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes)
e verifique se há excesso. Se houver,
gravar na variável excesso e na variável multa
o valor da multa que João deverá pagar.
Caso contrário mostrar tais variáveis com o conteúdo ZERO. """
print("*--- Calculadora de multa por quilo ---*")
print("AVISO: Se o peso for maior que 50 quilos, a multa será de 4.00$ por quilo excedente!")

peso = input("Digite o peso do peixe: ")
def controlarPeso(peso):
    if peso > 50:
        excesso = (peso - 50)
        multa = excesso * 4.00
        return "Valor da multa: '"+str(multa)+"$'"+" Peso em excesso: '"+str(excesso)+"Kg'"
    
print("Valores convertidos com sucesso! "+str(controlarPeso(peso)))
