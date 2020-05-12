import re
from datetime import datetime
from big_integer import BigInt


def handle_subtracting(a, b):
    s = str(a)
    s2 = str(b)
    print('a - b = ', end='')
    print(a.subtract(b))

    time_subtract_start = datetime.now()
    result = a.subtract(b)
    time_subtract_end = datetime.now()
    time_add_build_subtract_start = datetime.now()
    time_add_build_subtract_end = datetime.now()

    print('--------------------------------------------------')
    print('Верно: ', end='')
    print(int(str(result)) == (int(s) - int(s2)))
    print('Время работы реализации по Кнуту: ', end='')
    print(time_subtract_end - time_subtract_start)
    print('Время работы реализации встроенной: ', end='')
    print(time_add_build_subtract_end - time_add_build_subtract_start)
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

        handle_subtracting(a=a, b=b)


if __name__ == '__main__':
    main()
