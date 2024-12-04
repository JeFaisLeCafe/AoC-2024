f = open("input.txt", "r")
lines = f.readlines()
lines = [line.strip() for line in lines]
chars = []
for line in lines:
    chars.append(list(line))

# chars is now a list of lists, each list is a line

# ..X...
# .SAMX.
# .A..A.
# XMAS.S
# .X....

# we need to find the word "xmas" in the grid
# we can move in all 8 directions


# part 1
def has_xmas_word(x, y, chars):
    word = "XMAS"
    # multiple XMAS can be found from the same starting point
    count = 0
    # up
    if x - len(word) >= -1:
        found = True
        for i in range(len(word)):
            if chars[x - i][y] != word[i]:
                found = False
                break
        if found:
            count += 1
    # down
    if x + len(word) <= len(chars):
        found = True
        for i in range(len(word)):
            if chars[x + i][y] != word[i]:
                found = False
                break
        if found:
            count += 1

    # left
    if y - len(word) >= -1:
        found = True
        for i in range(len(word)):
            if chars[x][y - i] != word[i]:
                found = False
                break
        if found:
            count += 1

    # right
    if y + len(word) <= len(chars[0]):
        found = True
        for i in range(len(word)):
            if chars[x][y + i] != word[i]:
                found = False
                break
        if found:
            count += 1

    # up left
    if x - len(word) >= -1 and y - len(word) >= -1:
        found = True
        for i in range(len(word)):
            if chars[x - i][y - i] != word[i]:
                found = False
                break
        if found:
            count += 1

    # up right
    if x - len(word) >= -1 and y + len(word) <= len(chars[0]):
        found = True
        for i in range(len(word)):
            if chars[x - i][y + i] != word[i]:
                found = False
                break
        if found:
            count += 1

    # down left
    if x + len(word) <= len(chars) and y - len(word) >= -1:
        found = True
        for i in range(len(word)):
            if chars[x + i][y - i] != word[i]:
                found = False
                break
        if found:
            count += 1

    # down right
    if x + len(word) <= len(chars) and y + len(word) <= len(chars[0]):
        found = True
        for i in range(len(word)):
            if chars[x + i][y + i] != word[i]:
                found = False
                break
        if found:
            count += 1

    return count


def part1():
    # count the number of times we see the word "xmas" in the grid
    res = 0
    for i in range(len(chars)):
        for j in range(len(chars[0])):
            print(i, j, chars[i][j])
            if chars[i][j] == "X":
                print("found X", i, j, has_xmas_word(i, j, chars))
                res += has_xmas_word(i, j, chars)
    return res


print(part1())  #
