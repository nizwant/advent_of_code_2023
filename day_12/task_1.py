with open("day_12/input.txt", "r") as file:
    data = file.readlines()

accumulator = 0
for line in data:
    line = line.strip()
    sequence, list_of_lengths = line.split(" ")
    list_of_lengths = list_of_lengths.split(",")
    list_of_lengths = [int(length) for length in list_of_lengths]
    indexes_when_hash_is = [i for i, val in enumerate(sequence) if val == "?"]
    sequence = [sequence]
    ppp = sum(list_of_lengths)
    for i in indexes_when_hash_is:
        new = []
        for seq in sequence:
            new.append(seq[:i] + "." + seq[i + 1 :])
            new.append(seq[:i] + "#" + seq[i + 1 :])
        sequence = new

    acc = 0
    for seq in sequence:
        rec = []
        aaaa = 0
        for i in seq:
            if i == "#":
                aaaa += 1
            else:
                if aaaa != 0:
                    rec.append(aaaa)
                aaaa = 0
        if aaaa != 0:
            rec.append(aaaa)
        if rec == list_of_lengths:
            acc += 1

    accumulator += acc

print(accumulator)
