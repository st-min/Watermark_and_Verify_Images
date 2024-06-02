# Digital watermarking technique using deep-learning models (CNN, HiDDeN) and digital signature


### CNN 신경망 모델 (Convolutional Neural Networks)

CNN(Convolutional Neural Networks)은 주로 이미지와 비디오 인식, 이미지 분류, 의료 이미지 분석 등에서 널리 사용되는 딥러닝 모델입니다. CNN은 컨볼루션 레이어를 통해 이미지의 공간적 계층 구조를 학습하며, 주요 구성 요소는 다음과 같습니다.

### 주요 구성 요소

1. **Convolutional Layer (컨볼루션 레이어)**

    컨볼루션 레이어는 입력 이미지에 커널(필터)을 적용하여 특성 맵(feature map)을 생성합니다. 커널은 작은 크기의 행렬로, 입력 이미지와 합성곱 연산을 수행합니다.
    - **수식**: \((I * K)(x, y) = \sum_{i=0}^{m-1} \sum_{j=0}^{n-1} I(x+i, y+j) \cdot K(i, j)\)
    - \(I\)는 입력 이미지, \(K\)는 커널, \(m\)과 \(n\)은 커널의 높이와 너비입니다.

2. **Pooling Layer (풀링 레이어)**

    풀링 레이어는 특성 맵의 크기를 줄여 계산 비용을 줄이고 과적합을 방지합니다. 주로 Max Pooling과 Average Pooling이 사용됩니다.
    - **수식 (Max Pooling)**: \( P(x, y) = \max_{0 \leq i < m, 0 \leq j < n} I(x + i, y + j) \)
    - 여기서 \(P\)는 풀링 결과, \(I\)는 입력, \(m\)과 \(n\)은 풀링 크기입니다.

3. **Fully Connected Layer (완전 연결 레이어)**

    완전 연결 레이어는 마지막 단계에서 모든 뉴런이 서로 연결되어 클래스에 대한 확률을 출력합니다.
    - **수식**: \( y = f(Wx + b) \)
    - 여기서 \(x\)는 입력 벡터, \(W\)는 가중치 행렬, \(b\)는 편향 벡터, \(f\)는 활성화 함수입니다.

4. **Activation Function (활성화 함수)**

    활성화 함수는 비선형성을 추가하여 신경망이 복잡한 패턴을 학습할 수 있게 합니다. 주로 ReLU(Rectified Linear Unit), Sigmoid, Tanh 등이 사용됩니다.
    - **ReLU 수식**: \( f(x) = \max(0, x) \)

### CNN 아키텍처 예시

- **LeNet-5** (LeCun et al., 1998)
  - 입력: 32x32 흑백 이미지
  - 구조:
    1. Conv Layer (6x5x5 필터, 스트라이드 1, 패딩 0)
    2. Avg Pooling Layer (2x2, 스트라이드 2)
    3. Conv Layer (16x5x5 필터, 스트라이드 1, 패딩 0)
    4. Avg Pooling Layer (2x2, 스트라이드 2)
    5. Fully Connected Layer (120 뉴런)
    6. Fully Connected Layer (84 뉴런)
    7. Output Layer (10 뉴런, softmax)

- **AlexNet** (Krizhevsky et al., 2012)
  - 입력: 227x227 RGB 이미지
  - 구조:
    1. Conv Layer (96x11x11 필터, 스트라이드 4, 패딩 0)
    2. Max Pooling Layer (3x3, 스트라이드 2)
    3. Conv Layer (256x5x5 필터, 스트라이드 1, 패딩 2)
    4. Max Pooling Layer (3x3, 스트라이드 2)
    5. Conv Layer (384x3x3 필터, 스트라이드 1, 패딩 1)
    6. Conv Layer (384x3x3 필터, 스트라이드 1, 패딩 1)
    7. Conv Layer (256x3x3 필터, 스트라이드 1, 패딩 1)
    8. Max Pooling Layer (3x3, 스트라이드 2)
    9. Fully Connected Layer (4096 뉴런)
    10. Fully Connected Layer (4096 뉴런)
    11. Output Layer (1000 뉴런, softmax)

### CNN의 시각화

#### 네트워크 구조 예시 (AlexNet)

```
Input: 227x227x3
|
|-> Conv (96x11x11, stride=4, padding=0) -> 55x55x96
|-> MaxPool (3x3, stride=2) -> 27x27x96
|-> Conv (256x5x5, stride=1, padding=2) -> 27x27x256
|-> MaxPool (3x3, stride=2) -> 13x13x256
|-> Conv (384x3x3, stride=1, padding=1) -> 13x13x384
|-> Conv (384x3x3, stride=1, padding=1) -> 13x13x384
|-> Conv (256x3x3, stride=1, padding=1) -> 13x13x256
|-> MaxPool (3x3, stride=2) -> 6x6x256
|-> FC (4096) -> FC (4096) -> Output (1000)
```

#### 컨볼루션 연산 예시

![Convolution Operation](https://cdn-images-1.medium.com/max/1200/1*sjB2OEZbLBxZBD1X8FmdZg.gif)

### CNN의 적용 사례

1. **이미지 분류**: 이미지 데이터를 입력받아 사물이나 인물 등을 분류하는 작업. (e.g., ImageNet)
2. **객체 탐지**: 이미지 내에서 객체의 위치를 탐지하고 분류하는 작업. (e.g., YOLO, Faster R-CNN)
3. **이미지 생성**: GAN(Generative Adversarial Networks)을 이용한 이미지 생성.
4. **의료 영상 분석**: 의료 이미지 데이터를 분석하여 질병 진단에 도움.

### 요약 표

| 레이어 유형    | 설명                                             | 예시                       |
|----------------|--------------------------------------------------|----------------------------|
| Convolutional  | 필터를 사용해 입력 이미지에서 특징 추출           | Conv(3x3, stride=1, padding=1) |
| Pooling        | 공간 크기 축소, 특징 강조                         | MaxPool(2x2, stride=2)     |
| Fully Connected| 뉴런 완전 연결, 분류 작업 수행                    | FC(4096)                   |
| Activation     | 비선형성 추가, 네트워크 표현력 증가                | ReLU, Sigmoid              |

CNN은 컴퓨터 비전에서 매우 중요한 도구로, 다양한 구조와 레이어 조합을 통해 복잡한 이미지 인식 문제를 해결합니다. 기본적인 컨셉과 주요 요소들을 이해하면, 다양한 응용 분야에서 효과적으로 활용할 수 있습니다.
