/*
제목 : 큰 수의 법칙
난이도 : 하
풀이 시간 : 30분
시간 제한 : 1초 (시간 복잡도 제한 시간)
메모리 제한 : 128 MB (공간 복잡도 제한 시간)
기출 : 2019 국가 교육기관 코딩 테스트

'큰 수의 법칙'은 일반적으로 통계 분야에서 다뤄지는 내용이지만, 승태는 본인만의 방식으로 다르게 사용하고 있다.
승태의 큰 수의 법칙은 다양한 수로 이뤄진 배열이 있을 때, 주어진 수들을 M번 더해 가장 큰 수를 만드는 법칙이다.
단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수는 없는 것이 이 법칙의 특징이다.

예를 들어, 순서대로 2,4,5,4,6으로 이뤄진 배열이 있을 때, M이 8이고, K가 3이라고 가정하자.
이 경우 특정한 인덱스의 수가 연속해서 세 번까지만 더해질 수 있으므로 큰 수의 법칙에 따른 결과는 

6+6+6+5+6+6+6+5인 46이 된다.

단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다. 예를 들어 순서대로

3,4,3,4,3 으로 이뤄진 배열이 있을 때, M이 7이고, K가 2라고 가정하자. 

이 경우 두 번째 원소에 해당하는 4와 네 번째 원소에 해당하는4를 번갈아 두 번씩 더하는 것이 가능하다. 결과적으로

4+4+4+4+4+4+4 = 28이 도출된다.

배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 승태의 큰 수의 법칙에 따른 결과를 출력하시오.

1. 입력 조건

- 첫째 줄에 N(2,<=N<=1,000), M(1<=M<=10,000), K(1<=K<=10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.

- 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.

- 입력으로 주어지는 K는 항상 M보다 작거나 같다.

2. 출력 조건

- 첫째 줄에 승태의 큰 수의 법칙에 따라 더해진 답을 출력한다.

입력 예시

5 8 3

2 4 5 4 6

출력 예시

46
*/

/*
JS에는 기본적으로 입출력을 담당해서 받아오는 편리한 명령어가 없다.
예를 들어, 파이썬의 input 값이나 JAVA의 scan 등에 대한 것이다.
그래서 아래처럼 코드가 조금 장황하더라도 값을 Node.js를 활용해 아래와 같이 받아온다.
*/

const readline = require('readline');
const rl = readline.createInterface({ 
	input: process.stdin, // 입력값을 파이썬처럼 여러개 설정할 필요가 전혀 없다
	output: process.stdout 
}); 
let input = [];
rl.on('line', function (line) { 
	input.push(line.split('').map((el) => parseInt(el))) 
    
}) 
.on('close', function () {
    input[1].sort() // 입력이 다 되고 나서, close할 때 확인하자.
    let first = input[1][input[0][0]-1]
    let second = input[1][input[0][0]-2]
    let result = 0

    while (true){
        for (let i = 0; i<input[0][2]; i++){
            if(input[0][1] === 0) break;
            result += first
            input[0][1] --;
        }
        if(input[0][1] === 0) break;
        result += second
        input[0][1] --;
    }
	console.log(result); 
	process.exit();
}); 