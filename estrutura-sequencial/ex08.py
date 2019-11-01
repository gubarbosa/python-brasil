"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""

def salario_mensal():
    lucro_hora = int(input('Dinheiro ganho por hora:'))
    horas_mensais = int(input('Horas trabalhadas no mês:'))
    salario_total = lucro_hora * horas_mensais
    print('O salário mensal é de: R$ {}'.format(salario_total))
    return salario_total

salario_mensal()
