list = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(0, len(list) - 1):
    min_index = i
    for j in range(i + 1, len(list)):
        if list[min_index] > list[j]:
            min_index = j
    list[i], list[min_index] = list[min_index] , list[i]
    print(list)

