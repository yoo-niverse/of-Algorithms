''' 리스트 요소간의 차이가 가장 큰 구간의 값을 반환하는 코드 (시간복잡도 : O(n))'''
def max_profit(stock_list):
    last = len(stock_list)-1
    start = 0
    i = 1
    total_list = []
        # 각 구간별 차이를 계산하여 저장할 리스트
    while start < last:

        total_list.append(-(stock_list[start] - stock_list[i]))
            # start 인덱스와 i번째 인덱스까지의 차을 구한 후 total_list에 추가
        i += 1
            # i를 +1만큼 증가시켜 탐색구간을 확장
        if i == last+1:
            # i가 마지막 인덱스에 도달한 경우
            start += 1
                # 탐색 시작지점 인덱스를 +1 증가
            i = start + 1
                # i도 탐색 시작지점 다음부터 재탐색 시작

    return (max(total_list))
        # 리스트에 저장된 값 중 최대값을 반환



# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))


''' 모범 답안
def max_profit(stock_list):
    # 현재까지의 최대 수익
    max_profit_so_far = stock_list[1] - stock_list[0]

    # 현재까지의 최소 주식 가격
    min_so_far = min(stock_list[0], stock_list[1])

    # 주식 가격을 하나씩 확인한다
    for i in range(2, len(stock_list)):
        # 현재 파는 것이 좋은지 확인한다
        max_profit_so_far = max(max_profit_so_far, stock_list[i] - min_so_far)

        # 현재 주식 가격이 최솟값인지 확인한다
        min_so_far = min(min_so_far, stock_list[i])

    return max_profit_so_far

'''
