#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
def Fº_to_Cº():
    temp_fah = int(input('Temperatura em Farenheit:'))
    temp_celsius = int((5 * (temp_fah - 32) / 9))
    print('{}ºF equivale a {}ºC'.format(temp_fah, temp_celsius))
    return temp_celsius

Fº_to_Cº()