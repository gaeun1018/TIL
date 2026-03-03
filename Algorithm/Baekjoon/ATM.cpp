/*
 * 문제: 백준 11399번 - ATM
 * 링크: https://www.acmicpc.net/problem/11399
 * * [문제 설명]
 * 인하은행에는 ATM이 1대밖에 없다. 지금 이 ATM앞에 N명의 사람들이 줄을 서있다. 
 * 사람은 1번부터 N번까지 번호가 매겨져 있으며, i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.
 * 사람들이 줄을 서는 순서에 따라서, 돈을 인출하는데 필요한 시간의 합이 달라지게 된다.
 * 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.
 * * [입력]
 * 첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다. 
 * 둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)
 * * [출력]
 * 첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.
 */


#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	int num;
	cin >> num;
	int* result=new int[num];
	for (int i = 0; i < num; i++) {
		int n;
		cin >> n;
		result[i] = n;
	}
	sort(result, result + num);

	int cnt = 0;

	for (int i = 0; i < num; i++) {
		cnt += result[i] * (num - i);
	}

	cout << cnt;
	delete[] result;
}