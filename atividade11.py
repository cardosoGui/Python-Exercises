"""Fa�a um Programa que pe�a 2 n�meros inteiros e um n�mero real.
Calcule e mostre:
a.o produto do dobro do primeiro com metade do segundo.
b.a soma do triplo do primeiro com o terceiro.
c.o terceiro elevado ao cubo."""

np = input("Digite um primeiro valor: ")
ns = input("Digite um segundo valor: ")
def dobroProduto(np,ns):
    dobro = np * 2
    metade = ns / 2
    conj = {np,ns}
    return conj
print("Os Valores s�o: "+str(dobroProduto(np,ns)))
