# 딥러닝

![image](https://thebook.io/img/080324/018.jpg)

딥러닝은 인간의 두뇌에서 영감을 얻은 방식으로 데이터를 처리하도록 컴퓨터를 가르치는 인공 지능 방식이다.


## 딥러닝의 계산 원리
- 선형 회귀(linear regression)
- 로지스틱 회귀

<br>

### 선형 회귀

*선형 회귀란 독립 변수 x를 사용해 종속 변수 y의 움직임을 예측하고 설명하는 작업이다.*   

독립적으로 변할 수 있는 값 `x`를 `독립 변수`라고 한다. 또한, 이 독립 변수에 따라 종속적으로 변하는 `y`를 `종속 변수`라고 한다.    
하나의 x 값만으로도 y 값을 설명할 수 있다면 `단순 선형 회귀(simple linear regression)`라고 한다. 또한, x 값이 여러 개 필요하다면 `다중 선형 회귀(multiple linear regression)`라고 한다.

선형회귀는 점들의 특징을 가장 잘 나타내는 선을 그리는 과정이다.   
<br>

    y = ax+b


위의 식에서 *x*는 독립 변수이고 *y*는 종속 변수이다.  
정확하게 계산하려면 기울기 *a*와 *y* 절편 *b*의 값을 예측해야한다.

<br>

**최소 제곱법**

$$ a = \frac{(x-x 평균)(y-y평균)의  \ 합}{(x-x평균)^2의\ 합}$$
<br>

$$b = y의\ 평균 - (x의\ 평균 * 기울기 a)$$
<br>

최소 제곱법을 이용하면 *a*와 *b*의 값을 구할 수 있다.

<br>

**코드로 구현하기**

[Colab_LSM][colablink]

[colablink]: colab\LSM.ipynb

<br>


**평균 제곱 오차(Mean Square Error, MSE)**

오차(error)를 제곱한 값의 평균으로 이 값이 작을수록 훌륭한 알고리즘이다.

평균 제곱 오차(MSE) $$ \frac{1}{n}  \sum (y_i-\hat{y} _i)^2$$


<br>

**선형 회귀**란 임의의 직선을 그어 이에 대한 평균 제곱 오차를 구하고, 이 값을 가장 작게 만들어 주는 a 값과 b 값을 찾아가는 작업이다.

<br>

**코드로 구현하기**

[Colab_MSE][colablink]

[colablink]: colab\MSE.ipynb


<br>

#### 경사 하강법

오차의 변화에 따라 **이차 함수 그래프**를 만들고 적절한 **학습률**을 설정해 **미분 값이 0**인 지점을 구하는 것이다.

<br>

$$ \frac{1}{n}  \sum (y_i - (ax_i+b))^2$$
<br>

$$ a로\ 편미분 = \frac{2}{n} \sum-x_i(y_i - (ax_i+b))$$
$$ b로\ 편미분 = \frac{2}{n} \sum-(y_i - (ax_i+b))$$

<br>

**코드로 구현하기**

[Colab_선형회귀][colablink]

[colablink]: colab\선형회귀.ipynb

<br>

### 다중 선형 회귀

<br>

**코드로 구현하기**

[Colab_다중선형회귀][colablink]

[colablink]: colab\다중선형회귀.ipynb


<br>


### 머신 러닝
머신러닝에서 가설 함수(hypothesis)는 H(x)라고 표기한다.  
기울기는 가중치(weight)라고 하며, w로 표시하고 절편은 편향(bias)이라고 하며, b로 표시한다.  

    H(x) = wx + b

*평균 제곱 오차* -> **손실 함수**  
*경사 하강법* -> **옵티마이저**

<br>

**코드로 구현하기**

[Colab_다중선형회귀_tensorflow][colablink]

[colablink]: colab\다중선형회귀_텐서플로.ipynb

<br>

### 로지스틱 회귀
종속변수가 두 개의 클래스를 갖는 범주형일 때 분류기법으로 사용


**시그모이드 함수**
$$ y = \frac{1}{1+e^{-(ax+b)}}$$
<br>

![image](https://thebook.io/img/080324/102_2.jpg)
![image](https://thebook.io/img/080324/103.jpg)


**교차 엔트로피 오차 함수**
$$ -{ylogh + (1-y)log(1-h)} $$

실제 값을 *y*라고 할 때 이 값이 1 이면 뒷부분이 없어지고 반대로 0 이면 앞부분이 없어진다.