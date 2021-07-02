n = int(input())

def fibo(n) :
    if n < 2 :
        return n # 종료조건, 기저조건
    return fibo(n-1) + fibo(n-2)

print(fibo(n))
