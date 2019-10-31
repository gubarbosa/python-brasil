#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
def Cº_to_Fº():
    celsius = int(input('Temperatura em Cº:'))
    temp_fah = int((9/5) * celsius + 32)
    print('{}Cº equivale a {}Fº'.format(celsius, temp_fah))
    return temp_fah

Cº_to_Fº()