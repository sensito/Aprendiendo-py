# -*- coding: utf-8 -*-

def run(word):
    counter = 0
    with open('aaaa.txt', encoding='utf8') as f:
        for line in f:
            counter += line.count(word)
    print('{} esta {}'.format(word, counter))


if __name__ == '__main__':

    word = str(input('Dame la palabra a buscar en el texto: '))
    run(word)
