"""Faça um Programa que peça o raio de um círculo, calcule e mostre sua área"""

def area_circulo():
    raio = int(input('Digite o valor do raio do círculo:'))
    area = 3.14 * (raio * raio)
    print('Área do círculo: {}'.format(area))
    return area

area_circulo()