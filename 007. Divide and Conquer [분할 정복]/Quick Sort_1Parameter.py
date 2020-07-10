from Partition_of_Quick_Sort import partition
    # 파티션 함수를 작성한 모듈을 import
def quicksort(my_list, start=0, end=None):

    if end == None:
        end = len(my_list)-1
            
    if start < end:
        # 정렬을 시작하는 index가 마지막 index보다 큰 경우 명령을 수행하지 않음
        pivot = partition(my_list, start, end)
            # partition 함수의 실행결과를 통해 pivot의 index를 반환받는다.

        quicksort(my_list, start, (pivot-1))
            # pivot 기준 좌측 요소들을 재귀호출을 통해 정렬
        quicksort(my_list, (pivot+1), end)
            # pivot 기준 우측 요소들을 재귀호출을 통해 정렬

list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1) # start, end 파라미터 없이 호출
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2) # start, end 파라미터 없이 호출
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3) # start, end 파라미터 없이 호출
print(list3)
