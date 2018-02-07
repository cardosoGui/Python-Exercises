# -*- coding: cp1252 -*-
"""Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58."""
altura = input("Digite uma altura: ")
def pesoIdeal(altura):
    iPeso = (72.7 * altura) - 58
    return iPeso
print("Seu peso ideal: "+str(pesoIdeal(altura)))
    
