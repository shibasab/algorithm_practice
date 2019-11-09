import time

n = 4
w = [2, 1, 3, 2]
v = [3, 2, 4, 2]
W = 5
dp = [[0] * (n*max(v)+1) for i in range(n + 1)]


def solve():
    for i in range(1, n * max(v) + 1):
        dp[0][i] = 10 ** 10
    dp[0][0] = 0
    for i in range(n):
        for j in range(n*max(v)+1):
            if j < v[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = min(dp[i][j], dp[i][j-v[i]]+w[i])
    res = 0
    for i in range(n*max(v)+1):
        if dp[n][i] <= W:
            res = i
    print(res)
    
    
start = time.perf_counter()
solve()
end = time.perf_counter()
print("time", end-start)
