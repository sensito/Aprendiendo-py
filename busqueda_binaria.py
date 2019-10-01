# -*- coding: utf-8 -*-

def run():
    pass
def binary_search(numbers, number_to_find, low, high):

    if low > high:
        return False

    mid = (low + high) / 2
    mid = int(mid)
    if numbers[mid] == number_to_find:
        return True

    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    elif numbers[mid] < number_to_find:
        return binary_search(numbers, number_to_find, mid + 1, high)

if __name__ == '__main__':
    numbers = range(1, 10000000, 2)

    number_to_find = int(input('Ingresa un numero: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)

    if result is True:
        print('Si esta')
    else:
        print('No esta')
    run()
