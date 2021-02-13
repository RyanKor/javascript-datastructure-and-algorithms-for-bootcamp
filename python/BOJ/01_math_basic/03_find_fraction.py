'''
문제
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

1/1	1/2	1/3	1/4	1/5	…
2/1	2/2	2/3	2/4	…	…
3/1	3/2	3/3	…	…	…
4/1	4/2	…	…	…	…
5/1	…	…	…	…	…
…	…	…	…	…	…
이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

출력
첫째 줄에 분수를 출력한다.


*풀이에서 주의 사항*
이 방향에는 나름대로의 규칙이 존재하는데 분수들을 진행방향대로 나열해보자면
1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> 1/3 이런식으로 진행이 된다.
아직 감이 오지않는 사람들을 위해 조금더 구분을 해주자면
1/1 ->      1/2 -> 2/1 ->      3/1 -> 2/2 -> 1/3
1개 2개 3개 이런식으로 n개씩 늘어난다고 친다면
홀수씩 늘어날 때는 분자는 n부터 1까지 줄어들고 분모는 1부터 n까지 늘어난다.
짝수씩 늘어날 때는 분자는 1부터 n까지 늘어나고 분모는 n부터 1까지 줄어든다.
이 규칙을 발견하기까지가 쉽지 않은 문제였다.
'''
# 1193번

x = int(input())
num_list = []

num = 0
num_count = 0

while num_count < x:
    num += 1
    num_count += num

num_count -= num

if num % 2 == 0:
    i = x - num_count
    j = num - i + 1
else:
    i = num - (x - num_count) + 1
    j = x - num_count

print("{}/{}".format(i, j))
