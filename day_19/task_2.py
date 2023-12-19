with open("day_19/input.txt", "r") as f:
    data = f.readlines()


class Part:
    def __init__(self, x_min, x_max, m_min, m_max, a_min, a_max, s_min, s_max):
        self.x = (x_min, x_max)
        self.m = (m_min, m_max)
        self.a = (a_min, a_max)
        self.s = (s_min, s_max)
        self.list_ordered = [x_min, x_max, m_min, m_max, a_min, a_max, s_min, s_max]

    def __repr__(self):
        return f"x={self.x}, m={self.m}, a={self.a}, s={self.s}"

    def get_number(self):
        return (
            (self.x[1] - self.x[0] + 1)
            * (self.m[1] - self.m[0] + 1)
            * (self.a[1] - self.a[0] + 1)
            * (self.s[1] - self.s[0] + 1)
        )


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
stack = [(Part(1, 4000, 1, 4000, 1, 4000, 1, 4000), "in")]
while stack:
    parts, start = stack.pop()
    if start == "A":
        answer += parts.get_number()
        continue

    if start == "R":
        continue

    workflow = rules[start]
    for rule in workflow:
        if ":" not in rule:
            stack.append((parts, rule))
        else:
            rule, direction = rule.split(":")
            if rule[0] == "x":
                val_min, val_max = parts.x[0], parts.x[1]
                i = 0
            elif rule[0] == "m":
                val_min, val_max = parts.m[0], parts.m[1]
                i = 2
            elif rule[0] == "a":
                val_min, val_max = parts.a[0], parts.a[1]
                i = 4
            elif rule[0] == "s":
                val_min, val_max = parts.s[0], parts.s[1]
                i = 6

            if rule[1] == ">":
                if val_min > int(rule[2:]):
                    stack.append((parts, direction))
                    break
                elif val_max <= int(rule[2:]):
                    continue
                else:
                    a = parts.list_ordered.copy()
                    a[i] = int(rule[2:]) + 1
                    stack.append((Part(*a), direction))

                    b = parts.list_ordered.copy()
                    b[i + 1] = int(rule[2:])
                    parts = Part(*b)

            elif rule[1] == "<":
                if val_max < int(rule[2:]):
                    stack.append((parts, direction))
                    break
                elif val_min >= int(rule[2:]):
                    continue
                else:
                    a = parts.list_ordered.copy()
                    a[i + 1] = int(rule[2:]) - 1
                    stack.append((Part(*a), direction))

                    b = parts.list_ordered.copy()
                    b[i] = int(rule[2:])
                    parts = Part(*b)


print(answer)
