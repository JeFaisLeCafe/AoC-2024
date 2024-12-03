f = open("input.txt", "r")
lines = f.readlines()
lines = [line.strip() for line in lines]

# part 1
# We need to find all occurences of exactly `mul(X,Y)` where X and Y are numbers between 0 and 999
# Add each pair to a list


def findMul(line):
    # example line: xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
    # expected output: [[2, 4], [5,5], [11, 8], [8, 5]]

    # find all occurences of mul(X,Y)
    mul_occurences = []
    i = 0
    while i < len(line):
        if (
            line[i] == "m"
            and line[i + 1] == "u"
            and line[i + 2] == "l"
            and line[i + 3] == "("
        ):
            i += 4
            j = i
            x = ""
            while line[i].isdigit() and i < j + 3:
                x += line[i]
                i += 1
            if line[i] != ",":
                continue
            i += 1
            j = i
            y = ""
            while line[i].isdigit() and i < j + 3:
                y += line[i]
                i += 1
            if line[i] != ")":
                continue
            mul_occurences.append([int(x), int(y)])
        i += 1

    return mul_occurences


def part1():
    mul_occurences = []
    for line in lines:
        mul_occurences += findMul(line)
    # for each pair, multiply the two numbers and add it to the result
    res = 0
    for pair in mul_occurences:
        res += pair[0] * pair[1]

    return res


# print(part1())  # 174561379

# part 2


def find_enabled_mul(line):
    # in addition to find_mul, we need to check if the mul is enabled
    # by default, mul is enabled
    # if there is a `don't()` instruction, all muls after it are disabled, until the next `do()` instruction, which enables them again

    # example line: xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
    # expected output: [[2, 4], [8, 5]]

    is_enabled = True
    mul_occurences = []
    i = 0
    while i < len(line):
        if line[i : i + 7] == "don't()":
            is_enabled = False
            print("disabled")
            i += 7
            continue

        if (
            line[i] == "d"
            and line[i + 1] == "o"
            and line[i + 2] == "("
            and line[i + 3] == ")"
        ):
            print("enabled")
            is_enabled = True
            i += 4
            continue

        if is_enabled == False:
            i += 1
            continue

        if (
            is_enabled == True
            and line[i] == "m"
            and line[i + 1] == "u"
            and line[i + 2] == "l"
            and line[i + 3] == "("
        ):
            i += 4
            j = i
            x = ""
            while line[i].isdigit() and i < j + 3:
                x += line[i]
                i += 1
            if line[i] != ",":
                continue
            i += 1
            j = i
            y = ""
            while line[i].isdigit() and i < j + 3:
                y += line[i]
                i += 1
            if line[i] != ")":
                continue
            mul_occurences.append([int(x), int(y)])
            print("enabled mul", x, y)
        i += 1

    return mul_occurences


def part2():
    mul_occurences = []
    for line in lines:
        mul_occurences += find_enabled_mul(line)
    print(mul_occurences)
    # for each pair, multiply the two numbers and add it to the result
    res = 0
    for pair in mul_occurences:
        res += pair[0] * pair[1]

    return res


print(part2())  # 106921067
