import time

n = 5
S = [1, 2, 4, 6, 8]
T = [3, 5, 7, 9, 10]
itv = []


def solve():
    ans = 0
    for i in range(n):
        itv.append([T[i], S[i]])
    itv.sort()
    ans = 0
    t = 0
    for i in range(n):
        if t < itv[i][1]:
            ans += 1
            t = itv[i][0]
    print(ans)
    
    
start = time.perf_counter()
solve()
end = time.perf_counter()

print("time", end-start)
