# TIL


![image](img.png)

### 오늘의 학습 키워드

    문자열

### 해결 문제
<hr/>


### Minimum Suffix Flips

[문제 링크][link]

[link]: https://leetcode.com/problems/minimum-suffix-flips/description/

<br/>

**문제 설명**   

You are given a **0-indexed** binary string `target` of length `n`. You have another binary string `s` of length `n` that is initially set to all zeros. You want to make `s` equal to `target`.

In one operation, you can pick an index `i` where `0 <= i < n` and flip all bits in the inclusive range `[i, n - 1]`. Flip means changing `'0'` to `'1'` and `'1'` to `'0'`.

Return the minimum number of operations needed to make `s` equal to `target`.

<br/>

**제한사항**

- n == target.length
- 1 <= n <= 105
- target[i] is either '0' or '1'.

<br/>

**입출력 예**

Input: target = "10111"   
Output: 3  
```
Explanation: Initially, s = "00000".   
Choose index i = 2: "00000" -> "00111"   
Choose index i = 0: "00111" -> "11000"   
Choose index i = 1: "11000" -> "10111"   
We need at least 3 flip operations to form target.   
```

<br/>

**해결 과정**

처음 접근 방식은 문자열을 뒤집는 flip 함수를 구현 후 target 문자열과 s 문자열의 원소가 다를 때마다 문자열을 뒤집는 방식으로 코드를 작성하였다.

```python
class Solution:
    def minFlips(self, target: str) -> int:
        basic = "0" * len(target)
        answer = 0
        def flip(str,num):
            result = str[:num]
            for i in range(num,len(str)):
                if str[i]=="0":
                    result+="1"
                else:
                    result+="0"
            return result
        for i in range(len(target)):
            if target == basic:
                return answer
            if target[i]!=basic[i]:
                basic = flip(basic,i)
                answer +=1
        return answer
```

정답은 맞았지만 time limit 에 걸리는 예제가 있어 코드를 수정하게 되었다.

이전 인덱스의 원소와 현재 인덱스의 원소가 다를 땐 filp을 한다는 가정 하에 정답 횟수를 추가하면 문자열을 한 번만 돌아도 되므로 시간 복잡도가 줄게 된다.

```python
class Solution:
    def minFlips(self, target: str) -> int:
        basic = "0" * len(target)
        answer = 0
        current = "0"
        for i in target:
            if i != current:
                answer +=1
                current = i
        return answer
```

다음과 같이 구현하니 코드도 훨씬 간단해졌다.

#99클럽  #코딩테스트 준비  #개발자 취업  #항해99  #TIL