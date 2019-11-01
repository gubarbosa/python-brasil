"""Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58"""
from math import ceil

altura = float((input('Digite sua altura:')))

def peso_ideal(altura):
    peso_bom = ((72.7 * altura) - 58)
    print('De acordo com sua altura de {}m, seu peso ideal é de {:.1f}kg'.format(altura, peso_bom))
    return peso_bom

peso_ideal(altura)