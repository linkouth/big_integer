import re
from datetime import datetime
from big_integer import BigInt


def handle_division(a, b):
    div_result = None
    mod_result = None
    s2 = str(b)
    if int(s2) != 0:
        time_div_start = datetime.now()
        div_result = a.div(b)
        time_div_end = datetime.now()
        time_mod_start = datetime.now()
        mod_result = a.rem(b)
        time_mod_end = datetime.now()
    else:
        # Обработка ошибок
        print('Ошибка деления на ноль!')
        return

    # Вывод результата деления
    time_build_div_start = datetime.now()
    time_build_div_end = datetime.now()
    time_build_mod_start = datetime.now()
    time_build_mod_end = datetime.now()

    print('--------------------------------------------------')
    print('a / b = ', end='')
    print(div_result)

    print()
    print('--------------------------------------------------')
    print('a % b = ', end='')
    print(mod_result)

    print()
    print('--------------------------------------------------')
    print('Верно: ', end='')
    print(int(str(div_result)) == (int(str(a)) // int(str(b))))
    print('Сравнение времени работы деления')
    print('Время работы реализация по Кнуту: ', end=' ')
    print(time_div_end - time_div_start)
    print('Время работы встроенной реализация: ', end=' ')
    print(time_build_div_end - time_build_div_start)

    print()
    print('--------------------------------------------------')
    print('Верно: ', end='')
    print(int(str(mod_result)) == (int(str(a)) % int(str(b))))
    print('Сравнение времени работы нахождения остатка')
    print('Время работы реализация по Кнуту: ', end=' ')
    print(time_mod_end - time_mod_start)
    print('Время работы встроенной реализация: ', end=' ')
    print(time_build_mod_end - time_build_mod_start)


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

        handle_division(a=a, b=b)


if __name__ == '__main__':
    main()
