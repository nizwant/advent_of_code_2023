with open("day_16/input.txt", "r") as f:
    data = f.readlines()

matrix = []
for line in data:
    line = line.strip()
    line = list(line)
    matrix.append(line)

zeros = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
queue_of_rays = [((-1, 0), (1, 0))]
visited_directions = {}
while queue_of_rays:
    position, velocity = queue_of_rays.pop()
    new_position = (position[0] + velocity[0], position[1] + velocity[1])

    if new_position[0] < 0 or new_position[0] >= len(matrix):
        continue
    if new_position[1] < 0 or new_position[1] >= len(matrix[0]):
        continue
    if new_position in visited_directions:
        if velocity in visited_directions[new_position]:
            continue
        else:
            visited_directions[new_position].append(velocity)
    else:
        visited_directions[new_position] = [velocity]
    zeros[new_position[1]][new_position[0]] = 1

    # if .
    if matrix[new_position[1]][new_position[0]] == ".":
        queue_of_rays.append((new_position, velocity))

    # if |
    if matrix[new_position[1]][new_position[0]] == "|":
        if velocity[0] == 0:
            queue_of_rays.append((new_position, velocity))
        else:
            queue_of_rays.append((new_position, (0, -1)))
            queue_of_rays.append((new_position, (0, 1)))

    # if -
    if matrix[new_position[1]][new_position[0]] == "-":
        if velocity[1] == 0:
            queue_of_rays.append((new_position, velocity))
        else:
            queue_of_rays.append((new_position, (-1, 0)))
            queue_of_rays.append((new_position, (1, 0)))

    # if /
    if matrix[new_position[1]][new_position[0]] == "/":
        if velocity[0] == 0:
            queue_of_rays.append((new_position, (-velocity[1], 0)))
        else:
            queue_of_rays.append((new_position, (0, -velocity[0])))

    # if \
    if matrix[new_position[1]][new_position[0]] == "\\":
        if velocity[0] == 0:
            queue_of_rays.append((new_position, (velocity[1], 0)))
        else:
            queue_of_rays.append((new_position, (0, velocity[0])))

answer = 0
for line in zeros:
    answer += sum(line)

print(answer)
