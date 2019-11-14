from traslate import Traslate
def run():
    while True:
        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografía. ¿Qué deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

        if command == 'c':
            message = str(input('Escribe tu mensaje: '))
            tras = Traslate(initial_message=message)
            cypher_message = tras.cypher()
            print(cypher_message)
        elif command == 'd':
            message = str(input('Escribe tu mensaje cifrado: '))
            tras = Traslate(initial_message=message)
            decypher_message = tras.decipher()
            print(decypher_message)
        elif command == 's':
            print('salir')
        else:
            print('¡Comando no encontrado!')


if __name__ == '__main__':
    print('M E N S A J E S  C I F R A D O S')
    run()
