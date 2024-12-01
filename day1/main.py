f = open("input.txt", "r")
lines = f.readlines()
# lines = ['1721 923\n', '979 366\n']

# part 1
data = [[], []]
for line in lines:
    a, b = line.strip().split()
    data[0].append(int(a))
    data[1].append(int(b))

# # sort data[0] and data[1]
# data[0].sort()
# data[1].sort()

# diff = []

# # for each pair, compute and save their difference

# for i in range(len(lines)):
#     diff.append(abs(data[0][i] - data[1][i]))

# sum = sum(diff)
# print(sum)
# # 1660292


# part 2
def similarity_score(a: int, b: list[int]) -> int:
    score = 0
    for i in range(len(b)):
        # score is equal to the number of times a appears in b, times a
        if a == b[i]:
            score += a
    return score


# for each element in data[0], compute the similarity score with data[1]
scores = []
for i in range(len(data[0])):
    scores.append(similarity_score(data[0][i], data[1]))

sum = sum(scores)
print(sum)
# 22776016
