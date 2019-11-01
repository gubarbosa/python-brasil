"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#\n Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
# variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
# e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas."""

limite_kg = 50
multa_por_excedente = 4.00
peso_peixes = float(input('Digite o peso de peixes pescados: '))

def pescador(peso_peixes):
    excesso = peso_peixes - limite_kg
    if excesso > 0:
        multa = multa_por_excedente * excesso
        print('João teve um excesso de {} kg de peixes sobre o limite estabelecido, com uma multa de R${:.2f} '.format(excesso, multa))
    else:
        multa = 0
        print('João não passou do limite de peixes estabelecido, obteve {} kg de peixes'.format(peso_peixes))
    return excesso, multa

pescador(peso_peixes)