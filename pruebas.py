# -*- coding: utf-8 -*-
import os
MENU = ''' -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
        1.-Agregar nueva moneda
        2.-Borra una moneda
        2.-Cambio de divisa
        3.-Salida'''

class modifi_coins():
    """docstring for coin."""
    def add_coin(coins):
        coins_clas = dict(**coins)
        print(coins_clas)
        print(type(coins_clas))
        currency = str(input('Nombre de tu monesa: '))
        value = float(input('Ingresa el valor de te moneda: '))
        coins_clas[currency] = value
        return coins_clas


    def menu_currency(arg):
        for keys, values in prueba.items():
            print("{}.-{}".format(keys, values))
    def currency_exchange():
        pass


def run():
    prueba = modifi_coins()
    exit = False
    coins = {"Dolar":15.15,"pesos":1.1}
    while not exit:
        os.system('cls')
        print_menu()
        option = int(input("Escoje una opcion >> "))
        if option is 1:
            print(coins)
            coins = prueba.add_coin(coins)
            print(coins)
            os.system('pause')
        elif option is 2:
            currency_exchange()
        elif option is 3:
            exit = True
        else:
            print("Opcion invalida")
            os.system('pause')
    print("Adios")
    os.system('pause')
    os.system('cls')


def print_menu():
    print(MENU)
if __name__ == "__main__":
    run()
