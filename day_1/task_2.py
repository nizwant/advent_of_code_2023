import regex as re  # different regex module that supports overlapped matches

# read input
with open("input.txt") as f:
    data = f.readlines()

accumulator = 0
dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

pattern = re.compile(
    r"(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9)"
)

for line in data:
    match = pattern.findall(line, overlapped=True)
    if match[0] in dict:
        match[0] = dict[match[0]]

    if match[-1] in dict:
        match[-1] = dict[match[-1]]

    number = int(match[0] + match[-1])
    accumulator += number

print(accumulator)
