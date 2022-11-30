# from itertools import permutations

# # Brute Force
# n, t = map(int, input().split())
# count = 0
# for perm in permutations(range(1, n + 1)):
#     if count == t:
#         break
#     if all((index + 1) != value for index, value in enumerate(perm)):
#         print(*perm)
#         count += 1


# Using Generator
def get_next_derangement(lst):
    queue = [-1]
    lenlst = len(lst)
    while queue:
        i = queue[-1] + 1
        if i == lenlst:
            queue.pop()
        elif i not in queue and i != len(queue)-1:
            queue[-1] = i
            if len(queue) == lenlst:
                yield [lst[x] for x in queue]
            queue.append(-1)
        else:
            queue[-1] = i


n, t = map(int, input().split())
count = 0
for perm in get_next_derangement(range(1, n + 1)):
    if count == t:
        break
    print(*perm)
    count += 1