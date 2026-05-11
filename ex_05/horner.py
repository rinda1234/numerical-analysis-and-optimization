# 입력: 다항식 poly, 초기점 x0, 허용오차 tol, 최대반복횟수 kmax
# 출력: 근사해 approx

def horner(poly, x0, tol, kmax):
    n = len(poly)
    px0 = poly[n-1]
    for i in range(n-1):
        px0 = px0 + poly[i]*x0**((n-1)-i)
    
    if(px0 == 0.0): return x0

    for i in range(kmax):
        a = poly[0]; b = 0.0
        for j in range(1, n):
            b = x0*b + a
            a = x0*a + poly[j]

        c = x0 - a/b
        if(abs(c-x0) < tol): return c
        x0 = c
        print(c)

    approx = c
    return approx

# horner 호출하여 실행
# 다항식 p(x) = 2*x**4 - 3*x**2 + 3*x - 4
poly = [2, 0, -3, 3, -4]
tol = 1.0e-10
kmax = 10
x = horner(poly, -2.0, tol, kmax)
print('horner approx = ', x)
