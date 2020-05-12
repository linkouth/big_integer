import re
from datetime import datetime
from big_integer import BigInt


def handle_adding(a, b):
    s = str(a)
    s2 = str(b)
    print('a + b = ', end='')
    print(a.add(b))

    time_add_start = datetime.now()
    result = a.add(b)
    time_add_end = datetime.now()
    time_add_build_add_start = datetime.now()
    time_add_build_add_end = datetime.now()

    print('--------------------------------------------------')
    print('Результат: ', end='')
    print(int(str(result)) == (int(s) + int(s2)))
    print('Время работы реализации по Кнуту: ', end='')
    print(time_add_end - time_add_start)
    print('Время работы встроенной реализации: ', end='')
    print(time_add_build_add_end - time_add_build_add_start)
    print()


def main():
    is_continue = True
    while True:
        not_number = re.compile(r'^[-]?[0-9]+$')
        s = input('Введите первое число: ')
        while not not_number.match(s):
            print('Incorrect number')
            s = input('Введите первое число: ')

        a = BigInt(s)

        s2 = input('Введите второе число: ')
        while not not_number.match(s2):
            print('Incorrect number')
            s2 = input('Введите второе число: ')

        b = BigInt(s2)

        handle_adding(a=a, b=b)


if __name__ == '__main__':
    main()
