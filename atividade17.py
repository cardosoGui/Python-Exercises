""" Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
a.comprar apenas latas de 18 litros;
b.comprar apenas galões de 3,6 litros;
c.misturar latas e galões, de forma que o preço seja o menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. """

def cobertura():
    tamanho = input("Digite Metro Quadrado: ")
    litros = tamanho / 6
    
    if tamanho % 54 == 0 or tamanho % 18 == 0:
        latasMaior = tamanho / 54
        latasMenor = tamanho / 18
    else:
        latasMaior = int(tamanho/54)+1
        latasMenor = int(tamanho/18)+1
    print("*-----Opção de Latas-----*")
    print("1 ---- Latas de 18 Litros")
    print("2 ---- Latas de 3,6 Litros")
    select = int(input("Selecione: "))
    preco = latasMaior * 80
    preco_outro = latasMenor * 25
    if select == 1:
        print('%d latas de 18L' %latasMaior)
        print("R$ %.2f" %preco)
    elif select == 2:
        print('%d latas de 3,6L' %latasMenor)
        print("R$ %.2f" %preco_outro)
