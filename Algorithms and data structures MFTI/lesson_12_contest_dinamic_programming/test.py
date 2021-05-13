def make_exchange(money: int, coins: list):
    ways = [0] * (money + 1)
    ways[0] = 1
    for i in range(len(coins)):
        for j in range(len(ways)):
            if coins[i] <= j:
                ways[j] += ways[j-coins[i]]
    return ways[money]


print(make_exchange(1, [2,1]))