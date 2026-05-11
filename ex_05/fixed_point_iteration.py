# 입력: 함수 g, 초기점 x0, 허용오차 tol, 최대 반복횟수 kmax
# 출력: 근사해 approx

def fixed_point_iteration(g, x0, tol, kmax):
    gx0 = g(x0)
    if(gx0 == 0.0): return x0
    
    for i in range(kmax):
        if(abs(g(x0) - x0) < tol): return x0
        x0 = g(x0)
        print(x0)

    approx = x0
    return approx

# fixed_point_iteration 호출하여 실행
def g(x) : return 1 + 1/x

tol = 1.0e-10
kmax = 10
x = fixed_point_iteration(g, 2.0, tol, kmax)
print('fixed_point_iteration approx = ', x)