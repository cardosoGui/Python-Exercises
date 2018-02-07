""" Fa�a um programa para uma loja de tintas.
O programa dever� pedir o tamanho em metros quadrados da �rea a ser pintada.
Considere que a cobertura da tinta � de 1 litro para cada 3 metros quadrados
e que a tinta � vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usu�rio a quantidades de latas de tinta a serem compradas e o pre�o total. """

print("*---Loja de tintas---*")

def cobertura():
    tamanho = int(input('Metros Quadrados: '))
    litros = tamanho / 3
    if tamanho % 54 == 0:
        latas = tamanho / 54
    else:
        latas = int(tamanho/54)+1
    preco = latas * 80
    print('%d latas' %latas)
    print('R$ %.2f' %preco)


try:
    print(cobertura())
except Exception:
    print("Erro")
