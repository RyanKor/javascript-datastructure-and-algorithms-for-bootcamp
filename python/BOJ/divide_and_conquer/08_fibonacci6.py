'''
문제
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. n은 1,000,000,000,000,000,000보다 작거나 같은 자연수이다. -> 주어진 수의 범위가 어마어마하게 크다.

출력
첫째 줄에 n번째 피보나치 수를 1,000,000,007으로 나눈 나머지를 출력한다.
'''

import sys

num = int(sys.stdin.readline())


# 동적 프로그래밍 -> 메모리 초과
# def fibonacci(number):
#     fibo = {0: 0, 1: 1, 2: 1}
#     if number == 0:
#         return 0
#     if number == 1 or number == 2:
#         return 1
#     if number > 2:
#         for i in range(3, number+1):
#             fibo[i] = fibo[i-1]+fibo[i-2]
#     return fibo[number]


# print(fibonacci(num) % 1000000007)


# recursion function -> 메모리 초과
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


print(Fibonacci(num) % 1000000007)