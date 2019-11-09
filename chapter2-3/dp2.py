import time

n = 4
w = [2, 1, 3, 2]
v = [3, 2, 4, 2]
W = 5
dp = [[-1]*(W+1) for i in range(n+1)]


def rec(i, j):
    if dp[i][j] >= 0:
        return dp[i][j]
    res = 0
    if i == n:
        res = 0
    elif j < w[i]:
        res = rec(i+1, j)
    else:
        res = max(rec(i+1, j), rec(i+1, j-w[i])+v[i])
    
    dp[i][j] = res
    return dp[i][j]


start = time.perf_counter()
print(rec(0, W))
end = time.perf_counter()
print("time", end-start)
