# Porto Seguro's Safe Driver Prediction

## 대회 개요
- **링크**: https://www.kaggle.com/c/porto-seguro-safe-driver-prediction
- **목표**: 내년에 자동차 보험 청구를 할 운전자 예측 (이진 분류)
- **평가 지표**: Normalized Gini Coefficient
- **데이터**: 약 60만 건, 57개 feature (익명화)

## 파일
- `notebook.ipynb`: EDA + Feature Engineering + LightGBM/XGBoost 스태킹 앙상블

## 주요 접근
- 메타데이터 기반 feature 분류 (binary / categorical / real)
- 결측값(-1) 처리 및 Target Encoding (`ps_car_11_cat`)
- Under-sampling으로 클래스 불균형 조정 (양성 클래스 약 3.6%)
- LightGBM 3종 + XGBoost를 Logistic Regression으로 스태킹

## References
- [Bert Carremans - Data Preparation & Exploration](https://www.kaggle.com/bertcarremans/data-preparation-exploration)
- [ogrellier - XGB Classifier Upsampling](https://www.kaggle.com/ogrellier/xgb-classifier-upsampling-lb-0-283)
