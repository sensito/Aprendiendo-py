# -*- coding: utf-8 -*-

class Traslate():
    _KEYS = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '0': '.----',
        '1': '..---',
        '2': '..--',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '.': '.-.-.-',
        ',': '--..--',
        '?': '..--..',
        '!': '-.-.--',
        '/': '-..-.',
        '@': '.--.-.',
        ' ': '/',
        '': (),
        }

    def cypher(self, _message):
        words = _message.split(' ')
        cypher_message = []

        for word in words:
            cypher_word = ''
            for letter in word:
                cypher_word += self._KEYS[letter]
                cypher_word += ' '
            cypher_word += '/'
            cypher_message.append(cypher_word)
        return ' '.join(cypher_message)


    def decipher(self):
        words = _message.split(sep=' ')
        cosa = words
        words = []
        for letter in range(len(cosa)):
            words.append([cosa[letter]])
        decipher_message = []

        for word in words:
            decipher_word = ''
            for letter in word:

                for key, value in self._KEYS.items():
                    if value == letter:
                        decipher_word += key

            decipher_message.append(decipher_word)

        return decipher_message
