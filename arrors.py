# -*- coding: utf-8 -*-

contries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}
def run():
    while True:
        contry = str(input('Escribe el nombre del pais: '))
        try:
            print('La problacion de {} es de: {}'.format(contry, contries[contry]))
        except KeyError:
            print('No tenemos el dato de la poblacion de {}'.format(contry))
if __name__ == '__main__':
    run()
