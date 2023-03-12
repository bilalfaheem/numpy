import numpy as np
#slicing [start:end] step 0 default, end value not included
#[start:end:step]
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr[0:8])
print(arr[0:9])
print(arr[3:])
print(arr[:5])

arr1 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(arr1[0,0:6:2])