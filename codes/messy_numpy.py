import numpy as np

# === BUGS ===
# 1. Which command allow for reproducible results?
np.random.seed(20) #set same starting state
arr = np.random.rand(5) * 100  # Random array

# 2. Inefficient filtering!
filtered = arr[arr>50] #filtering boolean indexing technique

# 3. Any better method to calculate mean?
mean_val=np.mean(arr) #numpy mean

# 4. Three loops for matrix multiplication - that's definitely not optimal
def matrix_mult(a, b):
    return np.dot(a,b) #numpy dot function
  
# 5. Heard of multidimensional slicing?
def get_submatrix(matrix, rows, cols):
    submatrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix[i][j])
        submatrix.append(row)
    return submatrix 

# 6. NumPy uses SIMD, Did you know that?
def square_elements(arr):
    return list(map(lambda x: x**2, arr))

# 7. Does this work for 2D arrays?
def stack_vertically(a, b):
    return a + b