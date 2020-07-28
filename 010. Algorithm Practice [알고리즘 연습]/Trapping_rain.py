''' Brute Force 챕터에서 작성했던 코드의 시간복잡도를 O(n^2) 미만으로 단축한 코드 '''
def trapping_rain(buildings):
    total_height = 0 # 총 갇히는 비의 양을 담을 변수
    n = len(buildings)

    # 각각 왼쪽 오른쪽 최대값 리스트 정의
    left_list = [0] * n
    right_list = [0] * n

    # buildings 리스트 각 인덱스 별로 왼쪽으로의 최댓값을 저장한다
    left_list[0] = buildings[0]
    for i in range(1, n):
        left_list[i] = max(left_list[i - 1], buildings[i])

    # buildings 리스트 각 인덱스 별로 오른쪽으로의 최댓값을 저장한다
    right_list[-1] = buildings[-1]
    for i in range(n - 2, -1, -1):
        right_list[i] = max(right_list[i + 1], buildings[i])

    # 저장한 값들을 이용해서 총 갇히는 비의 양을 계산한다
    for i in range(n):
        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(right_list[i], left_list[i])

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        total_height += max(0, upper_bound - buildings[i])

    return total_height

print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


''' ------ 시간복잡도를 줄일 때 참고할 것 ------
    예를 들어 O(n^2)을 O(n)으로 줄인다고 할때, 반드시 반복문을 하나만 사용해야할 필요는 없다.
    간단히 설명하면 for문 내에 for문이 또 들어가서 2중 반복문이 된 경우 시간복잡도가 O(n^2)이 되는데,
    이 각각의 for문을 분리하여 O(n) + O(n) = O(2n)으로 만드는 것도 하나의 방법이다.
    O(2n) = O(n)이기 때문이다.
    
    이 알고리즘을 예로 설명하면
    Brute Force 방식에서는 for문 내에 max 메소드가 들어가 있어 시간복잡도를 증가시켰는데,
    이를 개선하기 위한 방법으로 for문에 n개 미만의 리스트를 탐색하는 max만 넣어 두개의 반복문으로 각각 만들 수도 있다.
    
    <Brute Force 방식을 적용, 시간복잡도가 O(n^2)인 상황 : 반복문에 max문 사용>
     for i in range(1, len(buildings)-1):
        l_max = max(buildings[:i])
            # 현재 index 기준 왼쪽에서 가장 큰 건물의 높이 저장
        r_max = max(buildings[i:])
            # 현재 index 기준 오른쪽에서 가장 큰 건물의 높이 저장

        sum += max(0, min(l_max, r_max) - buildings[i])
    
    
    <O(n)으로 시간복잡도를 감소시킨 상황 : 반복문 3개 사용>
    # buildings 리스트 각 인덱스 별로 왼쪽으로의 최댓값을 저장한다
    left_list[0] = buildings[0]
    for i in range(1, n):
        left_list[i] = max(left_list[i - 1], buildings[i])
                
    # buildings 리스트 각 인덱스 별로 오른쪽으로의 최댓값을 저장한다
    right_list[-1] = buildings[-1]
    for i in range(n - 2, -1, -1):
        right_list[i] = max(right_list[i + 1], buildings[i])

    # 저장한 값들을 이용해서 총 갇히는 비의 양을 계산한다
    for i in range(n):
        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(right_list[i], left_list[i])

 
    
    '''
