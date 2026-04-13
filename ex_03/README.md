# 📌 Python 출력 포맷 & NumPy dot vs matmul

## 🔹 Python 출력 포맷 방식

### 1. % formatting (C 스타일)

```python
name = "Tom"
age = 20

print("이름: %s, 나이: %d" % (name, age))
```

* C의 printf와 유사한 방식
* %s, %d 등의 형식 지정자 사용
* 현재는 잘 사용하지 않음

---

### 2. .format() 방식

```python
name = "Tom"
age = 20

print("이름: {}, 나이: {}".format(name, age))
```

```python
print("이름: {0}, 나이: {1}".format(name, age))
```

* 가독성이 좋음
* 위치 지정 가능

---

### 3. f-string (추천)

```python
name = "Tom"
age = 20

print(f"이름: {name}, 나이: {age}")
```

```python
print(f"내년 나이: {age + 1}")
```

* 가장 직관적인 방식
* Python 3.6 이상에서 사용 가능

👉 **f-string 사용 권장**

---

## 🔹 NumPy dot vs matmul

### 1. dot (내적 중심)

```python
import numpy as np

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

print(np.dot(A, B))
```

결과:

```
32
```

* 벡터: 내적 수행
* 행렬: 행렬곱처럼 동작
* 다차원에서 비직관적

---

### 2. matmul (행렬 곱)

```python
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print(np.matmul(A, B))
```

또는

```python
A @ B
```

* 행렬 곱 전용
* 다차원에서도 일관된 결과

---

## 🔥 핵심 차이

| 구분     | dot | matmul  |
| ------ | --- | ------- |
| 벡터     | 내적  | 행렬처럼 처리 |
| 2차원    | 행렬곱 | 행렬곱     |
| 3차원 이상 | 복잡함 | 배치 행렬곱  |

---

## ✅ 정리

* 출력 👉 f-string 사용
* 행렬 곱 👉 matmul(@) 사용
