def insertion_sort(list):
    for index in range(1, len(list)):
        val = list[index - 1]
        for check in range(index, 0, -1):
            if list[check] < list[check-1]:
                list[check], list[check - 1] = list[check - 1], list[check]
            else:
                break
    return list

print(insertion_sort([34,123,45,0,234,2,32,34,2]))
