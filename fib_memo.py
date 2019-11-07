import time

n = 100
memo = [0]*(n)


def main():
    start = time.perf_counter()
    ans = fib_memo(n)
    end = time.perf_counter()

    print("time ", end - start)
    print(memo)
    print(ans)


def fib_memo(n):
    if n <= 1:
        return n
    if (memo[n-1] != 0):
        return memo[n-1]

    memo[n-1] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n-1]


if __name__ == '__main__':
    main()
