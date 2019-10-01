# -*- coding: utf-8 -*-

def palindrome(word):
    reversed_letters = word[::-1]
    if reversed_letters == word:
        return True
    return False

def run():
    word = str(input('Escribe una palabra: '))
    result = palindrome(word)
    if result is True:
        print('{} es un palindromo'.format(word))
    else:
        print('{} no es un palindromo'.format(word))


if __name__ == '__main__':
    run()
