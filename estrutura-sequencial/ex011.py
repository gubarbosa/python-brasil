"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo."""

inteiro1 = int(input('Primeiro número inteiro:'))
inteiro2 = int(input('Segundo número inteiro:'))
real1 = float(input('Número real:'))

def calcular_numeros(inteiro1, inteiro2, real1):
    calculo1 = ((inteiro1 * 2) * inteiro2 / 2)
    calculo2 = ((inteiro1 * 3) + real1)
    calculo3 = ((real1 ** 3))

    print('o produto do dobro do primeiro com metade do segundo: {} \n'
          'a soma do triplo do primeiro com o terceiro: {} \n'
          ' o terceiro elevado ao cubo: {}'.format(calculo1, calculo2, calculo3))
    return calculo1, calculo2, calculo3

calcular_numeros(inteiro1, inteiro2, real1)