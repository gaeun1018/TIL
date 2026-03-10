# Costa Rican Household Poverty Level Prediction

## 대회 개요
- **링크**: https://www.kaggle.com/c/costa-rican-household-poverty-prediction
- **목표**: 코스타리카 가구의 빈곤 수준 4단계 분류 (다중 분류)
- **평가 지표**: Macro F1 Score
- **데이터**: 가구별 사회경제적 지표 (주거 환경, 가족 구성, 교육 수준 등)

## 파일
- `notebook.ipynb`: EDA + 결측치 처리 + Feature Engineering

## 주요 접근
- 가구주(head of household) 기준으로 타겟 레이블 정합성 수정
- 결측치를 도메인 지식 기반으로 처리 (임대료, 교육 연도 등)
- 상관관계 기반 중복 feature 제거
- 전기/벽/지붕/바닥 상태를 ordinal 변수로 통합

## References
- [Will Koehrsen - A Complete Introduction and Walkthrough](https://www.kaggle.com/willkoehrsen/a-complete-introduction-and-walkthrough)
