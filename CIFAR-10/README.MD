# CIFAR-10 Image Classifier

## 📌 프로젝트 소개
본 프로젝트는 **CIFAR-10 이미지 분류 문제**를 대상으로  
CNN(Convolutional Neural Network) 기반 모델을 구현하고,  
**학습 전략 및 구조적 개선을 통해 성능 향상을 실험**한 프로젝트입니다.

Baseline CNN 모델을 시작으로  
- Batch Normalization
- Optimizer 변경 (Adam → SGD)
- Learning Rate Scheduler

등을 단계적으로 적용하며 각 기법이 **모델 성능에 미치는 영향**을 비교·분석하였습니다.

---

## 🧾 사용한 기술
- **PyTorch**
- **CNN (Convolutional Neural Network)**
- **Data Augmentation**
  - RandomCrop
  - RandomHorizontalFlip
- **Batch Normalization**
- **Optimizer**
  - Adam
  - SGD (Momentum, Weight Decay)
- **Learning Rate Scheduler**
  - MultiStepLR

---

## 📊 실험 결과

| Model Configuration | Test Accuracy |
|---------------------|---------------|
| Baseline CNN (Adam) | 79.75%        |
| + Batch Normalization | 81.77%      |
| + SGD + LR Scheduler | **84.49%**   |

> Batch Normalization과 Learning Rate Scheduler를 적용함으로써  
> 모델의 일반화 성능이 점진적으로 향상됨을 확인하였습니다.

---

## 📎 코드 구성

```bash
src/
 ├── model.py    # CNN 아키텍처 정의 (BatchNorm 옵션 포함)
 ├── train.py    # 학습 루프, Optimizer 및 Scheduler 설정
 └── eval.py     # 저장된 모델 평가 (Inference 전용)
```

- **`model.py`**
  - CNN 아키텍처 정의
  - Batch Normalization 옵션 포함
- **`train.py`**
  - 데이터 로딩 및 전처리
  - Optimizer 및 Learning Rate Scheduler 설정
  - 학습 및 checkpoint 저장
- **`eval.py`**
  - 저장된 모델 로드
  - Test set 정확도 평가

---

## ▶️실행 방법

### 셋업

```bash
pip install -r requirements.txt
```

### 학습

**Baseline (Adam, BN 없음):**

```bash
python src/train.py --epochs 50 --optimizer adam --scheduler none
```

**성능 향상 설정 (SGD + BatchNorm + MultiStepLR):**

```bash
python src/train.py --epochs 120 --optimizer sgd --scheduler multistep --use_bn
```

학습된 모델은 기본적으로 아래 경로에 저장됩니다.
```
./checkpoints/best.pt
```

### 평가

```bash
python src/eval.py --ckpt ./checkpoints/best.pt --use_bn
```
---
## 📌 실험 정리 및 한계
본 프로젝트의 목적은 **CNN 기본 구조와 학습 전략에 대한 이해**에 있으며,  
사전 학습된 모델(ResNet 등)을 활용한 성능 극대화보다는  
각 기법의 효과를 직접 실험하고 비교하는 데 중점을 두었습니다.

향후 확장 가능성으로는 다음을 고려할 수 있습니다.
- Pretrained CNN 모델 기반 fine-tuning
- Advanced augmentation 기법 (Mixup, CutMix)
- Confusion Matrix 및 학습 곡선 시각화 추가

---

## 📌 결과 시각화
![Confusion Matrix](images/confusion_matrix.png)

![Loss & Accuracy Curve](images/loss_accuracy_curve.png)


---

## Notes

- Batch Normalization은 **모델 구조의 일부**로 `model.py`에 정의됨

- Learning Rate Scheduler는 **학습 루프의 일부**로 `train.py`에서만 사용됨

- `eval.py`는 **순수 추론(Inference) 전용 코드**임