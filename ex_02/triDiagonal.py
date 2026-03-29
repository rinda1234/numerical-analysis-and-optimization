# 입력: 삼중대각 정칙행렬 A, 열벡터 B
# 출력: 해 X

import numpy as np
import sys

def triDiagonal(A, b):
    n = len(b) # 행렬의 크기
    # 상삼각 행렬(사다리꼴 행렬)
    for j in range(0, n-1):
        lam = A[j+1, j]/A[j,j]  # A[j+1,j]를 0으로 만들기 위한 계수 
        A[j+1, j] = 0.0 # A[j+1,j]를 0으로 만듦
        A[j+1, j+1] = A[j+1, j+1] - lam * A[j, j+1] # A[j+1,j+1]을 A[j+1,j+1]에서 A[j,j+1]의 lam배를 빼줌
        b[j+1] = b[j+1] - lam * b[j] # b[j+1]을 b[j+1]에서 b[j]의 lam배를 빼줌

    # print(A) # 상삼각 행렬로 변환된 A를 출력
    # print(b) # 상삼각 행렬로 변환된 A에 대응하는 열벡터 b를 출력

    #해의 존재 유무 확인
    if (np.prod(np.diag(np.abs(A))) - 0.0) < sys.float_info.epsilon: # 대각선 원소 중 하나라도 0이면 해가 존재하지 않음, A를 절댓값 취한 대각원소만 꺼내 곱함. 이 값과 0.0값의 차이가 기계상수보다 작으면  
        print('해가 존재하지 않거나 무수히 많음')
        exit()
    
    # 역대입법
    x = np.zeros((n,1)) # 해 벡터 x 초기화
    x[n - 1] = b[n - 1]/A[n - 1, n - 1]
    for i in range(n-2, -1, -1): # n-2부터 0까지 1씩 감소하면서 반복
        x[i] = (b[i] - (A[i,i + 1] * x[i + 1])) / A[i,i]
    
    return x

# A = np.array([[2.0, 6.0, 0.0], [-2.0, -7.0, -3.0], [0.0, 2.0, -4.0]])
# b = np.array([[-10.0], [3.0], [-16.0]])
# x = triDiagonal(A, b)
# print(x)