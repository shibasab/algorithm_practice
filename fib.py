import time


def main():
    start = time.perf_counter()
    ans = fib(35)
    end = time.perf_counter()

    print("time ", end - start)
    print(ans)


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    main()
