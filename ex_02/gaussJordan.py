# 입력: 정칙행렬 A
# 출력: A의 역행렬 B

import numpy as np
import sys

def gaussJordan(A):
    n = len(A) # 행렬의 크기
    # 상삼각 행렬(사다리꼴 행렬)
    B = np.eye(n) # 단위행렬 B 초기화
    for j in range(0, n-1): # 마지막 열까진 체크 안함, j는 피벗위치, n-2까지
        # 피봇이 0인지 체크
        if np.abs(A[j, j] - 0.0) < sys.float_info.epsilon: 
            for k in range (j+1, n): # 아래 행들 중에서 피벗 대체할 수 있는 행을 찾음. k는 j+1부터 n-1까지
                if np.abs(A[k, j] - 0.0) > sys.float_info.epsilon: # A[k,j]가 0이 아닌 경우
                    temp = np.copy(A[k, :]); tempB = np.copy(B[k, :]) # k행 전체를 복사
                    A[k, :] = A[j, :]; B[k, :] = B[j, :]
                    A[j, :] = temp; B[j, :] = tempB
                    break
        for i in range(j+1, n): # j 번째 열 아래 원소들을 0으로 만드는 단계
            lam = A[i,j]/A[j,j] # A[i,j]를 0으로 만들기 위한 계수
            A[i, :] = A[i, :] - lam * A[j, :] # A[i,j]를 0으로 만들기 위해 A[i,:]에서 A[j,:]의 lam배를 빼줌
            B[i, :] = B[i, :] - lam * B[j, :] # B[i,:]도 동일하게 갱신

    #해의 존재 유무 확인
    if (np.prod(np.diag(np.abs(A))) - 0.0) < sys.float_info.epsilon: # 대각선 원소 중 하나라도 0이면 해가 존재하지 않음, A를 절댓값 취한 대각원소만 꺼내 곱함. 이 값과 0.0값의 차이가 기계상수보다 작으면  
        print('해가 존재하지 않거나 무수히 많음')
        exit()

    # 대각원소를 1로 만드는 단계
    for i in range(0, n):
        lam = A[i,i] # A[i,i]를 1로 만들기 위한 계수
        A[i, :] = A[i, :] / lam # A[i,:]를 lam으로 나눠서 A[i,i]를 1로 만듦
        B[i, :] = B[i, :] / lam # B[i,:]도 동일하게 갱신

    # print(A) # 상삼각 행렬로 변환된 A를 출력
    
    # 항등행렬화
    for i in range(n-1, -1, -1): # n-1부터 0까지 1씩 감소하면서 반복,아래행부터 0행까지 올림
        for j in range(i-1, -1, -1): # i-1부터 0까지 1씩 감소하면서 반복, i행 위 행들을 0으로 바꿈. 
            lam = A[j,i] # j 행 i열 원소, i열은 pivot위치. 
            A[j, :] = A[j, :] - lam * A[i, :] # A[j,i]를 0으로 만들기 위해 A[j,:]에서 A[i,:]의 lam배를 빼줌
            B[j, :] = B[j, :] - lam * B[i, :] # B[j,:]도 동일하게 갱신


    # print(A)

    return B

# A = np.array([[1.0, 3.0, -2.0], [2.0, 6.0, -2.0], [0.0, 1.0, 1.0]])
# x = gaussJordan(A)
# print(x)


