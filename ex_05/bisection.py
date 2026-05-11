#입력: 함수 f, 구간 [a, b], 허용 오차 tol, 최대 반복횟수 kmax
#출력: 근사해 approx

def bisection(f, a, b, tol, kmax):
    # fa나 fb가 0인 경우는 근이 a나 b인 경우이므로 바로 반환
    fa = f(a)
    if(fa == 0.0): return a
    fb = f(b)
    if(fb == 0.0): return b

    # fa와 fb의 부호가 같으면 근이 구간 [a, b]에 존재하지 않으므로 에러 메시지 출력 후 종료
    if(fa * fb) > 0.0:
        print('Root is not bracketed')
        exit()
    
    for i in range(kmax):
        length = (b-a)*0.5
        c = a + length; fc = f(c)
        if(abs(fc)<tol) and (abs(length)<tol): return c
        if(fc * fb) > 0.0:
            b = c; fb = fc
        else:
            a = c; fa = fc
        print(c)
    
    approx = c
    return approx

# bisection 호출하여 실행
def f(x) : return 2*x**3 - x**2 - 4

tol = 1.0e-10
kmax = 10
x = bisection(f, 0.0, 5.0, tol, kmax)
print('bisection approx = ', x)