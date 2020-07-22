''' 기존에 작성했던 Max_profits 코드를 O(n)으로 시간 최적화 하여 재작성 '''
def sublist_max(profits):
    # 시간복잡도를 n으로 줄이기 위해서는 반복문을 1개만 사용해야함.
    last = len(profits)-1
    start = i = 0
    total_list = []
        # 각 구간별 합계를 계산하여 저장할 리스트
    while start < last:

        total_list.append(sum(profits[start:i]))
            # start 인덱스부터 i번째 인덱스까지의 합을 구한 후 total_list에 추가
        i += 1
            # i를 +1만큼 증가시켜 탐색구간을 확장
        if i == last+1:
            # i가 마지막 인덱스에 도달한 경우
            start += 1
                # 탐색 시작지점 인덱스를 +1 증가
            i = start
                # i도 탐색 시작지점부터 재탐색 시작

    return (max(total_list))
        # 리스트에 저장된 값 중 최대값을 반환


# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))

'''
------ 아쉬운 점 ------
해설에서는 for 문을 사용하여
    max_check = max(max_check + profits[i], profits[i])
    max_profit = max(max_profit, max_check)
    return max_profit
의 형태로 간단하게 코드를 작성하였다.

해설과 조금 다르긴 하지만, 나도 반복문을 1개만 사용하였고 if문 자체가
시간복잡도에 미치는 영향은 미미하기에 O(2n) = O(n)이다.
하지만 조금 더 간단하게 코드를 작성하지 못한 점이 아쉽다. 
'''
