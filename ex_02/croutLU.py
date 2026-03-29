# 입력: 정칙행렬 A, 열벡터 B
# 출력: 해 X

import numpy as np

def croutLU(A, b):
    n = len(b) # 행렬의 크기
    L = np.zeros((n, n)) # 하삼각 행렬 L 초기화
    U = np.zeros((n, n)) # 상삼각 행렬 U 초기화

    # 하삼각 행렬(사다리꼴 행렬)
    # L의 첫번쨰 열 -> U의 첫번쨰행 ...
    for i in range(0, n):
        U[i, i] = 1.0 # U의 대각원소는 1로 고정

    for i in range(0, n):
        for j in range(i, n): # i는 열j 는 행
            if i == 0:
                L[j, i] = A[j, i]
            else:
                L[j, i] = A[j, i] - np.dot(L[j, 0:i], U[0:i, i])
        for j in range(i+1 , n): # j는 열, i는 행
            if i == 0:
                U[i, j] = A[i, j] / L[i, i]
            else:
                U[i, j] = (A[i, j] - np.dot(L[i, 0:i], U[0:i, j])) / L[i, i]

    print(L)
    print(U)

    # 대입법
    z = np.zeros((n,1)) # 중간 벡터 z 초기화
    z[0] = b[0]/L[0, 0]
    for i in range(1, n):
        z[i] = (b[i] - np.dot(L[i, 0:i], z[0:i])) / L[i, i]

    # 역대입법
    x = np.zeros((n,1)) # 해 벡터 x 초기화
    x[n - 1] = z[n - 1]/U[n - 1, n - 1]
    for i in range(n-2, -1, -1): # n-2부터 0까지 1씩 감소하면서 반복
        x[i] = (z[i] - np.dot(U[i,i+1:n], x[i+1:n])) / U[i,i]

    return x

# A = np.array([[2.0, 4.0, 0.0, 2.0, 6.0], [1.0, 5.0, 3.0, -2.0, 9.0], [2.0, 3.0, 3.0, 11.0, 0.0], [1.0, 4.0, 3.0, 6.0, 11.0], [3.0, 7.0, -1.0, 0.0, 21.0]])
# b = np.array([[14.0], [16.0], [19.0], [25.0], [30.0]])
# x = croutLU(A, b)
# print(x)