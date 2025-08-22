# Author    : Kiran raj R.
# Date      : 22/08/2025
# Question  : Create matrix


def createMatrix(row=2, column=2, fill=None):
    matrix = []
    
    i = j = 0
    for i in range(row):
        subMatrix = []
        for j in range (column):
            if fill is None:
                subMatrix.append(j)
            else:
                subMatrix.append(fill)
        matrix.append(subMatrix)
    return matrix

# Time complexity:    O(n*m)
# Space complexity:   O(n*m)


def print_matrix(matrix):
    if not matrix:
        print("The matrix is empty.")
        return

    print("[")
    for i, row in enumerate(matrix):
        # Use a list comprehension to convert each element to a string
        # and then join them with spaces.
        row_str = ", ".join(map(str, row))
        print(f" [{row_str}]", end="")
        # Add a comma and newline if it's not the last row
        if i < len(matrix) - 1:
            print(",")
    print("\n]")


# Test
print_matrix(createMatrix(3,3,1))