import re  # re 모듈 탑재


# 이메일 주소 정합성 체크를 위한 함수
def email_validation_check(email):
    """
        checking email address validation

        Args:
            email (str) : email address string

        Return:
            True or False (boolean) : the result of checking valdation
    """

    # 이메일 주소 정합성 유무 확인
    if re.findall(r'[\w.-]+@[\w.-]+.\w+', email)[0] != email:
        print(email, '는 이메일 주소 형식에 맞지 않습니다.')
        return False

    print(email, '는 이메일 주소로 적당합니다.')
    return True


if __name__ == '__main__':
    email_validation_check('#@c#o@gamil*cm')
    email_validation_check('isi.cho@gmail.com')
