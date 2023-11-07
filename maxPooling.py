import numpy as np

# Create a sample 4x4 input matrix
input_matrix = np.array([[1, 2, 3, 4],
                         [5, 6, 7, 8],
                         [9, 10, 11, 12],
                         [13, 14, 15, 16]])

# Define the size of the pooling window
pool_size = 2

# Apply max pooling
output_matrix = np.zeros((2, 2))

for i in range(0, input_matrix.shape[0], pool_size):
    for j in range(0, input_matrix.shape[1], pool_size):
        output_matrix[i // pool_size, j // pool_size] = np.mean(input_matrix[i:i+pool_size, j:j+pool_size])

print("Input Matrix:")
print(input_matrix)
print("Output Matrix after Max Pooling:")
print(output_matrix)


import numpy as np

# Create a 3x3 input matrix
input_matrix = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])

# Define a 2x2 filter (kernel)
filter = np.array([[0, 1],
                   [-1, 2]])

# Calculate the output matrix dimensions
output_rows = input_matrix.shape[0] - filter.shape[0] + 1
output_cols = input_matrix.shape[1] - filter.shape[1] + 1

# Initialize the output matrix
output_matrix = np.zeros((output_rows, output_cols))

# Perform convolution
for i in range(output_rows):
    for j in range(output_cols):
        output_matrix[i, j] = np.sum(input_matrix[i:i+2, j:j+2] * filter)

print("Input Matrix:")
print(input_matrix)
print("Filter (Kernel):")
print(filter)
print("Output Matrix after Convolution:")
print(output_matrix)
