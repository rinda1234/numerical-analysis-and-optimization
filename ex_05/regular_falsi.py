#입력: 함수 f, 구간 [a, b], 허용 오차 tol, 최대 반복횟수 kmax
#출력: 근사해 approx

def regular_falsi(f, a, b, tol, kmax):
    fa = f(a)
    if(fa == 0.0): return a
    fb = f(b)
    if(fb == 0.0): return b
    if(fa * fb) > 0.0:
        print('Root is not bracketed')
        exit()
    
    for i in range(kmax):
        c = (a*fb - b*fa) / (fb - fa); fc = f(c)
        if(abs(fc)<tol): return c
        if(fa * fc) < 0.0:
            b = c; fb = fc
        else:
            a = c; fa = fc
        print(c)
    
    approx = c
    return approx

# regular_falsi 호출하여 실행
def f(x) : return x**2 - 4*x - 4

tol = 1.0e-10
kmax = 10
x = regular_falsi(f, 0.0, 5.0, tol, kmax)
print('regular_falsi approx = ', x)