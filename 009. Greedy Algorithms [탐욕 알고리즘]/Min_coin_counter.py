''' 최소 동전으로 잔돈을 거슬러 주는 코드를 탐욕 알고리즘으로 작성 '''
def min_coin_count(value, coin_list):
    amount_coin = []
    amount_coin.append((value//500))
    amount_coin.append((value-(amount_coin[0]*500))//100)
    amount_coin.append((value-(amount_coin[1]*100))//50)
    amount_coin.append((value-(amount_coin[2]*50))//10)

    total = 0
    for i in range(len(amount_coin)-1):
        print(amount_coin[i])

    return total
# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
#print(min_coin_count(1700, default_coin_list))
#print(min_coin_count(23520, default_coin_list))
#print(min_coin_count(32590, default_coin_list))

'''
1. 최적 부분구조가 존재하는가?
YES. 가장 큰 단위의 동전을 지급하는 방법으로 문제를 분할할 수 있다.

2. 탐욕적 속성이 존재하는가?
YES. 작은 단위보다 큰 단위의 동전부터 지급함으로써 동전의 수를 줄일 수 있다. '''
