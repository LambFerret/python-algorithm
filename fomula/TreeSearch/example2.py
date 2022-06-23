N, M, V = 4, 5, 1
graph1 = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]]
visited1 = [True, False, False, False, False]
gone = []
#
#
# def dfs(graph, loc, visited):
#     if not visited[loc]:
#         visited[loc] = True
#         gone.append(loc)
#     for i in graph:
#         if i[0] == loc:
#             dfs(graph, i[1], visited)
#
#
# dfs(graph1, V, visited1)
# print(gone)
from collections import deque


def bfs(graph, loc, visited):
    q = deque([loc])
    while q:
        v = q.popleft()
        visited[v] = True
        for i in graph:
            if i[0] == v:
                q.append(i[1])
                if all(visited):
                    print(visited)
                    return
        gone.append(v)
    print(gone)


bfs(graph1, V, visited1)
