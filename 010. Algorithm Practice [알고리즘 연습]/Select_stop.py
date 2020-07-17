def select_stops(water_stops, capacity):
    left_water = capacity
    get_stops = []
    distance = 0
    for i in range(0, len(water_stops)-1):
        distance -= water_stops[i]
        left_water -= distance
        if left_water > water_stops[i] - water_stops[i-1]:
            continue
        else:
            get_stops.append(water_stops[i])


    return get_stops


# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))
