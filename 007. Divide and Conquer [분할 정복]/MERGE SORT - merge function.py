def merge(list1, list2):
    sorted_list = []
    mid1 = len(list1) // 2
    mid2 = len(list2) // 2

    if len(list1) < 1 or len(list2) < 1:
        return (list1 + list2)
            # 두 개의 리스트 중 하나라도 길이가 1 미만일 경우 단순병합 후 return

    
    if list1[0] > list2[0]:
        sorted_list.append(list2[0])
        return merge(list1, list2[:mid2])
    else:
        sorted_list.append(list1[0])
        return merge(list1[mid1:], list2)

    return sorted_list

# 테스트
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))
