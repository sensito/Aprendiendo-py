# -*- coding: utf-8 -*-

import turtle
def main():
    window = turtle.Screen()
    Daniel = turtle.Turtle()

    make_square(Daniel)
    turtle.mainloop()

def make_square(Daniel):
    length = int(input('Tamano del cuadrado: '))

    for i in range(4):
        make_line_and_turn(Daniel, length)

def make_line_and_turn(Daniel, length):
    Daniel.forward(length)
    Daniel.left(90)


if __name__ == '__main__':
    main()
