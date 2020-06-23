
def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1
    mid = start_index + end_index // 2

    if some_list[mid] == element:
        return mid
        # 아래. 생각치 못한 부분 / 작성한 내용이 잘못되었음
    # elif some_list[start_index] > element or some_list[end_index] < element:
    if start_index > end_index:
        return None
    '''elif start_index == end_index:
        if some_list[start_index] == element:
            return start_index'''

    if some_list[mid] > element:
        return binary_search(element, some_list, 0, mid-1)

    if some_list[mid] < element:
        return binary_search(element, some_list, mid+1)

    # return을 안써줘서 다 None 나옴. 반환을 안해주니까 넌이지 없는 넌이 아니고

''' 
BASE CASE : 중간값(mid)가 element와 같을 때
 - 구현완료
 
 RECURSIVE CASE : 
  1) mid > element - end_index=mid-1
  2) mid < element - start_index=mid+1
  
  6.23 : IndexError : list index out of range
'''

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
