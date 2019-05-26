# 피보나치 수열을 위한 모듈

def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

# 외부에서 CLI로 호출시
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1])) # 1번째 외부 인자값을 사용

