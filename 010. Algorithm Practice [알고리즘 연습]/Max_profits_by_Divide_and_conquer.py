''' 최대 수익구간의 값을 분할정복 방식으로 해결 (시간복잡도 : O(nlgn))'''
def maxim(profits, start, end):
        # maxim 함수는 가운데 구간에서의 최대 수익을 계산하기 위한 함수
    mid = (start + end) // 2

    leftsum = 0
    leftmax = profits[mid]

    for i in range(mid,start-1,-1):
        leftsum += profits[i]
        leftmax = max(leftmax, leftsum)

    rightsum = 0
    rightmax = profits[mid+1]

    for j in range(mid+1, end+1):
        rightsum += profits[j]
        rightmax = max(rightmax, rightsum)

    return leftmax + rightmax

def sublist_max(profits, start, end):
    if end - start <= 1:
        return profits[end]

    mid = (start+end) // 2
    left = sublist_max(profits, start, mid)
    right = sublist_max(profits, mid+1, end)
        # 문제를 분할하여 오른쪽과 왼쪽 영역으로 나누어 재귀호출
    middle = maxim(profits, start, end)
        # maxim 함수를 이용하여 중간 구간에서의 최대 수익 계산

    return max(left, right, middle)

# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))
