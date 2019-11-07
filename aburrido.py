# -*- coding: utf-8 -*-

def recive_word():
    word = str(input('Dame tu parabra para revertir:  '))
    return word

def invert_words(word):
    return word[::-1]



if __name__ == '__main__':
    word = recive_word()
    reverse_word = invert_words(word)
    print(reverse_word)
