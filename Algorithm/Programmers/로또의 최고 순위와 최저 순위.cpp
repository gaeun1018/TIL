/*
 * 문제: 프로그래머스 - 로또의 최고 순위와 최저 순위
 * 링크: https://school.programmers.co.kr/learn/courses/30/lessons/77484
 * * [문제 설명]
 * 로또 6/45(이하 '로또'로 표기)는 1부터 45까지의 숫자 중 6개를 찍어서 맞히는 대표적인 복권입니다.
 * 민우의 동생이 로또에 낙서를 하여, 일부 번호를 알아볼 수 없게 되었습니다. 
 * 알아볼 수 없는 번호를 0으로 표기하기로 하고, 민우가 구매한 로또 번호와 당첨 번호가 주어졌을 때, 
 * 당첨이 가능했던 최고 순위와 최저 순위를 알아보고 싶어 졌습니다.
 * 순위는 6개 일치(1등)부터 2개 일치(5등)까지이며, 그 외는 낙첨(6등)입니다.
 * * [제한사항]
 * - lottos는 길이 6인 정수 배열입니다. (0 이상 45 이하, 0은 지워진 숫자)
 * - win_nums은 길이 6인 정수 배열입니다. (1 이상 45 이하)
 */
 

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    int a = 0;
    int zero = 0;
    for (int i = 0; i < 6; i++) {
        if (lottos[i] == 0) {
            zero++;
            continue;
        }
        for (int j = 0; j < 6; j++) {
            if (lottos[i] == win_nums[j]) {
                a++;
                break;
            }
        }
    }
    if (a + zero == 0) //������ ���� ��÷�� ���
        answer.push_back(6);
    else
        answer.push_back(7 - a - zero);

    if (a == 0)
        answer.push_back(6);
    else
        answer.push_back(7 - a);
    return answer;
}