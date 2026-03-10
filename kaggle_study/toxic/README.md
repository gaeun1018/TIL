# Toxic Comment Classification Challenge

## 대회 개요
- **링크**: https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge
- **목표**: Wikipedia 댓글의 독성 유형 6가지를 다중 레이블 분류
- **평가 지표**: ROC AUC (각 레이블 평균)
- **클래스**: toxic / severe_toxic / obscene / threat / insult / identity_hate

## 파일
- `notebook.ipynb`: 텍스트 전처리 + LSTM 모델링 + 레이어 출력 확인

## 주요 접근
- Keras Tokenizer로 댓글 토큰화 및 색인화 (max_features=20,000)
- pad_sequences로 최대 길이 200으로 통일 (0 패딩)
- 문장 길이 분포 히스토그램으로 maxlen 근거 확인
- 모델 구조: Embedding(128) → LSTM(60) → GlobalMaxPool1D → Dropout → Dense(50) → Dense(6, sigmoid)
- Binary Cross-entropy loss로 다중 레이블 동시 학습
- K.function으로 중간 레이어 출력 확인

## References
- [sbongo - For Beginners: Tackling Toxic Using Keras](https://www.kaggle.com/sbongo/for-beginners-tackling-toxic-using-keras)
