/*
 * 문제: 프로그래머스 - 더 맵게 (힙)
 * 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42626
 * * [문제 설명]
 * 매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 
 * 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 
 * 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.
 * 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
 * Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
 * Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 
 * 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.
 * * [제한사항]
 * - scoville의 길이는 2 이상 1,000,000 이하입니다.
 * - K는 0 이상 1,000,000,000 이하입니다.
 * - scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
 * - 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
 */
 

#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

const int HEAP_SIZE = 1000000;

int heap[HEAP_SIZE];
int heap_count = 0;

void swap(int* a, int* b) {
	int tmp = *a; *a = *b; *b = tmp;
}

int first() {
	return heap[1];
}

int size() {
	return heap_count;
}

void push(int data) {
	// ���� ���� ������ �߰�
	heap[++heap_count] = data;

	//  child�� parent�� ���ϸ鼭 �ϳ��� ���� �ø��� �κ�
	int child = heap_count;
	int parent = child / 2;
	while (child > 1 && heap[parent] > heap[child]) {
		swap(&heap[parent], &heap[child]);
		child = parent;
		parent = child / 2;
	}
}

int pop() {
	// ���� ù��° ���Ҹ� ��ȯ
	int result = heap[1];

	// ù��° ���Ҹ� ���� ���� �� ���ҿ� �ٲٰ�
	// ���� ���� ���� ���� ���� �����̴� heap_count�� �����ش�.
	swap(&heap[1], &heap[heap_count--]);

	// child�� parent�� ���ϸ鼭 �˸��� ��ġ�� �ϳ��� ������ �κ�
	int parent = 1;
	int child = parent * 2;
	if (child + 1 <= heap_count) {
		child = (heap[child] < heap[child + 1]) ? child : child + 1;
	}

	while (child <= heap_count && heap[parent] > heap[child]) {
		swap(&heap[parent], &heap[child]);

		parent = child;
		child = child * 2;
		if (child + 1 <= heap_count) {
			child = (heap[child] < heap[child + 1]) ? child : child + 1;
		}
	}

	return result;
}

int solution(vector<int> scoville, int K) {
	int answer = 0;
	for (int i = 0; i < scoville.size(); i++) {
		push(scoville[i]);
	}
	if ((heap[0] == 0 and heap[1] == 0))
		return -1;
	while (first() < K) {
		if (size() == 1)
			return -1;
		push(pop() + pop() * 2);
		answer++;
	}
	return answer;
}