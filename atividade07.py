#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

def calcAreaQuad(altura,largura):
    area = altura * largura
    return area
print("O Dobro da area: "+str(calcAreaQuad(input("Digite a Altura: "),input("Digite a Largura: ")*2))+" m² ")
