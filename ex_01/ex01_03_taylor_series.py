# 목적 : 테일러전개에 따른 근사값
# 입력 : c=0에서 exp(x)의 n차 테일러전개
# 출력 : s는 x0=1인 죽 f(1)에서의 근사값

from math import factorial
sum = 0.0
for k in range(0, 10):
    sum += (1) ** k / factorial(k)
    
    if(k % 2) == 0: # k는 0부터 구해짐
        print(sum)