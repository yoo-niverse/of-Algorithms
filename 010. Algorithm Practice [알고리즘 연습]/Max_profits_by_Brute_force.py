def sublist_max(profits):

    if len(profits) == 1:
        return profits

    else:
        amount = 0
        for i in range(len(profits)-1):
            amount = profits[i]
            for j in range(i+1, len(profits)-1):
                if amount < 


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))
