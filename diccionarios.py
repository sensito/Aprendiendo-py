# -*- coding: utf-8 -*-
import os


def Sum(calificaciones):
    suma = 0
    for value in calificaciones.values():
        suma += value
    return suma

def avg(sum, calificaciones):
    promedio = sum / len(calificaciones.values())
    return promedio

def exit():
    bool = str(input('Tienes mas calificaciones? [Y]es or [N]o: '))
    os.system('cls')
    if bool == 'Y' or bool == 'y':
        return False
    else:
        return True

def enter(calificaciones):
    salida = False
    while not salida:
        Name = str(input('Dame el nombre de tu materia: '))
        values = int(input('Dame la calificacion para {}: '.format(Name)))
        calificaciones[Name] = values
        os.system('cls')
        salida = exit()
    return calificaciones


def run():
    calificaciones = {}
    calificaciones = enter(calificaciones)
    suma = Sum(calificaciones)
    promedio = avg(suma, calificaciones)
    print('Tu promedio es: {}'.format(promedio))

if __name__ == '__main__':
    run()
