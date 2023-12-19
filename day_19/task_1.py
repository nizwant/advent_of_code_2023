with open("day_19/input.txt", "r") as f:
    data = f.readlines()


class Part:
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def __repr__(self):
        return f"x={self.x}, m={self.m}, a={self.a}, s={self.s}"


rules = {}
parts = []
was_empty_line = False
for line in data:
    line = line.strip()
    if not line:
        was_empty_line = True
        continue
    if not was_empty_line:
        key, val = line.split("{")
        val = val[:-1]
        val = val.split(",")
        rules[key] = val
    else:
        line = line[1:-1]
        line = line.split(",")
        tab = []
        for cat in line:
            cat = cat.split("=")[1]
            tab.append(int(cat))
        parts.append(Part(*tab))

answer = 0
for part in parts:
    start = "in"
    while start not in ["R", "A"]:
        workflow = rules[start]
        for rule in workflow:
            if ":" not in rule:
                start = rule
            else:
                rule, direction = rule.split(":")
                if rule[0] == "x":
                    val = part.x
                elif rule[0] == "m":
                    val = part.m
                elif rule[0] == "a":
                    val = part.a
                elif rule[0] == "s":
                    val = part.s

                if rule[1] == ">":
                    if val > int(rule[2:]):
                        start = direction
                        break
                elif rule[1] == "<":
                    if val < int(rule[2:]):
                        start = direction
                        break

    if start == "A":
        answer += part.x + part.m + part.a + part.s

print(answer)
