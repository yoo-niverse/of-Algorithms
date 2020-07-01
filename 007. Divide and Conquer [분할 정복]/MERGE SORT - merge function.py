def merge(list1, list2):
    sorted_list = []
    i = j = 0

    if len(list1) <= 1 or len(list2) <= 1:
        if list1 > list2:
            sorted_list.append(list2 + list1)
            return sorted_list
        else:
            sorted_list.append(list1 + list2)
            return sorted_list

    print(f'list1 = {list1[0]}, list2= {list2[0]}')

    while (i < len(list1)) and (j < len(list2)):
        if list1[i] < list2[j]:
           sorted_list.append(list1[i])
           i += 1
        else:
           sorted_list.append(list2[j])
           j += 1


    # 재귀호출 하는 과정 속에서 마지막 값만 맨위 조건문에서 붙고 나머지는 소멸
    # 두개의 리스트 중 하나라도 len이 1이 될때까지 반복하고, 1이 되면 걍 붙어버려서

    return sorted_list

# 테스트
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))

#아니 쉬발 반복문을 써야한다고? 재귀를 안써도 된다고?
