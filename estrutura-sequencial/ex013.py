#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

escolha_sexo = str(input('Escreva seu gênero: Homem ou Mulher: ')).lower().capitalize()
altura = float(input('Digite sua altura: '))

def peso_idealv2(escolha_sexo, altura):
    if escolha_sexo == 'Homem':
        peso_ideal = (72.7 * altura) - 58
    elif escolha_sexo == 'Mulher':
        peso_ideal = (62.1 * altura) - 44.7
    else:
        pass

    print('Sendo {}, e com {}m, seu peso ideal é de {:.1f}kg'.format(escolha_sexo.lower(), altura, peso_ideal))
    return peso_ideal

peso_idealv2(escolha_sexo, altura)