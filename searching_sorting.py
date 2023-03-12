import numpy as np
arr = np.array([1,2,3,4,5,6,7,4,4])
alphaArr = np.array(["banana","apple","orange"])

x = np.where(arr == 4)
print(x)

#even position in array
y = np.where(arr%2 == 0)
print(y)

#sorting
z = np.sort(arr)
print(z)

q = np.sort(alphaArr)
print(alphaArr)
print(q)