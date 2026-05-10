# 입력: 행렬 A, 초기벡터 x, 이동변수 alpha, 최대 반복횟수 kmax
# 출력: A의 우세 고유값, 우세 고유벡터

import numpy as np

def invpower(A, x, kmax, alpha):
    # A 가 정방 행렬인지 체크
    m, n = A.shape
    if m != n:
        print('정방행렬이 아님')
        return
    
    B = A - np.eye(n)*alpha # 이동변수 alpha를 이용해서 A에서 alpha*I를 뺌
    
    for k in range(0, kmax):
        y = np.linalg.solve(B, x) # B*y= x B와 x의 선형방정식 B*y = x를 풀어서 y를 구함
        # 1차 방법
        # index = np.argmax(np.abs(y)) # 절대값이 최대값인 인덱스
        # value = y[index] # y의 원소 중 절댓값이 가장 큰 원소의 값
        # vector = y / value # y를 value로 나눠서 새로운 x를 만듦
        # 2차 방법
        value = np.dot(x, y)
        vector = y / np.linalg.norm(y) # 이렇게 하면 정규화된 고유벡터가 나옴
        value = (1.0 / value) + alpha # alpha에 가까운 고유값 반환
        print('k={0} \t 고유값={1} \t 고유벡터={2}'.format(k, value, vector))
        x = np.copy(vector) # x를 vector로 갱신
        
    return value, vector

A = np.array([[2.0, -1.0, 1.0], [-1.0, 1.0, -2.0], [1.0, -2.0, 1.0]])
x = np.array([1.0, 1.0, 1.0])
kmax = 100
alpha = -0.5 # 0 인경우 고윳값이 -1과 1중에 무엇과 가까운지 판단이 안됨. 
a, b = invpower(A, x, kmax, alpha)
print(a)
print(b)

w, V = np.linalg.eig(A)
print(w)
print(V)