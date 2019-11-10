# -*- coding: utf-8 -*-

def protected(func):
    def wrapper(password):

        if password == 'platzi':
            return func()
        else:
            print('Contraseña incorrecta')
    return wrapper

@protected
def protected_func():
    print('Tu contraseña es correcta')


def run():
    pass

if __name__ == '__main__':
    password = str(input('ingresa tu contraseña: '))
    protected_func(password)
