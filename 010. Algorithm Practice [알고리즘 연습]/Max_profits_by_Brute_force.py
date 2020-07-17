''' Brute Force 방식을 이용하여 리스트에서의 최대합을 return '''
def sublist_max(profits):

    if len(profits) == 1:
        return profits

    else:
        amount = 0
            # 최대합을 저장하며 update하는 변수
        tmp = 0
            # amount와의 비교를 위해 i~j 인덱스 요소의 합을 임시저장하는 변수
        #max_list = []
        for i in range(len(profits)-1):
            tmp = 0
            for j in range(i, len(profits)):
                tmp += profits[j]
                    # tmp에 i부터 j까지 요소의 합을 저장
                if tmp > amount:
                    amount = tmp
                        # tmp의 값이 amount보다 커지면 값을 update
                    #max_list = profits[i:j+1]

        return amount


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))
