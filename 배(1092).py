import sys

n = int(sys.stdin.readline()) #크레인의 수
container_weight_limit = list(map(int, sys.stdin.readline().split())) #크레인들의 무게제한
m = int(sys.stdin.readline()) #박스의 수
box_weight = list(map(int, sys.stdin.readline().split())) #각 박스의 무게

#내림차순으로 정렬
container_weight_limit.sort(reverse=True)
box_weight.sort(reverse=True)

if container_weight_limit[0] < box_weight[0]:
    print(-1)
    exit()
else:
    time = 0
    while len(box_weight) > 0:
        time += 1
        for i in container_weight_limit:
            for j in range(len(box_weight)):
                if i >= box_weight[j]:
                    del box_weight[j]
                    break

print(time)
