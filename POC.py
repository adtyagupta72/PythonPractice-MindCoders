import numpy as np
 
# Create arrays
arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[85,90,78],[72,88,95],[91,76,83]])  # 3 students x 3 subjects
 
print(arr2d.shape)     # (3, 3)
print(arr2d.dtype)     # int64
print(arr2d.ndim)      # 2 (2-dimensional)

zeros = np.zeros((3,4))           		# 3x4 array of 0s
ones  = np.ones((2,5))            		# 2x5 array of 1s
rng   = np.arange(0,50,5)         		# [0,5,10,15,...,45]
lin   = np.linspace(0,1,11)       		# 11 evenly spaced from 0 to 1
rand  = np.random.randint(40,100,(5,3))

print("zeros:", zeros)
print("ones:", ones)
print("rng:", rng)
print("lin:", lin)
print("rand:", rand)

# Vectorised math — no loops needed!
arr = np.array([10,20,30,40,50])
print(arr * 2)        # [20 40 60 80 100]
print(arr + 5)        # [15 25 35 45 55]
print(arr ** 2)       # [100 400 900 1600 2500]

# Statistics on arrays
marks_2d = np.array([[85,90,78],[72,88,95],[91,76,83]])
print(np.mean(marks_2d))           # Overall mean
print(np.mean(marks_2d, axis=1))   # Mean per student (row)
print(np.mean(marks_2d, axis=0))   # Mean per subject (column)
print(np.max(marks_2d))            # Highest mark
print(np.std(marks_2d))            # Standard deviation
 
# Boolean indexing (critical for data filtering!)
arr = np.array([55,82,43,91,67,78,35,88])
print(arr[arr > 70])   # [82 91 78 88] — only values > 70

