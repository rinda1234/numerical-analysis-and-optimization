# 입력: 정칙행렬 A, 열벡터 B
# 출력: 해 X

import numpy as np
import sys

def gaussPivot(A, b):
    n = len(b) # 행렬의 크기
    # 상삼각 행렬(사다리꼴 행렬)
    for j in range(0, n-1):
        target_row = np.argmax(np.abs(A[j:, j])) + j # A[j:n, j]에서 절댓값이 가장 큰 원소의 인덱스에 j를 더하여 target_row 계산, j를 더한 이유는 np.argmax가 A[j:, j]에서의 인덱스를 반환하기 때문(부분행렬에서의)
        if target_row != j:
            temp = np.copy(A[target_row, :]); tempb = np.copy(b[target_row])
            A[target_row, :] = A[j, :]; b[target_row] = b[j]
            A[j, :] = temp; b[j] = tempb

        for i in range(j+1, n):
            lam = A[i,j]/A[j,j] # A[i,j]를 0으로 만들기 위한 계수
            # A[i,j + 1:n] = A[i,j + 1:n] - lam * A[j,j + 1:n] 이렇게 하면 상삼각행렬의 왼쪽 아래부분이 0이 안됨. 
            A[i, :] = A[i, :] - lam * A[j, :] # A[i,j]를 0으로 만들기 위해 A[i,:]에서 A[j,:]의 lam배를 빼줌
            b[i] = b[i] - lam * b[j] 

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
        x[i] = (b[i] - np.dot(A[i,i+1:n], x[i+1:n])) / A[i,i]
    
    return x

# A = np.array([[1.0, -3.0, 3.0], [-3.0, 2.0, 3.0], [-1.0, 2.0, -1.0]])
# b = np.array([[-6.0], [-13.0], [3.0]])
# x = gaussPivot(A, b)
# print(x)
