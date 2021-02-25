import heapq
import sys

# 입력
V, E = map(int, input().split())
INF = 10 * V + 1  # 최댓값 설정
distance = [[] for _ in range(V + 1)]  # V*V배열로 만들면 메모리가 초과된다

for _ in range(E):
    start, end, dist = map(int, sys.stdin.readline().split())
    distance[start].append([end, dist])
    distance[end].append([start, dist])

K,F= map(int ,sys.stdin.readline().split())
# 다익스트라 알고리즘
queue = []  # 우선순위 큐 -> 힙으로 구현해줌
K_distance = [INF for _ in range(V + 1)]  # 답이 될 K로부터의 거리
K_distance[K] = 0  # 자기 자신은 0
heapq.heappush(queue, [0, K])  # 자기 자신으로부터 우선순위 큐를 시작한다
print(distance)
while queue:
    mid = heapq.heappop(queue)
    print(mid)
    for end in distance[mid[1]]:
        if K_distance[end[0]] > min(mid[0],end[0]) :
            K_distance[end[0]] = min(mid[0],end[0])
            heapq.heappush(queue, [K_distance[end[0]], end[0]])

for i in range(1, V + 1):
    if K_distance[i] == INF:
        print("INF")
    else:
        print(K_distance[i])