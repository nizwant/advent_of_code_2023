with open("day_13/input.txt") as f:
    data = f.readlines()

list_of_patterns = [[]]
for i in data:
    i = i.strip()
    if i == "":
        list_of_patterns.append([])
    else:
        list_of_patterns[-1].append(i)


def calculate_number_of_diff_in_reflections(left, right):
    number_of_differences = 0
    for left_row, right_row in zip(left, right):
        row_diff = [0 for m, n in zip(left_row, right_row) if m != n]
        number_of_differences += len(row_diff)
    return number_of_differences


acc = 0
for pattern in list_of_patterns:
    for i, row in enumerate(pattern[1:], 1):
        minimum = min(i, len(pattern) - i)
        number_of_diff = calculate_number_of_diff_in_reflections(
            pattern[i - minimum : i], pattern[i : i + minimum][::-1]
        )
        if number_of_diff == 1:
            acc += 100 * i
    pattern = list(zip(*pattern))
    for i, row in enumerate(pattern[1:], 1):
        minimum = min(i, len(pattern) - i)
        number_of_diff = calculate_number_of_diff_in_reflections(
            pattern[i - minimum : i], pattern[i : i + minimum][::-1]
        )
        if number_of_diff == 1:
            acc += i

print(acc)
