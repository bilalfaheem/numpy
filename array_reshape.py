import numpy as np
arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr2 = arr1.reshape(3,4)
arr5 = arr1.reshape(2,2,3)

print(arr1.ndim)
print(arr2.ndim)
print(arr1)
print(arr2)
print(arr5)
print(arr1.shape)
print(arr2.shape)
print(arr5.shape)

#Flattering an array
#converting multidimensional array to 1-D array

arr3 = np.array([[1,3,4],[2,4,7]])
arr4 = arr3.reshape(-1)
print(arr3.ndim)
print(arr4.ndim)
print(arr3)
print(arr4)

#indexing
print(arr3[1,2])