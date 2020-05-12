import re
from datetime import datetime
from big_integer import BigInt


def handle_multiplication(a, b):
    s = str(a)
    s2 = str(b)

    print('a * b = ', end='')
    print(a.multiply(b))

    time_multiple_start = datetime.now()
    result = a.multiply(b)
    time_multiple_end = datetime.now()
    time_multiple_build_start = datetime.now()
    time_multiple_build_end = datetime.now()

    print('--------------------------------------------------')
    print('Верно: ', end=' ')
    print(int(str(result)) == (int(s) * int(s2)))
    print('Время работы реализации по Кнуту: ', end='')
    print(time_multiple_end - time_multiple_start)
    print('Время работы встроенной реализации: ', end='')
    print(time_multiple_build_end - time_multiple_build_start)
    print()


def main():
    while True:
        not_number = re.compile(r'^[-]?[0-9]+$')
        s = input('Введите первое число: ')
        while not not_number.match(s):
            print('Некорректное число')
            s = input('Введите первое число: ')

        a = BigInt(s)

        s2 = input('Введите второе число: ')
        while not not_number.match(s2):
            print('Некорректное число')
            s2 = input('Введите второе число: ')

        b = BigInt(s2)

        handle_multiplication(a=a, b=b)


if __name__ == '__main__':
    main()
