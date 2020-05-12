class BigInt:
    BASE = 1000000000
    DEFAULT_BASE = 10
    BASE_KOEF = 9

    # Конструктор
    def __init__(self, init_s):
        self.is_negative = False
        self.value = []

        unsigned_str = init_s
        if len(init_s) and init_s[0] == '-':
            self.is_negative = True
            unsigned_str = init_s[1:]

        buf = ''
        for c in unsigned_str[::-1]:
            buf += c
            if len(buf) == self.BASE_KOEF:
                self.value.append(int(buf[::-1]))
                buf = ''

        if len(buf):
            self.value.append(int(buf[::-1]))

    # Функция обработчик сложения
    def add(self, number):
        if not self.is_negative and not number.is_negative:
            return self.add_positive(self, number)
        elif self.is_negative and number.is_negative:
            return self.add_positive(self, number, True)
        else:
            if self.is_negative:
                return self.subtract_positive(number, self)
            else:
                return self.subtract_positive(self, number)

    # Реализация сложения по Кнуту
    def add_positive(self, first, second, negative=False):
        ans = BigInt('')
        if len(first.value) < len(second.value):
            for _ in range(len(second.value) - len(first.value)):
                first.value.append(0)
        else:
            for _ in range(len(first.value) - len(second.value)):
                second.value.append(0)

        k = 0
        for i in range(len(first.value)):
            ans.value.append((first.value[i] + second.value[i] + k) % self.BASE)
            k = (first.value[i] + second.value[i] + k) // self.BASE

        ans.value.append(k)
        ans.is_negative = negative

        return ans.normalized()

    # Функция обработчик вычитания
    def subtract(self, number):
        if not self.is_negative and not number.is_negative:
            return self.subtract_positive(self, number)
        elif self.is_negative and number.is_negative:
            return self.subtract_positive(number, self)
        else:
            if self.is_negative:
                return self.add_positive(self, number, True)
            else:
                return self.add_positive(self, number)

    # Реализация вычитания по Кнуту
    def subtract_positive(self, first, second):
        ans = BigInt('')
        if len(first.value) < len(second.value):
            for _ in range(len(second.value) - len(first.value)):
                first.value.append(0)
        else:
            for _ in range(len(first.value) - len(second.value)):
                second.value.append(0)

        k = 0

        for i in range(len(first.value)):
            ans.value.append(first.value[i] - second.value[i] + k)
            if ans.value[-1] < 0:
                ans.value[-1] += self.BASE
                k = -1
            else:
                k = 0
        if k == -1:
            c = self.subtract_positive(second, first)
            c.is_negative = True
            return c
        else:
            return ans.normalized()

    # Реализация умножения по Кнуту
    def multiply(self, second):
        ans = BigInt('')
        for _ in range(len(self.value) + len(second.value) + 1):
            ans.value.append(0)

        for idx in range(len(self.value)):
            k = 0
            i = 0
            while i < len(second.value):
                tmp = second.value[i] * self.value[idx] + ans.value[i + idx] + k
                ans.value[i + idx] = tmp % self.BASE
                k = tmp // self.BASE
                i += 1
            ans.value[idx + len(second.value)] = k

        ans.is_negative = self.is_negative != second.is_negative
        return ans.normalized()

    #
    # Функция обработчик для использования деления по Кнуту или короткого
    #
    def div(self, number):
        if int(str(self)) < int(str(number)):
            return BigInt('0')
        if len(number.value) == 1:
            return self.div_mod_short(number.value[0], self.is_negative != number.is_negative)
        else:
            return self.div_mod_positive(self, number, self.is_negative != number.is_negative)

    #
    # Функция обработчик для нахождения остатка
    #
    def rem(self, number):
        if int(str(self)) < int(str(number)):
            return self
        if len(number.value) == 1:
            return self.div_mod_short(number.value[0], self.is_negative != number.is_negative, False)
        else:
            return self.div_mod_positive(self, number, self.is_negative != number.is_negative, False)

    #
    # Реализация алгоритма по Кнуту
    #
    def div_mod_positive(self, a, b, is_negative=False, is_div=True):
        # D1 Нормализация
        d = self.BASE // (b.value[-1] + 1)  # вычисление d. BASE == b
        u = a  # временные переменные
        v = b  # для иммутабельности
        n = len(v.value)  # размерность делителя
        m = len(u.value) - len(v.value)  # разность между размерностями делимого и делителя
        u = u.multiply(BigInt(str(d)))  # умножение u на d
        v = v.multiply(BigInt(str(d)))  # умножение v на d
        if len(u.value) == len(a.value):
            u.value.append(0)  # введение дополнительного разряда

        ans = BigInt('')  # результат деления
        for _ in range(m + 1):
            ans.value.append(0)

        # D2 Инициализация
        j = m
        while j >= 0:
            # D3 Вычислить q
            q = (u.value[j + n] * self.BASE + u.value[j + n - 1]) // v.value[-1]  # Вычиcляем q
            r = (u.value[j + n] * self.BASE + u.value[j + n - 1]) % v.value[-1]  # Вычиcляем r

            # Проверка условия в шаге D3
            while (q == self.BASE or q * v.value[n - 2] > self.BASE * r + u.value[j + n - 2]) and r < self.BASE:
                q -= 1
                r += v.value[n - 1]

            # D4 Умножить и вычесть
            temp = BigInt(str(q)).multiply(v)  # Результат умножения q на v
            while len(temp.value) < n + 1:
                temp.value.append(0)

            temp_big = BigInt('')
            temp_big.value = []

            for idx in range(n + 1):
                temp_big.value.append(u.value[idx + j])

            # Вычитаем из (u[j+n]...u[j]) результат умножения q на v
            temp_big = temp_big.subtract(temp)

            flag_negative = temp_big.is_negative

            # Добавляем b^(n+1), если отрицательный результат
            if flag_negative:
                # инициализируем b^(n+1)
                b_powered = BigInt('')
                b_powered.value = []
                for idx in range(n + 1):
                    b_powered.value.append(0)
                b_powered.value.append(1)

                # Складываем b^(n+1) к отрицательному числу,
                # полученного в предыдущем шаге
                temp_big = temp_big.add(b_powered)

                for idx in range(n + 1):
                    u.value[idx + j] = temp_big.value[idx]
            else:
                while len(temp_big.value) < n + 1:
                    temp_big.value.append(0)

                for idx in range(n + 1):
                    u.value[idx + j] = temp_big.value[idx]

            # D5 Проверка остатка
            ans.value[j] = q
            # D6 Компенсировать сложение
            if flag_negative:
                ans.value[j] -= 1

                temp_big = BigInt('')
                temp_big.value = []
                for idx in range(n + 1):
                    temp_big.value.append(u.value[j + idx])
                temp_big = temp_big.add(v)

                for idx in range(n + 1):
                    u.value[j + idx] = temp_big.value[idx]

            # D7 цикл по j
            j -= 1

        ans.is_negative = is_negative
        ans.normalized()

        # D8 Денормализация
        if is_div:
            return ans
        else:
            temp_big = BigInt('')
            temp_big.value = []

            for idx in range(n):
                temp_big.value.append(u.value[idx])

            return temp_big.div(BigInt(str(d)))

    # Реализация короткого деления
    def div_mod_short(self, number, is_negative, is_div=True):
        ans = BigInt('')
        for _ in range(len(self.value)):
            ans.value.append(0)
        k = 0
        for idx in range(len(self.value)):
            i = len(self.value) - 1 - idx
            cur = self.value[i] + k * self.BASE
            ans.value[i] = cur // number
            k = cur % number

        ans.normalized()
        ans.is_negative = is_negative
        if is_div:
            return ans
        else:
            return BigInt(str(k))

    # Реализация возведения в степень
    def pow(self, power, mod):
        # A1 Инициализация
        n = power
        y = BigInt('1')
        z = self

        while n.compare_with(BigInt('0')) != 0:
            # A2 Деление N пополам
            is_even = BigInt(str(n.rem(BigInt('2')))).compare_with(BigInt('0'))

            n = n.div(BigInt('2'))

            if is_even != 0:
                # A3 Умножение Y на Z
                y = (z.multiply(y)).rem(mod)
                # A4 N = 0?
                is_zero = n.compare_with(BigInt('0'))
                if is_zero == 0:
                    return y
            # A5 Возведение Z в квадрат
            z = (z.multiply(z)).rem(mod)

        return y

    def compare_with(self, big_number):
        if self.is_negative == big_number.is_negative:
            if self.is_negative:
                return -self.compare_by_radix(big_number)
            else:
                return self.compare_by_radix(big_number)
        else:
            if self.is_negative:
                return -1
            else:
                return 1

    def compare_by_radix(self, big_number):
        if len(self.value) == len(big_number.value):
            idx = len(self.value) - 1
            while idx >= 0 and self.value[idx] == big_number.value[idx]:
                idx -= 1
            if idx < 0:
                return 0
            else:
                if self.value[idx] > big_number.value[idx]:
                    return 1
                elif self.value[idx] < big_number.value[idx]:
                    return -1
                else:
                    return 0
        else:
            if len(self.value) > len(big_number.value):
                return 1
            else:
                return 0

    # Нормализация числа
    def normalized(self):
        while len(self.value) and len(self.value) > 1 and self.value[-1] == 0:
            del self.value[-1]

        return self

    # Представление Длинного числа в читаемом виде (в виде строки)
    def __str__(self):
        if len(self.value) == 1 and self.value[0] == 0:
            return '0'

        not_normalized = ''

        for v in self.value:
            not_normalized += f'{v:09}'[::-1]
        normalized = not_normalized[::-1]

        i = 0
        while normalized[i] == '0':
            i += 1
        if i > 0:
            normalized = normalized[i:]

        if self.is_negative:
            return '-' + normalized
        else:
            return normalized
