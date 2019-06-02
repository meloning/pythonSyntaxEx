import re


def email_validation_check(email):

    regex = r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}'

    find_result = re.findall(regex, email)

    if find_result[0] != email:
        print(email, '는 이메일 주소 형식에 맞지 않습니다.')
        return False

    print(email, '는 이메일 주소로 적당합니다.')
    return True

