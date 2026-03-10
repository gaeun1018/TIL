# Statoil/C-CORE Iceberg Classifier Challenge

## 대회 개요
- **링크**: https://www.kaggle.com/competitions/statoil-iceberg-classifier-challenge
- **목표**: 위성 레이더(SAR) 이미지에서 배(Ship)와 빙산(Iceberg) 이진 분류
- **평가 지표**: Log Loss
- **데이터**: 75×75 SAR 이미지 (Band-1, Band-2), 입사각(inc_angle), 총 1,604개

## 파일
- `notebook.ipynb`: 이미지 전처리 + Sequential CNN 모델링 + 제출

## 주요 접근

### 01_CNN_modeling
- Band-1, Band-2, (Band-1 + Band-2) / 2 평균을 합쳐 3채널 이미지로 구성
- Plotly 3D 시각화로 빙산/배 이미지 형태 탐색
- Sequential CNN 구조: Conv2D(64) → Conv2D(128) → Conv2D(128) → Dense
- ModelCheckpoint + EarlyStopping 콜백 적용


## References
- [cbryant - Keras CNN StatOil Iceberg LB 0.1516](https://www.kaggle.com/cbryant/keras-cnn-statoil-iceberg-lb-0-1995-now-0-1516)
