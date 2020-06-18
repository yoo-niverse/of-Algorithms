def binary_search(element, some_list):
    start_index = 0
        # 이진탐색 최초 수행 시 list의 시작 index는 0
    end_index = len(some_list)-1
        # 마찬가지로 최초 수행시 마지막 index는 (list의 길이-1)

    for i in range(start_index, end_index):
            # 첫 인덱스부터 마지막 인덱스까지 반복문 수행
        mid = (start_index + end_index) // 2
            # 이진탐색 수행을 위한 중간값은 항상 (시작 인덱스 + 끝 인덱스)의 절반
        if some_list[mid] == element:
            return mid
            # 만약 list의 중간값 index 값이 찾고자하는 element값과 같다면 그대로 해당 index return
        elif some_list[mid] > element:
            end_index = (mid-1)
            # 중간값이 찾고자하는 값보다 큰 경우 탐색 범위 제한(0번 인덱스부터 기존 중간값 바로 이전 인덱스까지 탐색)

        elif some_list[mid] < element:
            start_index = (mid +1)
            # 중간값이 찾고자 하는 값보다 작은 경우 탐색 범위 제한(중간값 다음 인덱스부터 마지막 인덱스까지)


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))

''' ------ 동작 설명 ------
1. 찾고자하는 값(element)와 찾을 대상이 되는 리스트(some_list)를 파라미터로 전달받는다.
2. 최초 수행 시 시작 인덱스는 0으로, 끝 인덱스는 리스트의 마지막 인덱스로 설정한다.
3. 시작부터 끝 인덱스까지의 반복문을 통해 찾는 값과 매 시점 중간값의 일치, 대소를 판별한다.
4. 중간값과 찾는 값이 동일한 경우 해당 중간값의 index를 return한다.

 ------ 오래걸린 이유 ------
 기본 개념 문제치고 상당히 오래걸린 문제였다. 이진탐색의 개념은 정확히 이해했지만
 막상 코드로 구현하려고하니 어려웠다. 중간값을 찾고, 그 중간값을 갱신하며 리스트의 탐색범위를 제한한다는 것은
 처음부터 생각했지만 그걸 코드로 작성해내는게 너무 어려웠다.
 
 처음에는 element가 some_list[mid]보다 크거나 작을 경우 slicing을 통해
 리스트의 범위를 한정지으려고 했는데, 계속 오류가 발생했다.
 이 방법 외에도 재귀호출을 적용해보려고 했지만 반복 재귀호출 오류로 인해 작동되지 않았다.
 
 결국 하루가 넘게 고민한 끝에 힌트를 하나 열었고, start_index와 end_index 변수를 적용하게 됐다.
 그렇게 적용한 결과 오류가 발생하진 않았지만 코드가 정상동작하지는 않았다.
 한참 이유를 찾다보니 mid를 갱신해주는 부분을 반복문내부에 넣지 않아 제대로된 결과가 출력되지 않은 것이었다.
 상당히 어려웠지만 그래도 나름의 고민을 통해 보람있게 문제를 해결할 수 있어서 다행이다.'''
