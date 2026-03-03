# 딥러닝

## 딥러닝 모델

[모델 실행 예제](colab/Deap_model.ipynb) 

<br>

데이터를 다루기 위해 numpy기능을 포함하며 다양한 포맷의 데이터를 다룰 수 있는 **pandas** 라이브러리를 사용한다.

[Pandas 라이브러리 실행 예제](colab/pandas.ipynb)

## 다중 분류 문제

**다중 분류**(multi classification)란 여러 개의 답 중 하나를 고르는 분류 문제이다.

**원-핫 인코딩**(one-hot encoding)이란 여러 개의 값으로 된 문자열을 0과 1로만 이루어진 형태로 만들어 주는 과정이이다.
<br>

코드로 구현하기   
[Colab_Multi](colab/multi_class.ipynb)

## 모델 성능 검증

**K겹 교차 검증**이란 데이터셋을 여러 개로 나누어 하나씩 테스트셋으로 사용하고 나머지를 모두 합해서 학습셋으로 사용하는 방법이다.

코드로 구현하기   
[Colab Verification](colab/model_verifi.ipynb)   



## 모델 성능 향상

최적의 학습 파라미터를 찾기 위해 학습 과정에서 사용하는 것이 **검증셋**이다.   
검증셋을 설정하면 검증셋에 테스트한 결과를 추적하면서 최적의 모델을 만들 수 있다.