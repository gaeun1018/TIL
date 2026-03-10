# TensorFlow Speech Recognition Challenge

## 대회 개요
- **링크**: https://www.kaggle.com/c/tensorflow-speech-recognition-challenge
- **목표**: 1초짜리 음성 WAV 파일에서 발화된 단어를 12개 클래스로 분류
- **평가 지표**: Categorical Accuracy
- **클래스**: yes / no / up / down / left / right / on / off / stop / go / silence / unknown
- **데이터**: 65,000개의 1초 WAV 파일 (30개 단어, 수천 명의 화자)

## 파일
- `notebook.ipynb`: 음성 데이터 EDA — 스펙트로그램, FFT, MFCC, VAD, PCA 분석

## 주요 내용
- Log-Spectrogram 계산 및 시각화 (Hann window, STFT)
- MFCC 및 Mel-power 스펙트로그램 추출 (librosa)
- 3D Plotly로 스펙트로그램 시각화
- VAD(Voice Activity Detection) 적용으로 묵음 구간 제거
- 8kHz 리샘플링 + FFT 비교 분석
- 단어별 평균 FFT 비교 및 Violin plot
- PCA로 이상치 탐지

## References
- [davids1992 - Speech Representation and Data Exploration](https://www.kaggle.com/davids1992/speech-representation-and-data-exploration)
