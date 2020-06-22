
def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1
    mid = start_index + end_index

    if some_list[mid] == element:
        return mid
    elif some_list[mid] > element:
        end_index = mid -1
        start_index = 0
        binary_search(element, some_list, start_index, end_index)
    elif some_list[mid] < element:
        start_index = mid+1
        end_index = None
        binary_search(element, some_list, start_index, end_index)

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
