def recursive_func(i):
    if i == 10:
        return
    print(i, "start")
    recursive_func(i + 1)
    print(i, "end")


# recursive_func(0)

# ex.1 DFS
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]
]
visited = [False] * 9

# dfs(graph, 1, visited)

# ex.2 BFS
from collections import deque


def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


bfs(graph, 1, visited)
