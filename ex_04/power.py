# 입력: 행렬 A, 초기벡터 x, 최대 반복횟수 kmax
# 출력: A의 우세 고유값, 우세 고유벡터

import numpy as np

def power(A, x, kmax):
    # A 가 정방 행렬인지 체크
    m, n = A.shape
    if m != n:
        print('정방행렬이 아님')
        return

    for k in range(0, kmax):
        y = np.matmul(A, x) # A와 x의 행렬곱
        # 1차 방법
        # index = np.argmax(np.abs(y)) # 절대값이 최대값인 인덱스
        # value = y[index] # y의 원소 중 절댓값이 가장 큰 원소의 값
        # vector = y / value # y를 value로 나눠서 새로운 x를 만듦
        # 2차 방법
        value = np.dot(x, y)
        vector = y / np.linalg.norm(y) # 이렇게 하면 정규화된 고유벡터가 나옴
        print('k={0} \t 고유값={1} \t 고유벡터={2}'.format(k, value, vector))
        x = np.copy(vector) # x를 vector로 갱신
        
    return value, vector

A = np.array([[2.0, -1.0, 1.0], [-1.0, 1.0, -2.0], [1.0, -2.0, 1.0]])
x = np.array([1.0, 1.0, 1.0])
kmax = 100
a, b = power(A, x, kmax)
print(a)
print(b)

w, V = np.linalg.eig(A)
print(w)
print(V)