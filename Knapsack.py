def bottom_up_knapsack(wt, val, limit):
    n = len(wt)
    table = [[0] * (limit + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for c in range(1, limit + 1):
            if wt[i - 1] <= c:
                take = val[i - 1] + table[i - 1][c - wt[i - 1]]
                skip = table[i - 1][c]
                table[i][c] = max(take, skip)
            else:
                table[i][c] = table[i - 1][c]

    chosen = []
    c = limit

    for i in range(n, 0, -1):
        if table[i][c] > table[i - 1][c]:
            chosen.append(i)
            c -= wt[i - 1]

    chosen.reverse()
    return table[n][limit], chosen


def top_down_knapsack(wt, val, limit):
    n = len(wt)
    memo = [[None] * (limit + 1) for _ in range(n + 1)]

    def solve(i, c):
        if i == 0 or c == 0:
            return 0

        if memo[i][c] is not None:
            return memo[i][c]

        if wt[i - 1] > c:
            memo[i][c] = solve(i - 1, c)
        else:
            take = val[i - 1] + solve(i - 1, c - wt[i - 1])
            skip = solve(i - 1, c)
            memo[i][c] = max(take, skip)

        return memo[i][c]

    result = solve(n, limit)
    chosen = []
    c = limit

    for i in range(n, 0, -1):
        if solve(i, c) != solve(i - 1, c):
            chosen.append(i)
            c -= wt[i - 1]

    chosen.reverse()
    return result, chosen


weights = [2, 1, 3, 2]
values = [12, 10, 20, 15]
capacity = 5

print("0/1 KNAPSACK PROBLEM")
print("====================")

for i in range(len(weights)):
    print("Item", i + 1, ": Weight =", weights[i], "Value =", values[i])

print("Capacity:", capacity)

value1, items1 = bottom_up_knapsack(weights, values, capacity)

print("\nBottom-Up Approach")
print("Maximum Value:", value1)
print("Selected Items:", items1)

value2, items2 = top_down_knapsack(weights, values, capacity)

print("\nTop-Down Approach")
print("Maximum Value:", value2)
print("Selected Items:", items2)