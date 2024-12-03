import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from utils.get_inputs import ProblemParser


lines = ProblemParser().load_input(2021, 15)
nums = [[] for _ in range(len(lines))]
for i, line in enumerate(lines):
    for c in line:
        nums[i].append(int(c))


def part1():
    dp = [[0 for _ in range(len(nums[0]))] for _ in range(len(nums))]
    for i in range(len(nums[0])):
        for j in range(len(nums)):
            if i == 0 and j == 0:
                dp[i][j] = 0
            elif i - 1 > 0 and j - 1 > 0:
                dp[i][j] = nums[i][j] + min(dp[i - 1][j], dp[i][j - 1])
            elif i - 1 > 0:
                dp[i][j] = nums[i][j] + dp[i - 1][j]
            else:
                dp[i][j] = nums[i][j] + dp[i][j - 1]

    print(dp[len(nums[0]) - 1][len(nums) - 1] - nums[0][0])


def expand_grid(g, n):
    expanded = []
    for bump in range(n * 2):
        temp = [[0 for _ in range(len(g[0]))] for _ in range(len(g))]
        for i in range(len(g[0])):
            for j in range(len(g)):
                val = g[i][j] + (bump + 1)
                if val >= 10:
                    val = val - 10 + 1
                temp[i][j] = val
        expanded.append(temp)
    app = []
    for i in range(n):
        for j in range(len(g)):
            g[j].extend(expanded[i][j])
    for i in range(n):
        curr = expanded[i : i + n + 1]
        temp = curr[0]
        for i in range(1, n + 1):
            for j in range(len(temp)):
                temp[j].extend(curr[i][j])
        app.append(temp)
    print(app)
    for a in app:
        g.extend(a)
    return g


def part2():
    expand_grid(nums, 4)
    for num in nums:
        print(num)
    dp = [[0 for _ in range(len(nums[0]))] for _ in range(len(nums))]
    for i in range(len(nums[0])):
        for j in range(len(nums)):
            if i == 0 and j == 0:
                dp[i][j] = 0
            elif i - 1 > 0 and j - 1 > 0:
                dp[i][j] = nums[i][j] + min(dp[i - 1][j], dp[i][j - 1])
            elif i - 1 > 0:
                dp[i][j] = nums[i][j] + dp[i - 1][j]
            else:
                dp[i][j] = nums[i][j] + dp[i][j - 1]

    print(dp[len(nums[0]) - 1][len(nums) - 1] - nums[0][0])


part1()
part2()
