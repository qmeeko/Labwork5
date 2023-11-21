import numpy as np
import matplotlib.pyplot as plt

a = np.arange(-5,12,1.75)
x = 12.1
f = np.exp(a*x) - 3.45 * a
f = np.array(f,dtype=float)
print(f"Массив: {f}")
i = 0
for item in a:
    print(f"a = {item}, f = {f[i]}")
    i+=1

print(f"F(max) = {np.max(f):.4f}\n"
      f"F(min) = {np.min(f):.4f}\n"
      f"F(mean) = {np.mean(f):.4f}")

print(f"Длина массива: {len(f)}")
print(f"Отсортированный массив: {np.sort(f)}")

plt.plot(a, f)
plt.yscale(value="log")
plt.axhline(np.mean(f), color='red', label='Среднее значение f')

plt.title('График функции f')
plt.xlabel('a')
plt.ylabel('f')
plt.legend()
plt.show()