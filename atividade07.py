#Fa�a um Programa que calcule a �rea de um quadrado, em seguida mostre o dobro desta �rea para o usu�rio.

def calcAreaQuad(altura,largura):
    area = altura * largura
    return area
print("O Dobro da area: "+str(calcAreaQuad(input("Digite a Altura: "),input("Digite a Largura: ")*2))+" m� ")
