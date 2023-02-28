# TODO list

### 1. Face Domain Adaptation
- [x] RMFD 데이터셋 확인
- [x] MFR2 데이터셋 확인

### 2. Face Recognition
- [x] AI-HUB 데이터셋 v2 (Face Emotion) 112x112로 인증이미지로 변환
- [x] 데이터바우처 데이터셋 112x112로 인증이미지로 변환
* 3장 이상인 경우에 얼굴인증 데이터셋으로 사용
- [x] 크롤링 데이터셋 112x112로 인증이미지로 변환
- [ ] **`AI-HUB 데이터셋 v1 (Face in the wild) 112x112로 인증이미지로 변환`**
* 민선씨에 Face Recognition으로 사용에 관련하여 문의
- [ ] **`AI-HUB 데이터셋 v3 (Masked Korean Face) 112x112로 인증이미지로 변환`**
* 민선씨가 해당 데이터가 있는 도커환경 공유 예정
* a. REI/REO, SPI/SPO, STD의 ID와 CRS의 ID 그룹으로 나누어지며, 마스크 미착용 데이터군에서 데이터를 선택한다.
* b. REI/REO, SPI/SPO, STD의 ID는 900개이며, CRS의 ID는 2698개이다.
* c. REI/REO, SPI/SPO, STD의 데이터군은 각 ID당 128장이며, CRS의 데이터는 각 ID당 18장이다.
* d. 총 ID는 3598개이며, 총 이미지의 개수는 163764개 이다.


#### 3. 이미지셋  MxNet 데이터셋 포맷으로 변환
- [x] AI-HUB, 데이터바우처, 크롤링의 데이터셋만으로 rec 파일로 변환
- [x] MS1MV3 rec 파일에 AI-HUB, 데이터바우처, 크롤링 이미지셋 추가

  ```/shared/Face/FaceRecognition/datasets/train/ms1m-retinaface-t1-plus 에 complete_ms1m 파일 존재```

- [x] glint360k rec 파일에 AI-HUB, 데이터바우처, 크롤링 이미지셋 추가

  ```/shared/Face/FaceRecognition/datasets/train/glint360k-plus 에 complete_glint 파일 존재```
  
- [x] MS1MV3-mask rec 파일에 AI-HUB, 데이터바우처, 크롤링 이미지셋 추가 (마스크 정보 포함)


  ```/shared/Face/FaceRecognition/datasets/train/glint360k-plus 에 complete_glint_m 파일 존재```

- [x] glint360k-mask rec 파일에 AI-HUB, 데이터바우처, 크롤링 이미지셋 추가 (마스크 정보 포함)


  ```/shared/Face/FaceRecognition/datasets/train/ms1m-retinaface-t1-plus 에 complete_ms1m_m 파일 존재```

- [insightface/rec_builder.py at master · deepinsight/insightface · GitHub](https://github.com/deepinsight/insightface/blob/master/python-package/insightface/data/rec_builder.py)
- [insightface/tutorial_pytorch_mask_aug.md at master · deepinsight/insightface · GitHub](https://github.com/deepinsight/insightface/blob/master/challenges/iccv21-mfr/tutorial_pytorch_mask_aug.md)
-  [Create a Dataset Using RecordIO | Apache MXNet](https://mxnet.apache.org/versions/1.9.1/api/faq/recordio.html)


### 4. Face Attribute (Age/Gender)
- [x] VGGFace2 데이터셋 확인
* 나이/성별의 데이터가 존재하는지 확인
* 나이가 0~100 혹은 10/20/30/40... 된 데이터셋인지 확인.
* 모든 데이터는 csv로 파일명/나이/성별(M,F)로 저장.

  ```
  나이/성별 데이터 존재. 나이 0~100으로 구성.
  
  ~NAS/insta/DATA/VGGface2 에 vgg_csv.csv 파일 존재
  ```

- [x] imdb-wiki 데이터셋 확인
* [https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/)
* imdb-wiki라는 데이터셋인데 나이 계산하는 부분이 있음 (ex. [age,~] = datevec(…), 링크에서 확인가능)
* 위에서 계산한 나이랑 공유된 csv의 나이가 일치하는지 확인. (슬랙에서 imdb_dlib_aligned.csv 검색하면 확인가능)
* imdb-wiki의 데이터셋은 아래의 경로에 다운로드 되어 있음.
```
/data/notebook/NAS/Gender-Age/NOT_YET_USED/imdb/
```
```
계산한 나이과 csv의 나이 일치
```
