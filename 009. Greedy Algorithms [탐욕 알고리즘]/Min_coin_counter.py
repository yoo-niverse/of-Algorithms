''' 최소 동전으로 잔돈을 거슬러 주는 코드를 탐욕 알고리즘으로 작성 '''
def min_coin_count(value, coin_list):
    amount_coin = []
    amount_coin.append((value//500))
    amount_coin.append((value-(amount_coin[0]*500))//100)
    amount_coin.append((value-(amount_coin[0]*500+amount_coin[1]*100))//50)
    amount_coin.append((value-(amount_coin[0]*500+amount_coin[1]*100+amount_coin[2]*50))//10)
        # 금액별 동전으로 계산하여 리스트에 동전의 수를 저장


    total = 0
    for i in range(len(amount_coin)):
        total += amount_coin[i]
            # 리스트에 저장된 동전의 수를 모두 더한다.
            ''' sorted를 통해 coin_list를 정렬하고, for문을 통해 리스트의 요소를 불러온 뒤 즉시 나누어 가산할 수 있다.
                거슬러줄 금액이 변하는 것에 대해서는 % 연산을 통해 즉각 업데이트 해준다. '''

    return total
# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))

'''
1. 최적 부분구조가 존재하는가?
YES. 가장 큰 단위의 동전을 지급하는 방법으로 문제를 분할할 수 있다.

2. 탐욕적 속성이 존재하는가?
YES. 작은 단위보다 큰 단위의 동전부터 지급함으로써 동전의 수를 줄일 수 있다. '''
