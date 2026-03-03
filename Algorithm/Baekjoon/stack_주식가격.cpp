/*
 * 문제: 프로그래머스 - 주식가격 (스택/큐)
 * 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42584
 * * [문제 설명]
 * 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
 * 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
 * * [제한사항]
 * - prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
 * - prices의 길이는 2 이상 100,000 이하입니다.
 */

#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer(prices.size());
    stack<int> stack;
    int num = prices.size();
    for(int i=0;i<num;i++){
        while(!stack.empty()&&prices[stack.top()]>prices[i]){
            answer[stack.top()] = i-stack.top();
            stack.pop();
        }
        stack.push(i);
    }
    while(!stack.empty()){
        answer[stack.top()] = num-stack.top()-1;
        stack.pop();
    }
    return answer;
}