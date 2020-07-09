from Partition_of_Quick_Sort import partition

def quicksort(my_list, start, end):
    pivot = partition(my_list, start, end)
    if pivot == start:
        return my_list
    if my_list[pivot] == start:
        my_list = quicksort(my_list, pivot+1, end)
    elif my_list[pivot] == end:
        my_list = quicksort(my_list, start, pivot-1)
    else:
        my_list = quicksort(my_list, pivot+1, end)
        my_list = quicksort(my_list, start, pivot-1)


# 원본 리스트가 바뀌질 않는데?



# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)

''' my_list[i] == p의 경우에 분기가 없어서 무한반복 걸림'''
