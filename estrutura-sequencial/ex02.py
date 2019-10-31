#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
def numero_informado():
    numero = int(input('Digite um número qualquer:'))
    print('O número informado é {}'.format(numero))
    return numero

numero_informado()