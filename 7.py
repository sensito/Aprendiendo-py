# -*- coding: utf-8 -*-


def foreign_exchenge_calculator(ammount):
    mex_to_col_rate = 145.97

    return mex_to_col_rate * ammount

def run():
    print('Calculadora de divisas')
    print('Convierte pesos mx a pesos cl')
    print('')

    ammount = float(input('Ingresa la cantidad de pesos mx a convertir : '))

    result = foreign_exchenge_calculator(ammount)

    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount, result))
    print('')





if __name__ == '__main__':
    run()
