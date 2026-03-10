# Home Credit Default Risk

## 대회 개요
- **링크**: https://www.kaggle.com/c/home-credit-default-risk
- **목표**: 대출 신청자의 상환 능력 예측 (이진 분류)
- **평가 지표**: ROC AUC
- **데이터**: 대출 신청 정보 + 외부 신용 기록, 이전 대출 이력 등 다수의 테이블

## 파일
- `01_EDA_baseline.ipynb`: EDA + 결측치/이상치 처리 + 베이스라인 모델
- `02_feature_engineering.ipynb`: 외부 데이터 집계 + Feature Engineering + LightGBM

## 주요 접근

### 01_EDA_baseline
- 결측치 비율 테이블 생성
- `DAYS_EMPLOYED` 이상치 탐지 및 처리 (365243일 → NaN)
- EXT_SOURCE 변수 분석 (target과 가장 높은 상관관계)
- Polynomial features 생성 (EXT_SOURCE × DAYS_BIRTH 조합)
- 도메인 지식 기반 파생 변수 생성 (`CREDIT_INCOME_PERCENT`, `ANNUITY_INCOME_PERCENT` 등)
- Logistic Regression / Random Forest 베이스라인 제출

### 02_feature_engineering
- `bureau.csv`, `bureau_balance.csv` 외부 데이터 집계 (count, mean, max, min, sum)
- 범주형 변수 one-hot encoding 후 고객 단위로 집계
- 상관계수 0.8 이상 중복 feature 제거
- LightGBM 5-Fold CV로 최종 모델 학습 및 제출

## References
- [Will Koehrsen - Start Here: A Gentle Introduction](https://www.kaggle.com/willkoehrsen/start-here-a-gentle-introduction)
- [Will Koehrsen - Introduction to Manual Feature Engineering](https://www.kaggle.com/willkoehrsen/introduction-to-manual-feature-engineering)
