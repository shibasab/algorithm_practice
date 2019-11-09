import time

n = int(input())
a = list(map(int, input().split()))
k = int(input())


def dfs(i, summ):
    if i == n:
        return summ == k
    if (dfs(i + 1, summ)):
        return True
    if (dfs(i + 1, summ + a[i])):
        return True
    return False


start = time.perf_counter()
if (dfs(0, 0)):
    print("Yes")
else:
    print("No")
end = time.perf_counter()

print("time", end-start)
