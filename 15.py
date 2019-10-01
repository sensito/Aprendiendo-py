# -*- coding: utf-8 -*-

def palindrome(word):
    reverse_letters =[]

    for letter in word:
        reverse_letters.insert(0, letter)
    reverse_word = ''.join(reverse_letters)
    if reverse_word == word:
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
