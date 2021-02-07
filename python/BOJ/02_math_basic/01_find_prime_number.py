'''
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

*풀이 주의 사항*

- 내가 알고 있다고 생각하지만, 사실 모르고 있는 것들이 꽤 있다.
- 소수에 관한 알고리즘 문제도 이전에도 많이 풀었지만, 막상 다른 사람 코드를 안찾아보고 내가 풀려고 해보니 손이 멈춘다.
- 즉 소수에 관한 알고리즘 풀이는 여태까지 내 실력이 아니었다는 뜻이 된다.
'''
import sys

test_case = int(sys.stdin.readline())
cnt = 0

prime_number = list(map(int, sys.stdin.readline().split()))

for i in prime_number:
    count = 0
    if i == 1:
        continue
    for j in range(2, i+1):
        if i % j == 0:
            count += 1
    if count == 1:  # 이 코드를 추가 안하면, 반드시 에러가 발생한다.
        cnt += 1
print(cnt)