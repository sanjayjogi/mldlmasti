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
