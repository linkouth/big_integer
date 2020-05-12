from big_integer import BigInt


def test_all():
    test_division()


def test_division():
    n = 5000
    m = 250
    is_correct = True
    for i in range(1, n):
        a = BigInt(str(i))
        for j in range(1, m):
            b = BigInt(str(j))
            custom_result = a.div(b)
            build_in_result = i // j
            if int(str(custom_result)) != build_in_result:
                print(f'{str(custom_result)} is not equal to {build_in_result}')
                is_correct = False
                break
    if is_correct:
        print('Division is correct')
    else:
        print('Division is not correct')


def main():
    test_all()


if __name__ == '__main__':
    main()
