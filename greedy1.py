import time

v = [1, 5, 10, 50, 100, 500]
c = [3, 2, 1, 3, 0, 2]
A = 620

def solve(a):
    ans = 0
    for i in range(5, 0, -1):
        t = min(a // v[i], c[i])
        a -= t*v[i]
        ans += t
    print(ans)
    
start = time.perf_counter()
solve(A)
end = time.perf_counter()

print("time", end-start)