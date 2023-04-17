import numpy as np

a = np.array(
    [
    [3,1,1],
    [1,-2,-1],
    [1,1,1]
    ])

print(a)
print(np.shape(a))

b = np.array(
    [4,1,2]
)

print(b)
print(np.shape(b))

a_inv = np.linalg.inv(a)

print(a_inv)
print(np.shape(a_inv))

answer = np.dot(a_inv, b)

print(answer)
print(np.shape(answer))

print("change branch to prg")