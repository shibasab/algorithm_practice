import time

N = 3
L = [8,5,8]


def solve(n):
    ans = 0
    while n > 1:
        mii1 = 0
        mii2 = 1
        if L[mii1] > L[mii2]:
            mii1, mii2 = mii2, mii1
        for i in range(2, n):
            if L[i] < L[mii1]:
                mii2 = mii1
                mii1 = i
            elif L[i] < L[mii2]:
                mii2 = i
        t = L[mii1] + L[mii2]
        ans += t
    
        if mii1 == n-1:
            mii1, mii2 = mii2, mii1
        L[mii1] = t
        L[mii2] = L[n-1]
        n -= 1
        
    print(ans)
    
    
start = time.perf_counter()
solve(N)
end = time.perf_counter()

print("time", end-start)
