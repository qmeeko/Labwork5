import numpy as np
import math
# 1 Задание
x = (2.57e3)
f = (0.873)
y = (pow(math.sin((math.pi/8)-f),2)+pow(3+pow(x,2),1/4))/2
print(f"1.1. Значение y = {y}")
# 2 Задание
X = np.ones((12, 3))
X[:, 1] = np.random.randint(9, 21, 12)
X[:, 2] = np.random.randint(60, 83, 12)

Y = np.random.uniform(13.5,18.6,12)

A = np.linalg.inv(X.transpose() @ X) * (X.transpose() @ Y)

print(f"1.2 Вектор оценок A = {A}")
