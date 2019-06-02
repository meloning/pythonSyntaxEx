with open('../chapter15/common_test.py', 'r') as f: # with -> file close 까지 함께 실행
    f_list = f.readlines()

print(f.closed)
print(f_list)