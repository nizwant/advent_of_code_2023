with open("day_19/input.txt", "r") as f:
    data = f.readlines()

rules = {}
was_empty_line = False
for line in data:
    line = line.strip()
    if not line:
        break
    key, val = line.split("{")
    val = val[:-1]
    val = val.split(",")
    rules[key] = val


answer = 0
stack = [([1, 4000, 1, 4000, 1, 4000, 1, 4000], "in")]
while stack:
    parts, start = stack.pop()
    if start == "A":
        answer += (
            (parts[1] - parts[0] + 1)
            * (parts[3] - parts[2] + 1)
            * (parts[5] - parts[4] + 1)
            * (parts[7] - parts[6] + 1)
        )
        continue

    if start == "R":
        continue

    workflow = rules[start]
    for rule in workflow:
        if ":" not in rule:
            stack.append((parts, rule))
            continue

        rule, direction = rule.split(":")
        if rule[0] == "x":
            i = 0
        elif rule[0] == "m":
            i = 2
        elif rule[0] == "a":
            i = 4
        elif rule[0] == "s":
            i = 6

        val_min, val_max = parts[i], parts[i + 1]
        if rule[1] == ">":
            if val_min > int(rule[2:]):
                stack.append((parts, direction))
                break
            elif val_max <= int(rule[2:]):
                continue
            else:
                a = parts.copy()
                a[i] = int(rule[2:]) + 1
                stack.append((a, direction))
                parts[i + 1] = int(rule[2:])

        elif rule[1] == "<":
            if val_max < int(rule[2:]):
                stack.append((parts, direction))
                break
            elif val_min >= int(rule[2:]):
                continue
            else:
                a = parts.copy()
                a[i + 1] = int(rule[2:]) - 1
                stack.append((a, direction))
                parts[i] = int(rule[2:])


print(answer)
