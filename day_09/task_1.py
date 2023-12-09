with open("day_09/input.txt") as f:
    data = f.readlines()


cleaned_data = []
for line in data:
    line = line.strip()
    line = line.split(" ")
    cleaned_data.append([int(number) for number in line])


def create_sequence_of_difference(sequence):
    sequence_of_difference = []
    for i in range(len(sequence) - 1):
        sequence_of_difference.append(sequence[i + 1] - sequence[i])
    return sequence_of_difference


sum_of_predictions = 0
for sequence in cleaned_data:
    list_of_sequence_differences = [sequence]
    while any(list_of_sequence_differences[-1]):
        list_of_sequence_differences.append(
            create_sequence_of_difference(list_of_sequence_differences[-1])
        )

    while len(list_of_sequence_differences) > 1:
        list_used_to_prediction = list_of_sequence_differences.pop()
        list_of_sequence_differences[-1].append(
            list_used_to_prediction[-1] + list_of_sequence_differences[-1][-1]
        )

    sum_of_predictions += list_of_sequence_differences[0][-1]

print(sum_of_predictions)
