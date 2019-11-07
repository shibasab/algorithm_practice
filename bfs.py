import time
import queue

inf = 10**10
n = 10
m = 10
maze = [['#', 'S', '#', '#', '#', '#', '#', '#', '.', '#'],
        ['.', '.', '.', '.', '.', '.', '.', '#', '.', '#'],
        ['.', '#', '.', '#', '#', '.', '#', '#', '.', '#'],
        ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['#', '#', '.', '#', '#', '.', '#', '#', '#', '#'],
        ['.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
        ['.', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
        ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
        ['.', '#', '#', '#', '#', '.', '#', '#', '#', '.'],
        ['.', '.', '.', '.', '#', '.', '.', '.', 'G', '#']]

d = [[0] * n for _ in range(m)]
s = [0, 1]  # スタート地点の座標
g = [9, 8]  # ゴールの座標
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    q = queue.Queue()
    for i in range(n):
        for j in range(m):
            d[i][j] = inf
    q.put([s[0], s[1]])
    d[s[0]][s[1]] = 0
    while not q.empty():
        p = q.get()
        if (p[0] == g[0] and p[1] == g[1]):
            break
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            if (nx >= 0 and nx < n and ny >= 0 and ny < m):
                if (maze[nx][ny] != "#" and d[nx][ny] == inf):
                    q.put([nx, ny])
                    d[nx][ny] = d[p[0]][p[1]] + 1
    return d[g[0]][g[1]]


def solve():
    start = time.perf_counter()
    res = bfs()
    end = time.perf_counter()
    print(res)
    print("time", end-start)


solve()
