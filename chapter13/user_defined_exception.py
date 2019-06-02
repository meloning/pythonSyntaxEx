class TooBigNumError(Exception):

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return 'too big number {}. Use 1~10'.format(self.val)


def user_defined_exception_test():
    num = int(input('1~10 사이의 정수 입력 : '))

    if num > 10:
        raise TooBigNumError(num)

    print('숫자 {} 를 입력했네'.format(num))


if __name__ == '__main__':
    user_defined_exception_test()