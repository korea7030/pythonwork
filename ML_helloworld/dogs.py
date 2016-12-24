import numpy as np
import matplotlib.pyplot as plt

## 개의 종류 부류(그레이하운드 vs 레브라도)
greyhounds = 500
labes = 500

# 그레이하운드, 레브라도 키 분포
grey_height = 28 + 4 * np.random.randn(greyhounds)
lab_height = 24 + 4 * np.random.randn(labes)

## 키라는 특성에 대한 histogram
plt.hist([grey_height, lab_height], stacked = True, color=['r', 'b'])
plt.show()
