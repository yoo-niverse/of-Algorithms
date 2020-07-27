''' Brute Force 챕터에서 작성했던 코드의 시간복잡도를 O(n^2) 미만으로 단축한 코드 '''
def trapping_rain(buildings):
    amount_water = []                  # 각 인덱스별 빗물의 양을 저장하기 위한 리스트
    mid = len(buildings) // 2          # 리스트 인덱스의 중간값을 계산
    left = max(buildings[:mid])        # left 변수에 중간을 기준으로 왼쪽에서 가장 큰 값을 저장
    right = max(buildings[mid+1:])     # right 변수에 중간을 기준으로 오른쪽에서 가장 큰 값을 저장

    for i in range(1, len(buildings)):
        if buildings[i] == left or buildings[i] == right:
            continue
                # i번째 요소의 값이 가장 큰 좌측 또는 우측의 값이라면 pass
        else:

            if left > right:
                amount_water.append(right - buildings[i])
            else:
                amount_water.append(left - buildings[i])

    return (sum(amount_water))


print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    # 이와 같은 경우에서 1번 인덱스와 3번 인덱스 사이 빗물의 양이 저장되지 않는 것은 어떻게 해결?
