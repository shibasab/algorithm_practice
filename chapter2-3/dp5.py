import time

n = 4
w = [2, 1, 3, 2]
v = [3, 2, 4, 2]
W = 5
dp = [[0] * (W + 1) for i in range(n + 1)]


def solve():
    for i in range(n):
        for j in range(W+1):
            for k in range(j//w[i]+1):
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-k*w[i]]+k*v[i])
    print(dp[n][W])


start = time.perf_counter()
solve()
end = time.perf_counter()
print("time", end-start)
