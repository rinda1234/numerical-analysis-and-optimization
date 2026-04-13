# 입력: SPD(sparse positive definite, 대부분의 원소가 0 인 양의 정부호 행렬) 행렬 A, 초기벡터 x, 허용오차  tol, 최대 반복횟수 kmax
# 출력: 근사해 approx

import numpy as np

def gaussSeidel(A, b, x, kmax, tol):
    r = b - np.matmul(A, b) # 초기 잔여 오차 벡터 r 
    rnorm = np.linalg.norm(r) # 잔차 크기
    bnorm = np.linalg.norm(b) # b의 크기
    n = len(A) # 행렬의 크기
    xnew = np.copy(x) 
    k = 1
    print('k \t\t 근사해')
    while((rnorm > (tol * bnorm)) and (k <= kmax)): # 잔여 오차가 b 에 대한 허용오차보다 크면 계속 돌아가고 
        # x[i] 를 한 행씩 업데이트
        for i in range(0, n):
            Lsum = np.dot(A[i, 0:i], xnew[0:i]) # i 번째 행에서 왼쪽 부분 합 계산
            # Lsum = np.matmul(A[i, 0:i], x[0:i]) # i 번째 행에서 왼쪽 부분 합 계산
            Usum = np.dot(A[i, i+1:n], x[i+1:n]) # i 번째 행에서 오른쪽 부분 합 계산
            xnew[i] = (b[i] - Lsum - Usum) / A[i, i] # i 번째 원소 업데이트   
        print('k={0} \t x={1}'.format(k, xnew)) # k 번째 근사해 출력
        x = np.copy(xnew) # x를 업데이트된 xnew로 복사
        r = b - np.matmul(A, b) # 잔여 오차 벡터 r 업데이트
        rnorm = np.linalg.norm(r) # 잔차 크기 업데이트
        k += 1 # 반복 횟수 증가
    approx = xnew # 최종 근사해
    return approx

A = np.array([[8.0, 2.0, -4.0], [5.0, 10.0, -3.0], [-1.0, 5.0, 20.0]])       
b = np.array([6.0, 12.0, 24.0])
x = np.array([0.0, 0.0, 0.0])
kmax = 10
tol = 0.0001
approx = gaussSeidel(A, b, x, kmax, tol)
print(approx)