''' 분할정복을 이용하여 합병정렬을 구현하는 코드 '''
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

# 테스트
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))

''' ------ 동작 설명 ------
1. 병합정렬을 수행하기 위한 파라미터로 list1, list2를 받는다.
2. 2개의 리스트 중 하나라도 길이가 1이거나 0인 경우는 단순 비교를 통해 순서대로 병합한다.
3. 그 외의 경우는 순서대로 각 리스트의 첫번째 인덱스끼리 비교하며 작은 요소를 sorted_list에 순서대로 삽입한다.
4. 만약 특정 리스트가 더 큰 수를 많이 가지고 있어 소진되지 않은 경우, 반복문에 사용한 변수를 활용하여 단순 병합한다.

 ------ 오래 고민한 이유 ------
 * 분할 정복 = 재귀함수 이용이라는 고정관념을 가지고 있었기 때문.
 
 이번 코드에서는 재귀를 전혀 이용하지 않고, 반복문만 사용했다.
 당연히 문제를 작은 단위로 나누는 해결법이니 재귀를 사용해야한다고 생각하고, 그렇게 코드를 작성했지만
 4번째 테스트문부터는 어떻게해도 정상 동작하지 않았다. 애초에 이 문제는 분할 정복이 아니라,
 분할 정복으로 병합 정렬을 수행하기 위해 함수하나를 작성하는 것이었다.
 
 오랜 고민끝에 반복문으로 방향을 전환한 뒤에도, 일부 소진되지 않은 요소들이 병합되지 않는 것을 해결하고자
 한참 애를 먹었는데, i와 j같은 반복문 변수를 사용하니 쉽게 해결할 수 있었다.'''
