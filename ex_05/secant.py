#입력: 함수 f, 초기점 x0, x1, 허용오차 tol, 최대 반복횟수 kmax
#출력: 근사해 approx

def secant(f, x0, x1, tol, kmax):
    fx0 = f(x0)
    if(fx0 == 0.0): return x0
    fx1 = f(x1)
    if(fx1 == 0.0): return x1

    for i in range(kmax):
        c = x1 - (fx1*(x1-x0))/(fx1-fx0); fc = f(c)
        if(abs(fc) < tol): return c
        x0 = x1; fx0 = f(x0)
        x1 = c; fx1 = f(x1)
        print(c)

    approx = c
    return approx

# secant 호출하여 실행
def f(x) : return x**2 - 4
tol = 1.0e-10
kmax = 10
x = secant(f, 0.0, 5.0, tol, kmax)
print('secant approx = ', x)