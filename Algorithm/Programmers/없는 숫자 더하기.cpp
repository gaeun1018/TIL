/*
 * 문제: 프로그래머스 - 없는 숫자 더하기
 * 링크: https://school.programmers.co.kr/learn/courses/30/lessons/86051
 * * [문제 설명]
 * 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. 
 * numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.
 * * [제한사항]
 * - 1 <= numbers의 길이 <= 9
 * - 0 <= numbers의 모든 원소 <= 9
 * - numbers의 모든 원소는 서로 다릅니다.
 */


#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> numbers) {
    int answer = 0;
    for (int i = 1; i < 10; i++) {
        if (find(numbers.begin(), numbers.end(), i) == numbers.end()) {
            answer += i;
            cout << i;
        }

    }
    return answer;
}