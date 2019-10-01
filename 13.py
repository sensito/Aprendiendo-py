# -*- coding : utf-8 -*-
import random

def run():
    number_foud = False
    rand_number = random.randint(0, 20)

    while not number_foud:
        number = int(input('Intenta un numero: '))

        if number == rand_number:
            print('Felicidades encontraste el numero')
            number_foud = True
        elif number > rand_number:
            print('El numero es pequeno')
        else:
            print('El numero es mas grande')

if __name__ == '__main__':
    run()
