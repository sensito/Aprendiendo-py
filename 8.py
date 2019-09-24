# -*- coding: utf-8 -*-


def say_Hello(ege):
    if ege > 18:
        print('Hola senor')
    else:
        print('Hola nino')

def main():
    ege = int(input('Ingresa tu edad: '))
    print('')
    say_Hello(ege)


if __name__ == '__main__':
    main()
