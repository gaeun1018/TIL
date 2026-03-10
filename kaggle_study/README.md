# Kaggle Study

캐글 대회를 공부하며 참고한 커널을 분석하고 따라 구현한 코드 모음입니다.

각 노트북은 공개된 커널을 참고하여 작성하였으며, 코드를 직접 실행하고 주석을 달며 학습했습니다.
참고한 원본 커널은 각 폴더의 README에 명시되어 있습니다.

---

## 대회 목록

| 분야 | 대회명 | 주요 기법 |
|------|--------|-----------|
| Tabular | [Porto Seguro's Safe Driver Prediction](#porto-seguro) | EDA, Feature Engineering, LightGBM/XGBoost 앙상블 |
| Tabular | [Costa Rican Household Poverty Level Prediction](#costa-rica) | EDA, 결측치 처리, Feature Engineering |
| Tabular | [Home Credit Default Risk](#home-credit) | Feature Engineering, 외부 데이터 집계, LightGBM |
| CV | [Statoil/C-CORE Iceberg Classifier Challenge](#iceberg) | SAR 이미지 처리, CNN |
| Audio | [TensorFlow Speech Recognition Challenge](#speech) | Log-Spectrogram, FFT, MFCC, VAD |
| NLP | [Toxic Comment Classification Challenge](#toxic) | 토큰화, 패딩, Bi-LSTM |

---

## 상세

### Porto Seguro's Safe Driver Prediction <a name="porto-seguro"></a>
- 자동차 보험 청구 여부 예측 (이진 분류)
- LightGBM 3종 + XGBoost 스태킹 앙상블, Target Encoding, Under-sampling

### Costa Rican Household Poverty Level Prediction <a name="costa-rica"></a>
- 가구별 빈곤 수준 4단계 분류
- 도메인 지식 기반 결측치 처리, 가구주 기준 타겟 정합성 수정

### Home Credit Default Risk <a name="home-credit"></a>
- 대출 상환 능력 예측 (이진 분류)
- bureau/bureau_balance 외부 데이터 집계, Polynomial features, LightGBM CV

### Statoil/C-CORE Iceberg Classifier Challenge <a name="iceberg"></a>
- SAR 위성 이미지에서 배 vs 빙산 분류 (이진 분류)
- Band-1/2로 3채널 이미지 구성, Sequential CNN

### TensorFlow Speech Recognition Challenge <a name="speech"></a>
- 1초 음성 파일에서 단어 분류 (12개 클래스)
- Log-Spectrogram, MFCC, FFT, VAD, PCA 분석

### Toxic Comment Classification Challenge <a name="toxic"></a>
- Wikipedia 댓글 독성 유형 분류 (다중 레이블)
- 토큰화/패딩, LSTM → GlobalMaxPool → Dense
