import numpy as np
arr = np.array([1,2,3,4])
for x in arr:
    print(x)

arr1 = np.array([[1,2,3,4],[5,6,7,8]])
for x in arr1:
    print("array",x)
    for y in x:
        print("value",y)