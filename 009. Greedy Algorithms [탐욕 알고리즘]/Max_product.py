''' 각 리스트에 있는 요소들 중 하나를 뽑아 최대값을 반환하는 코드를 Greedy Algorithm으로 구현 '''
def max_product(card_lists):
    if len(card_lists) <= 1:
        return max(card_lists[0])
            # 카드 리스트의 길이가 1이하일 경우 첫번째 리스트에서의 최대값을 return
    else:
        return (max(card_lists[0]) * max_product(card_lists[1:]))
            # 그 외의 경우는 0번 인덱스에서의 최대값과 1번 인덱스를 재귀호출한 결과를 곱하여 return
            # 재귀호출이 아닌 for 반복문을 사용할 경우, for card in card_list: 의 형태로 작성할 수 있다.

# 테스트
test_cards1 = [[1, 6, 5], [4, 2, 3]]
print(max_product(test_cards1))

test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
print(max_product(test_cards2))

test_cards3 = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
print(max_product(test_cards3))

test_cards4 = [[5, 5, 5], [4, 3, 5], [1, 1, 1], [9, 8, 3], [2, 8, 4], [5, 7, 4]]
print(max_product(test_cards4))

'''
1. 최적 부분구조가 존재하는가?
YES. 각 리스트에서 어떤 요소를 선택할 것인지에 따라 결과가 달라질 수 있다.

2. 탐욕적 속성이 존재하는가?
YES. 가장 큰 요소들을 선택하여 곱하는 것이 가장 큰 값을 얻을 수 있다. 
'''
