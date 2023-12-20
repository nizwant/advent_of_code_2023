with open("day_20/input.txt", "r") as f:
    data = f.readlines()

# data = [
#     "broadcaster -> a, b, c",
#     "%a -> b",
#     "%b -> c",
#     "%c -> inv",
#     "&inv -> a",
# ]
# data = [
#     "broadcaster -> a",
#     "%a -> inv, con",
#     "&inv -> b",
#     "%b -> con",
#     "&con -> output",
# ]

dict_of_conjunctions = {}
for line in data:
    module_name, _ = line.strip().split(" -> ")
    if module_name[0] == "&":
        dict_of_conjunctions[module_name[1:]] = []

for line in data:
    module_name, module_neighbor = line.strip().split(" -> ")
    module_neighbor = module_neighbor.split(", ")
    for neighbor in module_neighbor:
        if neighbor in dict_of_conjunctions:
            dict_of_conjunctions[neighbor].append(module_name[1:])

modules = {}
for line in data:
    module_name, module_neighbor = line.strip().split(" -> ")
    module_neighbor = module_neighbor.split(", ")
    if module_name[0] == "%":
        module_state = "off"
        module_type = module_name[0]
        module_name = module_name[1:]
    elif module_name[0] == "&":
        module_state = {i: False for i in dict_of_conjunctions[module_name[1:]]}
        module_type = module_name[0]
        module_name = module_name[1:]
    else:
        module_state = "l"
        module_type = "broadcaster"
    modules[module_name] = [module_state, module_neighbor, module_type]

counter_h = 0
counter_l = 0

for _ in range(1000):
    counter_l += 1
    list_of_modules = [(i, "l", "broadcaster") for i in modules["broadcaster"][1]]
    while list_of_modules:
        module, signal_type, sender = list_of_modules.pop(0)
        if signal_type == "h":
            counter_h += 1
        else:
            counter_l += 1
        if module not in modules:
            continue
        module_state, module_neighbor, module_type = modules[module]
        if module_type == "%" and signal_type == "h":
            continue
        if module_type == "%" and signal_type == "l":
            if modules[module][0] == "off":
                modules[module][0] = "on"
                list_of_modules.extend([(i, "h", module) for i in module_neighbor])
            else:
                modules[module][0] = "off"
                list_of_modules.extend([(i, "l", module) for i in module_neighbor])
        if module_type == "&":
            if signal_type == "h":
                module_state[sender] = True
            else:
                module_state[sender] = False
            if all(module_state.values()):
                list_of_modules.extend([(i, "l", module) for i in module_neighbor])
            else:
                list_of_modules.extend([(i, "h", module) for i in module_neighbor])
            modules[module][0] = module_state
print(counter_h * counter_l)
