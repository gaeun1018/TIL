/*
 * 문제: 백준 4673번 - 셀프 넘버
 * 링크: https://www.acmicpc.net/problem/4673
 * * [문제 설명]
 * 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자. 
 * 예를 들어, d(75) = 75+7+5 = 87이다.
 * n을 d(n)의 생성자라고 한다. 위의 수열에서 33은 39의 생성자이고, 39는 51의 생성자, 51은 57의 생성자이다. 
 * 생성자가 없는 숫자를 셀프 넘버라고 한다. 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
 * * [입력]
 * 입력은 없다.
 * * [출력]
 * 10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.
 */

#include<iostream>
#include<string>
#include<vector>

using namespace std;

int main() {
	vector<bool> result(20000, true);
	for (int i = 1; i < 10000; i++) {
		int num = i;
        string nums = to_string(i);
		for (int n=0; n < nums.size(); n++) {
			num += nums[n] - '0';
		}
		result[num] = false;
    }
	for (int i = 1; i < 10000; i++) {
		if (result[i] == true)
			cout <<i<<endl;
	}
}