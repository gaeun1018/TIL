/*
 * 문제: 백준 10870번 - 피보나치 수 5 (재귀)
 * 링크: https://www.acmicpc.net/problem/10870
 * * [문제 설명]
 * 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 
 * 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
 * n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
 * * [입력]
 * 첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.
 * * [출력]
 * 첫째 줄에 n번째 피보나치 수를 출력한다.
 */

#include <iostream>

using namespace std;
int fibo(int num){
 if(num==0){
  return 0;
 }
 if(num==1){
  return 1;
 }
 return fibo(num-1)+fibo(num-2);
}
int main(){
 int num;
 cin>>num;
 cout<<fibo(num);
}