''' 가장 효율적으로 리스트에 중복 요소가 있는 element를 찾아내는 코드 '''
def find_same_number(some_list):
    for i in range(len(some_list)):
        if some_list[i] in some_list[i+1:]:
            # i번째 인덱스 이후 리스트에서 현재 위치의 요소와 동일한 요소가 있다면
            return some_list[i]
                # 현재 요소를 반환하고 수행을 종료

    ''' Dynamin Programming의 Memoization을 사용할 경우 아래와 유사 
    double_element = {}
    for elem in some_list:
        if elem in double_element:
            return elem
        
        double_element[elem] = True
        '''



# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
