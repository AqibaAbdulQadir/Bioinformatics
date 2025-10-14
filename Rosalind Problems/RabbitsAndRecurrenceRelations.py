from functools import lru_cache

n, k = list(map(int, input().strip().split()))


@lru_cache(None)
def dp(i):
    if i >= n: return 0
    ans = 1
    for j in range(2, n):
        ans += k * dp(i+j)
    return ans


print(dp(0))
