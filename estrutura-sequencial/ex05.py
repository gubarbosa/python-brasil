"""Faça um Programa que converta metros para centímetros."""

def metros_para_cm():
    qntd_metros = input('Escreva um valor de metros qualquer:')
    centimetros = qntd_metros * 100
    print('{} metros = {} centímetros'.format(qntd_metros, centimetros))
    return centimetros

metros_para_cm()