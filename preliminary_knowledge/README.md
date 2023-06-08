# Laplacian의 정의와 의의

<b>정의</b>: 수학에서 라플라스 연산자 또는 라플라시안은 2차 미분 연산자의 일종으로 기울기의 발산을 의미하며 기호로는 $\Delta$ 또는 $\bigtriangledown^2$ 으로 나타낸다.
참고: https://ko.wikipedia.org/wiki/%EB%9D%BC%ED%94%8C%EB%9D%BC%EC%8A%A4_%EC%97%B0%EC%82%B0%EC%9E%90

즉, 유클리드 공간의 2차 연속 미분이 가능한 스칼라 함수 $f$ 에 대한 라플라시안은 함수 $f$ 에 대한 기울기의 발산으로, 기울기(gradient) 연산을 먼저 취한 후, 그것으로부터 출력되는 벡터장에 대해 divergence를 구하는 것이며, 아래와 같이 표현할 수 있다.

$$\Delta f = \bigtriangledown^2 f = \bigtriangledown \cdot \bigtriangledown f = div(grad(f)) = \dfrac{\delta^2 f}{\delta x^2} + \dfrac{\delta^2 f}{\delta y^2} + \dfrac{\delta^2 f}{\delta z^2}$$

<b>라플라시안(기울기의 발산)</b>: 스칼라 함수에 대해 기울기 연산(gradient 즉, 편미분)을 구한 뒤에 발산(내적)을 구해서 스칼라 값을 계산한 것.

<b>발산(divergence)</b>: 벡터장에서 작동하는 벡터 연산자로서 벡터의 내적 연산을 하므로 결과값으로 스칼라 값을 얻게 된다. 벡터장이란 액체 또는 기체의 흐름을 나타내는 것으로 생각될 수 있으며, 여기서 벡터장의 각 벡터는 움직이는 유체의 속도 벡터를 나타냄.

> Roughly speaking, divergence measures the tendency of the fluid to collect or disperse at a point, and curl measures the tendency of the fluid to swirl around the point.  - Page 433, [Single and Multivariable Calculus, 2020](https://www.whitman.edu/mathematics/multivariable/multivariable.pdf)

[<b>스칼라 함수의 라플라시안(기울기와 발산)</b>](https://angeloyeo.github.io/2019/08/28/laplacian.html)
 
 <p align="center">
  <img src="https://github.com/iispace/Graph/assets/24539773/22afc3b6-f7f8-4272-b383-5b14d54b33ad" width="400" height="280">
  
  <div align="center">그림 1 스칼라 함수 예시(MATLAB의 peak 함수)</div>
  <div align="center">참고:https://www.mathworks.com/help/matlab/visualize/changing-surface-properties.html</div>
</p>

<br>

 이 함수에 대한 기울기(gradient)를 구하면 가파르게 변하는 방향으로 [그림 2]의 $x, y$ 평면 위에 파란색 화살표 모양으로 표시된 바와 같은 벡터장이 생성된다.

 <p align="center">
  <img src="https://github.com/iispace/Graph/assets/24539773/68a4add8-3c5c-4e71-9fa6-4e576a126107" width=600" height="480">
  
  <div align="center">그림 2 스칼라 함수와 gradient 표시</div>
  <div align="center">참고:https://angeloyeo.github.io/2019/08/28/laplacian.html</div>
</p>
<br>
                     
주어진 스칼라 함수 $f$ 에 대한 기울기인 벡터장에 대하여 발산(divergence)를 구하면 어떤 값이 나올까?
                     
$(0,2)$ 근처에서는 벡터장이 한 점으로 수렴하는 형태이기 때문에 발산(divergence) 값은 음의 값이 되고, $(0, -2)$ 근처에서는 벡터장이 한 점으로부터 바깥으로 발산하는 형태이므로 divergence의 값이 양의 값이 된다.
                     
정리하자면, <b>라플라시안의 의의</b>는 어떤 스칼라 함수 $f$ 에 대하여 기울기(gradient) 연산을 취한 후에, 그것에 대한 발산(divergence)를 구하면 이 스칼라 함수의 높이 값이 얼마나 낮은 지를 수치로 볼 수 있게 된다는 것이다.

 <p align="center">
  <img src="https://github.com/iispace/Graph/assets/24539773/1922dc2f-12a7-4c67-b65a-57a3d1f197fe" width=600" height="480">
  
  <div align="center">그림 3 스칼라 함수에 대한 Laplacian(기울기의 발산)</div>
  <div align="center">참고:https://angeloyeo.github.io/2019/08/28/laplacian.html</div>
</p>
<br>

<hr>

## 라플라시안 공식

어떤 스칼라 함수 $F(x, y, z)$ 의 기울기 벡터(벡터장) $\overrightarrow F$ 가 $\overrightarrow F = (P \ \hat i, Q \ \hat j, R \ \hat k)$ 라고 할 때, <br>

라플라시안 공식: $\bigtriangledown \cdot \overrightarrow F = (\frac{\delta}{\delta x}, \frac{\delta}{\delta y}, \frac{\delta}{\delta z}) \cdot (P, Q, R)$ $= \dfrac{\delta P}{\delta x} + \dfrac{\delta Q}{\delta y} + \dfrac{\delta R}{\delta z}$ <br>

*cf.)* dot ($\cdot$) 연산자: 길이가 같은 두 sequence의 구성 요소를 곱하고, 그 결과의 합을 반환하는 연산자로 벡터의 내적과 같은 의미의 연산자<br><br>

<hr>

# 더 읽을거리

## [A Gentle Introduction to the Laplacian](https://machinelearningmastery.com/a-gentle-introduction-to-the-laplacian/)

Pierre-Simon de Laplace에 의해 천체 역학 또는 우주 공간에서 물체의 운동 연구에 처음 적용되었다는 라플라시안은 이미지 처리(예:Edge Detection) 및 spectral clustering과 관련된 응용 프로그램에 사용된 불연속 공간으로 재구성(recast)될 수 있으며, 이러한 특성을 이용하서 이미지에서 edge detection 등과 같은 분야에 적용된다고 한다.

[라플라시안에 대해 소개한 Machine Learning Mastery 사이트](https://machinelearningmastery.com/a-gentle-introduction-to-the-laplacian/)에서는 다음의 세 가지 관점에 대한 인사이트를 주고자 하는 것 같다.

1. 라플라시안과 발산과의 관계
2. 라플라시안과 Hessian 의 관계 (볼록? 오목?)
3. 연속형 라플라시안이 어떻게 이산 공간으로 재구성되고, 이미지 처리나 spectral clustering 응용 분야에 적용될 수 있는가?  

<br>

