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
