import time

with open("day_12/input.txt", "r") as file:
    data = file.readlines()


def backtrack(index_list_q_m, list_of_lengths, sequence):
    if not index_list_q_m:
        rec = calculate(sequence)
        return 1  # rec == list_of_lengths

    acc = 1  # 0 counts the backtrack invocations
    sequence = sequence[: index_list_q_m[0]] + "#" + sequence[index_list_q_m[0] + 1 :]
    li = calculate(sequence[: index_list_q_m[0] + 1])
    if len(li) < 1 or (
        len(li) <= len(list_of_lengths)
        and li[-1] <= list_of_lengths[len(li) - 1]
        and li[:-1] == list_of_lengths[: len(li) - 1]
        # we checked previous elements earlier, maybe only tail needs to match
    ):
        acc += backtrack(index_list_q_m[1:], list_of_lengths, sequence)
    sequence = sequence[: index_list_q_m[0]] + "." + sequence[index_list_q_m[0] + 1 :]

    if len(li) != 0:
        if li[-1] == 1:
            li = li[:-1]
        else:
            li[-1] -= 1

    if len(li) < 1 or (
        len(li) <= len(list_of_lengths)
        and li[-1] <= list_of_lengths[len(li) - 1]
        and li[:-1] == list_of_lengths[: len(li) - 1]
        # ist almost the same calculation as in line 18
    ):
        acc += backtrack(index_list_q_m[1:], list_of_lengths, sequence)

    return acc


# 29790435
# 319578
# 30.11418390274048


def calculate(seq):
    seq = seq.replace(".", " ")
    seq = seq.split()
    return [len(i) for i in seq]


times = time.time()
accumulator = 0
for line in data:
    line = line.strip()
    sequence, list_of_lengths = line.split(" ")
    list_of_lengths = [int(length) for length in list_of_lengths.split(",")]
    sequence = (sequence + "?") * 1 + sequence
    list_of_lengths = list_of_lengths * 2
    indexes_when_question_is = [i for i, val in enumerate(sequence) if val == "?"]
    accumulator += backtrack(indexes_when_question_is, list_of_lengths, sequence)
    print(line)

print(accumulator)
print(time.time() - times)
