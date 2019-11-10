# -*- coding: utf-8 -*-


def protected(func):
    def wrapper(a, b):
        if a > b:
            return func(a, b)
        else:
            print('{} es menor que {}'.format(a, b))
    return wrapper


@protected
def protected_add(a, b):
    print(a+b)

def run():
    a = int(input('Ingresa un valor: '))
    b = int(input('Ingresa un valor: '))
    protected_add(a,b)



if __name__ == '__main__':
    run()
