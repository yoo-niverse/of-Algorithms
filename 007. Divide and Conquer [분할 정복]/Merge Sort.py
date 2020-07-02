def merge(list1, list2):
    sorted_list = []
        # list1, list2를 이용하여 정렬된 요소를 저장할 새로운 통합 list
    i = j = 0
        # 반복문에 사용할 list1, list2의 index

    if len(list1) <= 1 or len(list2) <= 1:
        if list1 > list2:
            return list2 + list1
        else:
            return list1 + list2
            # 2개의 list 중 하나라도 그 길이가 1보다 짧거나 같은 경우에는 둘의 단순비교를 통해 순서를 결정

    while (i < len(list1)) and (j < len(list2)):
        # i 그리고 j가 list1, list2의 길이보다 작은 동안 반복 수행
        if list1[i] < list2[j]:
            if list1[i] in sorted_list:
                continue

            else:
                sorted_list.append(list1[i])
                i += 1
            # list2의 요소가 더 크다면, list1의 요소를 sorted_list에 삽입하고, list1의 다음 index와 비교한다.
        else:
            if list2[j] in sorted_list:
                continue

            else:
                sorted_list.append(list2[j])
                j += 1
            # list1의 요소가 더 크다면, list2의 요소를 sorted_list에 삽입하고, list2의 다음 index와 비교한다.

    if i == len(list1):
        sorted_list += list2[j:]
    elif j == len(list2):
        sorted_list += list1[i:]
            # i(j)가 list1(list2)의 길이와 같아졌다는 의미는 list1을 모두 소진했다는 의미
            # 그 경우에는 아직 소진되지 않은 list2(list1)의 요소가 있으면 j(i)번째 index부터 단순 병합

    return sorted_list

# 합병 정렬
def merge_sort(my_list):

    if len(my_list) <= 1:
        return my_list

        # 메인 함수의 역할은 '분할'
    #if len(my_list) == 2:
     #   return merge(my_list[0:0], my_list[1:1]) # my_list의 길이가 2가되면 각 요소를 전달

    mid = len(my_list) // 2
    part1 = part2 = []
    for i in range(0, len(my_list[:mid])-1):
        for j in my_list[:mid]:
            if my_list[i] > j:
                continue
            else:
                part1.append(my_list[i])
    print(part1)




    # if문 써서 원소가 하나면 merge로 넘길까? pt1 끝내고 pt2 넘길까?

    #return merge(part1, part2)

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
