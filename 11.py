# -*- coding: utf-8 -*-

def three_Squares(Number_squares):
    for i in range(Number_squares):
        if i % 3 != 0:
            continue
        else:
            print(i)


def main():
    Number = int(input('Ingresa un numero: '))
    three_Squares(Number)



if __name__ == '__main__':
    main()
