# -*- coding: utf-8 -*-
import os
MENU = ''' -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
        1.-Cambio de divisa
        2.-Salir
        '''

def currency_exchange():
        pass


def run():
    exit = False
    coins = {"1.-dolar": 15.15, "2.-pesos": 1.1}
    while not exit:
        os.system('cls')
        print_menu()
        option = int(input("Escoje una opcion >> "))
        if option is 1:
            for keys, values in coins.items():
                print("{}>>{}".format(keys, values))
            intercambiar = coins.va
            currency_exchange()
        elif option is 2:
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
