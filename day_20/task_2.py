import math
from functools import reduce

with open("day_20/input.txt", "r") as f:
    data = f.readlines()

# create "set" of conjunction modules
dict_of_conjunctions = {}
for line in data:
    module_name, _ = line.strip().split(" -> ")
    if module_name[0] == "&":
        dict_of_conjunctions[module_name[1:]] = []

# populate it with its input sources
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


counter = 0
set_of_cycles_length = set()
while True:
    counter += 1
    list_of_modules = [(i, "l", "broadcaster") for i in modules["broadcaster"][1]]
    while list_of_modules:
        module, signal_type, sender = list_of_modules.pop(0)

        if module not in modules:
            continue
        module_state, module_neighbor, module_type = modules[module]

        # if flip-flop
        if module_type == "%" and signal_type == "h":
            continue
        if module_type == "%" and signal_type == "l":
            if module_state == "off":
                module_state = "on"
                list_of_modules.extend([(i, "h", module) for i in module_neighbor])
            else:
                module_state = "off"
                list_of_modules.extend([(i, "l", module) for i in module_neighbor])

        # if conjunction
        if module_type == "&":
            if signal_type == "h":
                module_state[sender] = True
            else:
                module_state[sender] = False
            if all(module_state.values()):
                list_of_modules.extend([(i, "l", module) for i in module_neighbor])
            else:
                list_of_modules.extend([(i, "h", module) for i in module_neighbor])

        if len(set_of_cycles_length) == 4:
            smc = lambda x, y: abs(x * y) // math.gcd(x, y)
            print(reduce(smc, list(set_of_cycles_length)))
            exit()
        # update module state
        modules[module][0] = module_state
        if any(modules["zr"][0].values()):
            set_of_cycles_length.add(counter)
