#1504 - 특정한 최단 경로(Gold 4)

import sys
import heapq

def dijkstra(node):
    distance = [INF] * (n + 1)
    distance[node] = 0

    q = []
    heapq.heappush(q, (0, node))

    while q:
        dist, pre = heapq.heappop(q)

        if distance[pre] < dist:
            continue

        for i in graph[pre]:
            if distance[i[0]] > dist + i[1]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))

    return distance

n, e = map(int, sys.stdin.readline().split())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    i, j, cost = map(int, sys.stdin.readline().split())
    graph[i].append((j, cost))
    graph[j].append((i, cost))

v1, v2 = map(int, sys.stdin.readline().split())

path1 = dijkstra(1)[v1] + dijkstra(v1)[v2] + dijkstra(v2)[n]
path2 = dijkstra(1)[v2] + dijkstra(v2)[v1] + dijkstra(v1)[n]
result = min(path1, path2)

if result < INF:
    print(result)
else:
    print(-1)