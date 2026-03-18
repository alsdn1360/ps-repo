import heapq, sys

input = sys.stdin.readline


# main
n = int(input())

classes = []

for _ in range(n):
    s, t = map(int, input().split())
    classes.append((s, t))

classes.sort()

class_room = []

for s, t in classes:
    if not class_room or s < class_room[0]:
        heapq.heappush(class_room, t)
        continue

    if s >= class_room[0]:
        heapq.heappop(class_room)
        heapq.heappush(class_room, t)

print(len(class_room))
