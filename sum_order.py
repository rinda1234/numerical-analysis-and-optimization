# 처음에 1.0인 상태로 더한것과 0.0에서 마지막에 1.0을 더한 것의 차이. 
sum1 = 1.0
sum2 = 0.0

dif = 1 / (10 ** 16) # ** : 거듭제곱

for i in range(1, 10 ** 7): # 1 부터 10의 7승까지 반복
    sum1 += dif
    sum2 += dif

sum2 += 1.0

print(sum1)
print(sum2)