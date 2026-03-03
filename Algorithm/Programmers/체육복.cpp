/*
 * 문제: 프로그래머스 - 체육복 (탐욕법/Greedy)
 * 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42862
 * * [문제 설명]
 * 점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 
 * 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 
 * 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 
 * 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
 * * [제한사항]
 * - 전체 학생의 수는 2명 이상 30명 이하입니다.
 * - 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
 * - 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
 * - 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
 * - 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다.
 */


#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    answer = n - lost.size();
    sort(lost.begin(), lost.end());
    sort(reserve.begin(), reserve.end());
    bool* res = new bool[reserve.size()];
    for (int i = 0; i < reserve.size(); i++) {
        res[i] = true;
    }
    bool* los = new bool[lost.size()];
    for (int i = 0; i < lost.size(); i++) {
        los[i] = true;
    }
    for (int i = 0; i < lost.size(); i++) {
        for (int j = 0; j < reserve.size(); j++) {
            if (lost[i] == reserve[j]) {
                los[i] = false;
                res[j] = false;
                answer++;
                break;
            }
        }
    }
    for (int i = 0; i < lost.size(); i++) {
        for (int j = 0; j < reserve.size(); j++) {
            if (abs(lost[i] - reserve[j]) == 1) {
                if (res[j] == true and los[i] == true) {
                    res[j] = false;
                    answer++;
                    break;
                }
            }
        }
    }
    delete res;
    delete los;
    return answer;
}