import traceback


def exceptioni_test():
    print("[1] Can ou add 2 and '2' in python?")

    try:
        print("[2] Try it", 2 + '2')
    except TypeError:
        print('[2] I got TypeError! Check below!')
        traceback.print_exc()
        raise  # 해당 에러를 다시 발생

    print("[3] It's not possible to add integer and string together")


def exception_test2(file_path):
    try:
        file = open(file_path, 'r')
    except IOError:
        print('Can\'t open', file_path)
    else:
        print('File has', len(file.readlines()), 'lines')
        file.close()
    finally:
        print('I just tried to read this file.', file_path)


if __name__ == '__main__':
    # exceptioni_test()

    exception_test2('../chapter11/user_management.py')
    exception_test2('../chapter11/user_managemen.py')
