def linear_search(element, some_list):
    for i in range(0, len(some_list)):
        if element == some_list[i]:
            return i
                # 찾고자하는 값과 i번째 요소의 값이 같다면 인덱스 return

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))

''' ------ 동작 설명 ------
1. 찾고자 하는 값과 탐색의 대상이 되는 리스트를 파라미터로 전달받는다.
2. 0번 index부터 (some_list의 길이 -1) 인덱스까지 반복문을 수행한다.
3. 찾고자 하는 값과 i번째 요소의 값이 같다면 index를 return한다.

제시된 문제에서 element in some_list 등의 조건을 사용하지 말라고 하였기때문에,
선형탐색의 정의 그대로 0번부터 마지막 index까지 순차적으로 탐색하는 코드를 작성하였다.'''
