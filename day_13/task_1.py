with open("day_13/input.txt") as f:
    data = f.readlines()

list_of_patterns = [[]]
for i in data:
    i = i.strip()
    if i == "":
        list_of_patterns.append([])
    else:
        list_of_patterns[-1].append(i)

acc = 0
for pattern in list_of_patterns:
    for i, row in enumerate(pattern[1:], 1):
        minimum = min(i, len(pattern) - i)
        if pattern[i - minimum : i] == pattern[i : i + minimum][::-1]:
            acc += 100 * i

    pattern = list(zip(*pattern))
    for i, row in enumerate(pattern[1:], 1):
        minimum = min(i, len(pattern) - i)
        if pattern[i - minimum : i] == pattern[i : i + minimum][::-1]:
            acc += i

print(acc)
