'''
문제
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

*알아야할 것*
- 유클리드 호제법
- 
'''
import sys

a, b = map(int, sys.stdin.readline().split())

# 36, 48
# 2 2 3 3 / 2 2 2 2 3

# 최대 공약수
# 여기서 적용되는 공식은 '유클리드 호제법'이라는 방법이다.


def gdc(x, y):
    while y > 0:
        x, y = y, x % y
    return x


# 최소 공배수

def lcm(x, y):
    return x * y // gdc(x, y)


print(gdc(a, b))
print(lcm(a, b))
