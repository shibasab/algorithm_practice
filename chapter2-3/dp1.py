import time

n = 4
w = [2, 1, 3, 2]
v = [3, 2, 4, 2]
W = 5


def rec(i, j):
    res = 0
    if i == n:
        # 品物は残っていない
        res = 0
    elif j < w[i]:
        # この品物は入らない
        res = rec(i+1, j)
    else:
        # 入れない場合と入れる場合を試す
        res = max(rec(i+1, j), rec(i+1, j-w[i])+v[i])
    
    return res


start = time.perf_counter()
print(rec(0, W))
end = time.perf_counter()
print("time", end-start)
