# numpy-numerical python-this is the library for working with array
# the array object in Numpy is called ndarray

import Numpy as np

arr= np.array([1,2,3,4,5])
print(arr)

# Vectorized operation

print(arr*2) # multiply each element by to instead of iterating each element

# multi-dimensional array

arr1 = np.array([[1,2,3,4],[5,6,7,8]])
print(arr1)


# array operations
print("Array Operations")
arr2 = np.array([[4,5,2],[4,5,2]])
print(f"Add: {arr2+2}")
print(f"Sub: {arr2-2}")
print(f"Mul: {arr2*2}")
print(f"Div: {arr2//2}")
print(f"square: {arr2**2}")

# Array shape and size
matrix = np.array([[1,2,3,4],[5,6,7,8]])
print(matrix.shape)
print(matrix.size)

# built-in mathematical functions
matrix2 = np.array([[1,2,3,4],[5,6,7,8]])
print(" ")
print(np.sum(matrix2))
print(np.min(matrix2))
print(np.max(matrix2))
print(np.median(matrix2))
print(np.std(matrix2))
print(np.average(matrix2))