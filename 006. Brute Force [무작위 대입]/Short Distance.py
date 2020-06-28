''' 2개 좌표간의 최단거리를 계산하여 가장 가까운 좌표 2개를 return하는 코드'''
from math import sqrt
    # 제곱근 사용을 위한 sqrt 함수 import


def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)
    # 제곱근을 사용하여 파라미터로 받은 2개 좌표간의 거리 계산 후 return

def closest_pair(coordinates):
    min = 500
        # 최소거리의 초기값을 500으로 지정
    store_1 = store_2 = ()
    for first in test_coordinates:
        for second in test_coordinates:
                # first와 second에 각각 좌표값을 저장
            if first == second:
                continue
                    # first와 second의 값이 같은 경우 거리는 0이 되어버리므로, 포함하지 않음
            if distance(first, second) < min:
                min = distance(first, second)
                store_1 = first
                store_2 = second
                    # 좌표간 거리가 min의 값보다 작다면 min의 값을 최신화하고, fisrt와 second를 반환
    return [store_1, store_2]

# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))

''' ------ 동작 설명 ------
1. 2개의 좌표를 파라미터로 전달받는다.
2. 반복문을 사용하여 튜플에 저장된 좌표간의 거리를 계산하여 최단 거리를 찾는다.
3. 최단거리를 만들어내는 좌표 2개를 반환한다.'''
