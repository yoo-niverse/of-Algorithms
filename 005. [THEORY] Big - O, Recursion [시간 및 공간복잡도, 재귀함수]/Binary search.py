''' 이진탐색을 재귀함수로 구현하는 코드'''
def binary_search(element, some_list, start_index=0, end_index=None):
    if end_index == None:
        end_index = len(some_list)-1
        # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스 저장

    mid = (start_index + end_index) // 2
        # ★ 가장 큰 실수가 있었던 부분.. 덧셈 연산부분에서 괄호로 연산의 우선순위를 지정해주지 않았다.

    if some_list[mid] == element:
        return mid
        # 중간값이 찾고자 하는 요소와 일치하는 경우 중간값 index를 반환하고 종료

    if some_list[start_index] > element or some_list[end_index] < element:
        return None
        # 시작 index가 찾는 값보다 크거나, 마지막 index가 찾는 값보다 작을 경우 대상이 리스트에 있을 수 없다.

    if some_list[mid] > element:
        return binary_search(element, some_list, 0, mid-1)
        # 중간값이 찾고자하는 값보다 큰 경우 재귀호출을 통해 마지막 index를 중간값 바로 앞 index로 변경

    if some_list[mid] < element:
        return binary_search(element, some_list, mid+1, end_index)
        # 중간값이 찾고자하는 값보다 작은 경우 재귀호출을 통해 시작 index를 중간값 바로 다음 index로 변경

    # return을 안써줘서 다 None 나옴. 반환을 안해주니까 넌이지 없는 넌이 아니고

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
print(binary_search(34, [3, 6, 18, 20, 23, 34, 59, 63]))

''' ------ 동작 설명 ------
1. 찾을 값, 탐색할 리스트, 시작 index, 마지막 index를 파라미터로 받는다.
2. 중간값과 찾을 값의 대소비교에 따라 재귀호출 또는 return 통해 index를 반환한다.
3. 찾는 값이 없을 경우에는 None을 반환한다.

 ------ 시간이 매우 오래 걸린 이유 ------
 
 이진탐색의 개념은 간단했기에 case를 BASE와 RECURSIVE로 나누어 생각하는데는 어려움이 없었다.
 그러나 첫번째 실수는 BASE CASE가 [1개만] 있을 것이라고 생각한 것이었다.
 당연히 중간값 == 찾는 값일 경우만 BASE가 될 줄 알았는데, 찾는 값이 없는 경우도 BASE에 포함이 되었다.
 없는 경우를 판별하는 if 조건문을 작성하는 것은 간단했다. 하지만 나중에 답안을 보니 start_index > end_index의 꼴로
 더 간단하게 작성할 수도 있었다.
 
 RECURSIVE CASE를 작성하며, 치명적인 실수를 했다. 
 예시 상황에서 5, 6번째는 중간값 < 찾는 값의 경우인데, 이 부분에서 계속 오류가 발생했다.
 if some_list[mid] < element: 이하의 부분이 뭔가 잘못됐기에 그렇다는 것인데
 무엇이 오류인지 계속 생각해보고, 손으로 직접 그려보며 답을 찾고자 했지만 찾을 수 없었다.
 
 한참 고민하며 힌트를 봐도 이미 나는 해결한 내용에 대한 이야기들 밖에 없었다.
 알고보니 mid를 계산하는 과정에서 mid = start_index + end_index // 2로 작성을 했었다..
 덧셈 연산에 괄호를 사용하여 연산의 우선순위를 부여했어야 했는데 그렇게 하지 않아서 잘못된 결과가 나오고 있었던 것이다.
 
 IndexError가 나는 이유를 알 수없었는데 그래서였다.
 이틀동안 고민해도 해결되지 않았던 원인이 이렇게 간단하고 어이없는 실수때문이었다니 허망하고,
 몇번이나 코드를 적동하면서도 발견하지못한 내 자신이 수치스러웠다. 앞으로는 꼼꼼히 더 자세히 볼 수 있도록 노력해야겠다.'''
