# -*- coding: utf-8 -*-





def factorial(number):
    if number == 0 :
        return 1
    return number * factorial(number - 1)


def main():
    number = int(input('Ingresa un numero: '))
    result = factorial(number)
    print(result)

if __name__ == '__main__':
    main()
