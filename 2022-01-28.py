#버블정렬
# list = [3,2,5,7,1]
# n = len(list)
# for i in range(n -1):
#     for j in range(n - 1 -i):
#         if list[j] > list[j+1]:
#             list[j], list[j+1] = list[j+1], list[j]
    
# print(list)

#삽입정렬
list = [3, 2, 5, 7, 1]
n = len(list)
for i in range(1, n):
    for j in range(i, 0, -1):
        if list[j -1] > list[j]:
            list[j-1], list[j] = list[j], list[j-1]

print(list)

#병합정렬
list = [3, 2, 5, 7, 1]

def merge_sort(list):
    if len(list) < 2:
        return list
    mid = len(list) // 2
    low_list = merge_sort(list[:mid])
    high_list = merge_sort(list[mid:])

    merged_list = []
    l = h = 0
    while l < len(low_list) and h < len(high_list):
        if low_list[l] < high_list[h]:
            merged_list.append(low_list[l])
            l += 1
        else:
            merged_list.append(high_list[h])
            h += 1

    merged_list += low_list[l:]
    merged_list += high_list[h:]
    return merged_list

list = merge_sort(list)
print(list)
