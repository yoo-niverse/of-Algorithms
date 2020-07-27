def trapping_rain(buildings):
    amount_water = []
    mid = len(buildings) // 2
    left = max(buildings[:mid])
    right = max(buildings[mid+1:])
    for i in range(len(buildings)):
        if buildings[i] == left or buildings[i] == right:
            continue
        else:
            l_one = max(buildings[:i])
            r_one = max(buildings[i+1:])

            if l_one > r_one:
                amount_water.append(l_one - r_one)
            else:
                amount_water.append(r_one - l_one)

    return (sum(amount_water))



# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
