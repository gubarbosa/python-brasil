#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def media():
    nota_1 = int(input('Digite a primeira nota bimestral:'))
    nota_2 = int(input('Digite a segunda nota bimestral:'))
    nota_3 = int(input('Digite a terceira nota bimestral:'))
    nota_4 = int(input('Digite a quarta nota bimestral:'))
    media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
    print('A média do aluno é {}'.format(media))
    return media

media()