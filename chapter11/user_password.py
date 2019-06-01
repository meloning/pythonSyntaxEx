# 비밀번호 정합성 체크를 위한 함수
def password_validation_check(pwd):

    """
        checking password validation

        Args:
            pwd (str) : password string

        Return:
            true or False (boolean) : the result of checking validation
    """

    if len(pwd) < 6 or len(pwd) > 12:
        print(pwd, '의 길이가 적당하지 않습니다.')
        return False

    for c in pwd:
        if not c.isnumeric() and not c.isalpha():
            print(pwd, '는 숫자와 영문자로만 구성되지 않았습니다.')
            return False

    upper = False
    lower = False

    for c in pwd:

        if upper and lower:
            break

        if c.isalpha():

            if not upper:
                upper = c.isupper()

            if not lower:
                lower = c.islower()

    if not upper or not lower:
        print(pwd, '는 영문 대문자와 소문자가 함께 존재하지 않습니다.')
        return False

    print(pwd, '는 비밀 번호로 적당합니다.')
    return True

if __name__ == '__main__':
    password_validation_check('23jke')
    password_validation_check('432rewvb53')
    password_validation_check('2@3jke%')
    password_validation_check('3k39QLe6o0')