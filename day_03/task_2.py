with open("./day_03/input.txt") as f:
    lines = f.readlines()

# creation of the matrix
matrix = []
for line in lines:
    row = []
    for char in line.strip():
        row.append(char)
    matrix.append(row)

# size of square matrix
size = len(matrix)


def is_valid_matrix_index(i, j, n):
    return i >= 0 and i < n and j >= 0 and j < n


adjacent_cells = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
bit_mask_matrix = [[[0, []] for i in range(size)] for j in range(size)]

for i, row in enumerate(matrix):
    for j, cell in enumerate(row):
        if cell == "*":
            for adjacent_cell in adjacent_cells:
                if is_valid_matrix_index(
                    i + adjacent_cell[0], j + adjacent_cell[1], size
                ) and matrix[i + adjacent_cell[0]][j + adjacent_cell[1]] in list(
                    "0123456789"
                ):
                    i_tmp = i + adjacent_cell[0]
                    j_tmp = j + adjacent_cell[1]
                    while is_valid_matrix_index(i_tmp, j_tmp, size) and matrix[i_tmp][
                        j_tmp
                    ] in list("0123456789"):
                        j_tmp += -1
                    j_tmp += 1
                    if (i_tmp, j_tmp) not in bit_mask_matrix[i][j][1]:
                        bit_mask_matrix[i][j][1].append((i_tmp, j_tmp))
                        bit_mask_matrix[i][j][0] += 1

sum = 0
for row in bit_mask_matrix:
    for cell in row:
        if cell[0] == 2:
            i, j = cell[1][0]
            number_1 = 0
            while is_valid_matrix_index(i, j, size) and matrix[i][j] in list(
                "0123456789"
            ):
                number_1 = number_1 * 10 + int(matrix[i][j])
                j += 1

            i, j = cell[1][1]
            number_2 = 0
            while is_valid_matrix_index(i, j, size) and matrix[i][j] in list(
                "0123456789"
            ):
                number_2 = number_2 * 10 + int(matrix[i][j])
                j += 1

            sum += number_1 * number_2

print(sum)
