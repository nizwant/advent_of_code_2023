with open("./day_3/input.txt") as f:
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


adjecent_cells = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 0),
]
bit_mask_matrix = [[False for i in range(size)] for j in range(size)]


for i, row in enumerate(matrix):
    for j, cell in enumerate(row):
        if cell in list(".0123456789"):
            continue
        for adjecent_cell in adjecent_cells:
            if is_valid_matrix_index(i + adjecent_cell[0], j + adjecent_cell[1], size):
                bit_mask_matrix[i + adjecent_cell[0]][j + adjecent_cell[1]] = True

sum = 0
for i, row in enumerate(matrix):
    number = 0
    if_number_part_of_engine = False
    for j, cell in enumerate(row):
        if cell in list("0123456789"):
            number = number * 10 + int(cell)
            if bit_mask_matrix[i][j]:
                if_number_part_of_engine = True
            continue

        if if_number_part_of_engine:
            sum += number

        number = 0
        if_number_part_of_engine = False

    if if_number_part_of_engine:
        sum += number

print(sum)
