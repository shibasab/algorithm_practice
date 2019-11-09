import time

n = 4
m = 4
s = "abcd"
t = "becd"
dp = [[0] * (n + 1) for i in range(m + 1)]


def solve():
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    
    print(dp[n][m])
    
    
start = time.perf_counter()
solve()
end = time.perf_counter()
print("time", end-start)
