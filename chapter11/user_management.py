import user_email as ue
import user_password_re as upr


# 사용자 클래스 정의
class User:
    """
        This class keeping user's email address and password

        Put email address & password when creating instance.
        And also need to check validation of address & password.
    """

    # 초기화 함수 재정의
    def __init__(self, email, pwd):
        self.email = email
        self.pwd = pwd
        self.check_validation()  # 입력한 이메일 주소 및 비밀 번호 검증

    # 정합성 검증 함수 호출을 통한 이메일 주소 및 비밀번호 적합성 검증
    def check_validation(self):
        """ checking email & password validation """
        ue.email_validation_check(self.email)
        upr.password_validation_check(self.pwd)


if __name__ == '__main__':
    user1 = User('isi.cho@gmail.com', '3jkMf8Exe')
    print('=====================================')
    user2 = User('isi.cho@gm@il*cOm', 'eee')
    print('=====================================')
    user3 = User('i#i.cho@gmail.com', '3#kMEx90e')
