'''
문제
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

*출제 의도*
- 스택에 활용되는 여러가지 내장 메소드를 잘 활용할 수 있는지 기본 문법을 체크하는 문제다.
'''
import sys
test_case = int(sys.stdin.readline().rstrip())
result = []
for i in range(test_case):
    each_case = sys.stdin.readline().split()
    if each_case[0] == 'push':
        result.append(int(each_case[-1]))
    elif each_case[0] == 'pop':
        if result == []:
            print(-1)
        else:
            print(result.pop())
    elif each_case[0] == 'size':
        print(len(result))
    elif each_case[0] == 'empty':
        if result == []:
            print(1)
        else:
            print(0)
    else:
        if result == []:
            print(-1)
        else:
            print(result[-1])
