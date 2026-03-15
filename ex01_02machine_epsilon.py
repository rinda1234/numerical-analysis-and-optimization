# 목적 : 기계오차 측정
# 참고 : 실수와 기계오차

meps = 1.0
while(1 + meps > 1.0):
    meps /= 2.0

meps *= 2.0

print(meps)

# 시스템에 변수로 지정된 기계오차
import sys
print(sys.float_info.epsilon)

# 실수의 오차 처리
print(0.1 + 0.2 == 0.3) # False
print(0.1 + 0.2) # 0.30000000000000004

import math
print(math.fabs((0.1 + 0.2) - 0.3) <= sys.float_info.epsilon) # fabs : 실수의 절댓값 구하는 함수

