@cache
def num_coin_sums(N, coins):
    if N < 0: return 0
    if N == 0: return 1
    if len(coins) == 0: return 0
    return num_coin_sums(N - coins[0], coins) + num_coin_sums(N, tuple(coins[1:]))


