function solution(answers) {
    var answer = [];
    var person1 = [1, 2, 3, 4, 5];
    var person2 = [2, 1, 2, 3, 2, 4, 2, 5];
    var person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    var scores = [0, 0, 0];  // 각 수포자의 점수를 저장하는 배열

    for (var i = 0; i < answers.length; i++) {
        if (answers[i] === person1[i % person1.length]) {
            scores[0]++;
        }
        if (answers[i] === person2[i % person2.length]) {
            scores[1]++;
        }
        if (answers[i] === person3[i % person3.length]) {
            scores[2]++;
        }
    }

    var maxScore = Math.max(scores[0], scores[1], scores[2]);  // 가장 높은 점수

    for (var j = 0; j < scores.length; j++) {
        if (scores[j] === maxScore) {
            answer.push(j + 1);  // 가장 높은 점수를 받은 수포자 번호를 answer 배열에 추가
        }
    }

    return answer;
}