''' 파티션 함수를 이용하여 Quicksort 구현하는 코드 '''
from Partition_of_Quick_Sort import partition
    # 파티션 함수를 작성한 모듈을 import
def quicksort(my_list, start, end):
    if start < end:
        # 정렬을 시작하는 index가 마지막 index보다 큰 경우 명령을 수행하지 않음
        pivot = partition(my_list, start, end)
            # partition 함수의 실행결과를 통해 pivot의 index를 반환받는다.

        quicksort(my_list, start, (pivot-1))
            # pivot 기준 좌측 요소들을 재귀호출을 통해 정렬
        quicksort(my_list, (pivot+1), end)
            # pivot 기준 우측 요소들을 재귀호출을 통해 정렬

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

''' ------ 동작 설명 ------
1. quicksort 함수는 퀵 정렬을 수행할 list와 시작과 끝 index를 파라미터로 받는다.
2. 시작 인덱스가 끝 인덱스보다 작은 경우에만 동작을 수행한다.
3. 함수가 호출될 경우 주어진 리스트의 0번 index부터 마지막 index까지, 전체 범위를 pivot 기준으로 정렬한다.
4. partition 함수를 통해 정렬 후 pivot의 index를 반환받는다.
5. pivot의 위치를 토대로 그의 좌측 영역과 우측 영역을 재귀를 통해 분할하여 정렬한다.

------ 분할정복 알고리즘 중 가장 쉬웠던 문제 ------
partition 함수 구현에는 조금 시간이 걸렸지만, quicksort 함수 구현에는 오랜 시간이 걸리지 않았다.
다만 구상은 금방했고, 코드로 구현하니 오류가 자꾸 발생하여 그 오류를 해결하는데 대부분의 시간을 사용했다.
특히 최초 작성했던 코드는 지금과 거의 동일한데도 불구하고 (TypeError: unsupported operand type(s) for -: 'NoneType' and 'int')라는
오류가 계속해서 발생했다. pivot+1, pivot-1을 출력해도 정상적으로 출력이 될뿐만 아니라 type 함수로 확인해도 int형으로 출력되는데
왜 NoneType이라고 하는지 알수가 없었는데, 알고보니 partition 함수에서 while문의 조건을 (end - start) 형식으로 줬기 때문이었다.'''
