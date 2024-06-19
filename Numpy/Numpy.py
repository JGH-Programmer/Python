import numpy as np

A = np.array([[1, 2], [3, 4], [5, 6]])

B = np.concatenate(([A,A]),axis=1)
C = A.flatten()
print(C)

# 데이터 생성
data = np.array([[1, 2], [3, 4], [5, 6]])

# 정규화
mean = np.mean(data, axis=0)
std = np.std(data, axis=0)
normalized_data = (data - mean) / std
print("정규화된 데이터:\\n", normalized_data)

# 데이터 생성
data = np.array([[1, 2], [np.nan, 4], [5, np.nan]])

# 결측치 처리
mean = np.nanmean(data, axis=0)
inds = np.where(np.isnan(data))
data[inds] = np.take(mean, inds[1])
print("결측치 처리된 데이터:\\n", data)

