""" Faça um programa que peça o tamanho de um arquivo para download
(em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do
arquivo usando este link (em minutos). """

def download():
    tamanho =  input("Digite o tamanho do arquivo em MB: ") * 1024
    velocidade = 1000 * input("Digite a velocidade da internet Mbps: ")
    bits = (velocidade / 100000) * 1024
    real = velocidade / bits
    print(real)
    conexao = float(tamanho / real)
    print(conexao)
    tempo = float(conexao / 60)
    return tempo
    
