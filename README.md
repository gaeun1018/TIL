
# 📚 TIL (Today I Learned)

> 
> 이 레포지토리는 Computer Vision, Deep Learning에 대한 깊이 있는 학습과 실무 인턴십 경험, 그리고 탄탄한 기본기를 위한 알고리즘 문제 풀이를 기록한 공간입니다.

<br>

## 🛠️ Tech Stack
- **Language**: ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![C++](https://img.shields.io/badge/C++-%2300599C.svg?style=flat-square&logo=c%2B%2B&logoColor=white)
- **AI / Deep Learning**: ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=flat-square&logo=PyTorch&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=flat-square&logo=TensorFlow&logoColor=white)
- **Computer Vision**: ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)

<br>

## 📁 Repository Structure & Contents

이 레포지토리는 크게 **3가지 핵심 카테고리**로 구성되어 있습니다.

### 💼 [1. Work Experience](./work_Experience)
> 실무 환경에서 컴퓨터 비전 인턴으로 근무하며 마주한 문제들과 해결 과정을 기록했습니다.

- **Computer Vision Intern 업무 회고** ([📄 상세 보기](./work_Experience/Computer_Vision_Intern.md))
  - **데이터 파이프라인**: OpenCV를 활용한 이미지 전처리(Resize, Crop, Noise 제거) 및 Python 크롤링 자동화
  - **모델 최적화**: 기존 Face Recognition 모델의 입출력 구조 분석 및 하이퍼파라미터 설정 변경
  - **실험 및 성능 개선**: CNN 기반 이미지 인식 모델의 병목 구간 파악 및 Learning Rate, Batch Size 등 튜닝 실험 진행

### 🧠 [2. Deep Learning](./DeepLearning)
> 딥러닝의 수학적 기초부터 신경망 모델 구현까지의 이론을 정리하고, Google Colab을 통해 실습한 코드를 보관합니다.

- **딥러닝 기초 및 회귀 모델** ([📄 상세 보기](./Deep_Learning/DeapLearning_preliminary.md))
  - 선형 회귀(최소 제곱법, 평균 제곱 오차) 및 경사 하강법의 수학적 원리 학습
  - 로지스틱 회귀와 교차 엔트로피 오차 함수 이해
- **신경망과 퍼셉트론** ([📄 상세 보기](./Deep_Learning/DealLearning_perceptron.md))
  - 다층 퍼셉트론(MLP)을 통한 XOR 문제 해결 및 오차 역전파(Backpropagation) 구현
  - 기울기 소실 문제 파악 및 ReLU 함수, 확률적 경사 하강법(SGD), 모멘텀 개념 적용
- **모델 성능 검증 및 실습** ([📄 상세 보기](./Deep_Learning/DeapLearning_basic.md))
  - Pandas 기반 데이터 전처리 및 원-핫 인코딩
  - K겹 교차 검증(K-Fold Cross Validation)을 활용한 다중 분류 모델 성능 평가
  - 💻 **Colab 실습**: `선형회귀.ipynb`, `XOR.ipynb`, `multi_class.ipynb` 등 구현 완료

### 💻 [3. Algorithm](./Algorithm)
> 탄탄한 프로그래밍 기본기를 위해 자료구조/알고리즘 이론을 학습하고, 코딩 테스트 문제를 풀이합니다.

- **Theory (개념 정리)**
  - [그래프(Graph) 탐색: BFS, DFS 및 인접 행렬/리스트 구현](./Algorithm/Theory/그래프.md)
  - [이진 탐색(Binary Search): 개념 및 C++ 구현](./Algorithm/Theory/이진탐색.md)
- **Problem Solving (C++)**
  - **Baekjoon**: 스택(오큰수), 재귀(피보나치), 문자열 등 단계별 문제 풀이
  - **Programmers**: 정렬(가장 큰 수, K번째 수), 탐욕법(구명보트, 체육복), 해시 등 주요 알고리즘 풀이

<br>

