''' Quick Sort를 구현하기 위해 먼저 pivot을 지정하고 정렬해주는 partition 함수를 구현하는 코드 '''

def swap_elements(my_list, index1, index2):
    tmp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = tmp
    return my_list
        # list 내의 두 요소 위치를 바꾸어주는 함수

def partition(my_list, start, end):
    if start == end:
        return my_list

    i = b = start
        # start는 정렬을 시작할 index, b는 big 그룹의 시작 index, i는 unknown 그룹의 시작 index
    p = my_list[end]
        # 기준 p(pivot)에는 list의 가장 마지막 요소를 저장
    while i < len(my_list)-1:
        if p <= my_list[i]:
            i += 1
                # 기준 p보다 현재 위치의 요소값이 크다면, unknown 그룹의 index(i)만 1 증가
        elif p > my_list[i]:
            my_list = swap_elements(my_list, i, b)
            i += 1
            b += 1
                # 기준 p보다 현재 위치의 요소값이 작다면, unknown 그룹의 index(i)와 함께 big 그룹의 index(b)도 1 증가
                # 현재 index의 값과 big 그룹 1번 index의 값을 상호 교체

        if i == end:
            my_list = swap_elements(my_list, end, b)
            return b
            # unknown 그룹의 index가 마지막 index에 도달했다면, pivot의 위치를 big 그룹의 앞으로 옮겨주고, index 반환


# 테스트 1
#list1 = [4, 3, 6, 2, 7, 1, 5]
#pivot_index1 = partition(list1, 0, len(list1) - 1)
#print(list1)
#print(pivot_index1)


# 테스트 2
#list2 = [6, 1, 2, 6, 3, 5, 4]
#pivot_index2 = partition(list2, 0, len(list2) - 1)
#print(list2)
#print(pivot_index2)

''' ------ 동작 설명 ------
1. pivot 기준 정렬할 list, 탐색 범위의 시작과 끝 index를 파라미터로 받는다.
2. 리스트의 영역을 Unknown(i), Big(b), Small로 구분하며 순차적으로 비교해나간다.
3. 최초 실행 시 i, b는 start(시작 index)와 같다.
4. 가장 앞의 요소부터 pivot과 대소를 비교한다.
5. pivot < my_list[i] 일 경우에는 위치변경 없이, i index만 +1 증가시켜준다.
이렇게하면 방금 비교한 i번째 index는 자연스레 big 그룹에 속하게 된다.

6. 반대로 pivot > my_list[i]인 경우에는 우선 b가 가르키고 있는 big 그룹 첫번째 요소와
현 위치 i번째 요소를 서로 바꾸어준다. 이를 통해 i번째 요소가 big 그룹 앞으로 이동하게 되면,
해당 영역부터 small 그룹이 된다.

7. 리스트의 마지막까지 이를 반복하고, 최종적으로 pivot을 b index가 가르키는 곳으로 이동시킨다.

 ------ 오래걸린 이유 ------
 꽤 오랜시간 고민했던 문제였긴하지만, 힌트를 전혀 사용하지 않았다.
 앞서 고민했던 문제들에 비해 생소한 용어가 많았음에도 구상은 크게 어렵지 않았다.
 다만 오래걸린 이유는 내가 처음부터 문제를 잘못 이해하고 있었기 때문이다.
 
 문제에서는 재귀함수를 활용하지 않고, 최초 1회 실행을 통해
 우선적으로 pivot을 기준으로 정렬하는 코드를 작성하라고 했는데
 나는 그 의도를 오해하고 재귀함수를 사용하여 결과를 도출해려고 쩔쩔맸었다..'''
