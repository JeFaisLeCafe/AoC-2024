f = open("input.txt", "r")
lines = f.readlines()
lines = [line.strip() for line in lines]


# part 1


def isLineSafe(line):
    # line = '1 14 44 32' for example
    parts = line.split()
    # line is safe if the numbers are :
    # - all increasing or decreasing, stricly
    # - the difference between two consecutives numbers is <= 3

    # convert the parts to integers
    parts = [int(part) for part in parts]
    isIncreasing = True
    isDecreasing = True
    for i in range(1, len(parts)):
        if parts[i] > parts[i - 1]:
            isDecreasing = False
        elif parts[i] < parts[i - 1]:
            isIncreasing = False

    if not isIncreasing and not isDecreasing:
        return False

    if isIncreasing and isDecreasing:
        return False

    if isIncreasing:
        for i in range(1, len(parts)):
            if parts[i] - parts[i - 1] > 3 or parts[i] - parts[i - 1] < 1:
                return False
    elif isDecreasing:
        for i in range(1, len(parts)):
            if parts[i - 1] - parts[i] > 3 or parts[i - 1] - parts[i] < 1:
                return False

    return True


def part1():
    safe_lines = 0
    for line in lines:
        if isLineSafe(line):
            safe_lines += 1
    return safe_lines


print(part1())  # 230


def part2():
    # now, in addition, if a line is unsafe, we need to:
    # - try if we can make it safe by removing one number
    # - if we can, then it is safe
    # - if we can't, then it is unsafe

    # we can remove a number if the difference between the two numbers around it is <= 3
    # for example, if we have 1 4 5 6 9, we can remove 5 to get 1 4 6 9
    # if we have 1 4 5 6 9 10, we can remove 5 or 6 to get 1 4 6 9 10

    safe_lines = 0
    for line in lines:
        if isLineSafe(line):
            safe_lines += 1
        else:
            parts = line.split()
            parts = [int(part) for part in parts]
            # create an array of all the possible lines we can get by removing one number
            possible_lines = []
            for i in range(len(parts)):
                new_parts = parts.copy()
                new_parts.pop(i)
                possible_lines.append(new_parts)
            for possible_line in possible_lines:
                if isLineSafe(" ".join([str(part) for part in possible_line])):
                    safe_lines += 1
                    break
    return safe_lines


print(part2())  # 301
