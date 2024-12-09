import numpy as np

data = [[10,20,30,40],[50,60,70,80]]
k = np.array(data)
print(type(k.shape))

m = np.array([[ 0,  1,  2,  3,  4],
            [ 5,  6,  7,  8,  9],
            [10, 11, 12, 13, 14]])

value = m[1][2]
print(value)
value = m[2][4]
print(value)
value = m[1][1:3]
print(value)
value = m[1:3, 2]
print(value)
value = m[0:2, 3:]
print(value)