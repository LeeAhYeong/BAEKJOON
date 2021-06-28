'''
n = int(input())
current_su = 0
next_su = 1
answer = 0

def pibo(n):
    for _ in range(10):
        current_su = next_su
        next_su = current_su + next_su
    
print(next_su)
'''

def fibonacci(num):
    a, b = 0, 1 
    for i in range(num): 
        a, b = b, a+b 
    return a # 아래는 테스트로 출력해 보기 위한 코드입니다. 
    
print(fibonacci(10))


