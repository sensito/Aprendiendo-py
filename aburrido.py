# -*- coding: utf-8 -*-

def recive_word():
    word = str(input('Dame tu parabra para revertit'))
    return word

if __name__ == '__main__':
    word = recive_word()
    reverse_word = lambda word: word[::-1]
    reverse_word_space= lambda  reverse_word: reverse_word.split(' ')
    
