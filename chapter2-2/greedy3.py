import time

S = "ACDBCB"
n = len(S)

def solve():
    ans = ""
    a = 0
    b = n-1
    while a <= b:
        left = False
        for i in range(b-a+1):
            if S[a+i] < S[b-i]:
                left = True
                break
            elif S[a+i] > S[b-i]:
                left = False
                break
        if left:
            ans += S[a]
            a += 1
        else:
            ans += S[b]
            b -= 1
    print(ans)
    
    
start = time.perf_counter()
solve()
end = time.perf_counter()

print("time", end-start)
