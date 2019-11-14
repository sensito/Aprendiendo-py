from lamp import Lamp


def protected(func):
    def wrapper(password):
            if password == 'Foco':
                return func()
            else:
                print('Contraseña incorrecta')
    return wrapper

@protected
def menu():
    lamp = Lamp(is_turned_on=False)

    while True:
        command = str(input('''
                ¿Qué deseas hacer?
                [p]render
                [a]pagar
                [s]alir
            '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        elif command == 's':
            print('Adios :b')
            break
        else:
            print('Opcion nula')
def run():
    password = str(input('ingresa tu contraseña: '))
    menu(password)

if __name__ == '__main__':
    run()
