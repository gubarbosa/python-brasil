"""Faça um Programa que peça dois números e imprima a soma."""

def soma():
    numero1 = int(input('Digite o primeiro número:'))
    numero2 = int(input('Digite o segundo número:'))
    soma = numero1 + numero2
    print('{} + {} = {}'.format(numero1, numero2, soma))
    return soma

soma()
#numero_1 = input('Digite dois números para efetuar a soma:')
#print(int(numero_1[0]) + int(numero_1[-1]))