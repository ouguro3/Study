# numpy로 그래프 그리기

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3])
y = np.array([2,4,6])

print(x)
print(y)

plt.plot(x,y)
plt.show()