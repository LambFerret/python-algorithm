from collections import deque

graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
]


def ICE_bfs(graph, loc):
    if graph[loc[0]][loc[1]] == 1:
        return 0

    q = deque([graph[loc[0]][loc[1]]])
    print(graph[loc[0]][loc[1]])
    while q:
        v = q.popleft()
        print(v, end=' -> ')
        for i in graph[v]:
            if graph[v] == 0:
                q.append(i)
                graph[i] = 1
    return 1

count = 0
for a in range(4):
    for b in range(5):
        count += ICE_bfs(graph, [a,b])

print(count)
