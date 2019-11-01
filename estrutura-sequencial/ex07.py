"""Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário."""

def dobro_area_quadrado():
    lado_quadrado = int(input('Digite o valor do lado do quadrado:'))
    area_quadrado = lado_quadrado ** 2
    print('O dobro da área do quadrado de lado {} é {}'.format(lado_quadrado, area_quadrado * 2))
    return area_quadrado * 2

dobro_area_quadrado()