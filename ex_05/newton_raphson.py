# 입력: 함수 f, 미분 함수 df, 초기점 x0, 허용 오차 tol, 최대 반복횟수 kmax
# 출력: 근사해 approx

def newton_raphson(f, df, x0, tol, kmax):
    fx0 = f(x0)
    if(fx0 == 0.0): return x0

    for i in range(kmax):
        c = x0 - fx0/df(x0); fc = f(c)
        if(abs(fc)<tol): return c
        x0 = c; 
        fx0 = f(x0)
        print(c)

    approx = c
    return approx

# newton_raphson 호출하여 실행
def f(x) : return x**2 - 4
def df(x) : return 2*x

tol = 1.0e-10
kmax = 10
x = newton_raphson(f, df, 5.0, tol, kmax)
print('newton_raphson approx = ', x)