''' 분할 정복을 이용해 start ~ end의 값을 모두 더하는 코드'''
def consecutive_sum(start, end):
    sum_l = sum_r = 0
    mid = (start + end) // 2
        # 문제를 분할하기 위해 input을 모두 더한 후 절반으로 나누어 중간값을 찾는다.
    if start == end:
        return start
        # 시작하는 수와 마지막 수가 같은 경우 문제를 더 이상 분할할 수 없으므로 그대로 반환한다.

    sum_l += consecutive_sum(start, mid)
        # 문제 분할 1 : 첫 수부터 중간값까지 분할하여 계산한 값을 sum_l에 저장
    sum_r += consecutive_sum(mid+1, end)
        # 문제 분할 2 : 중간값 다음부터 마지막 수까지 분할하여 계산한 값을 sum_r에 저장

    return(sum_r + sum_l)

# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))

''' ------ 동작 설명 ------
1. 함수의 파라미터로 시작값과 마지막 값을 받는다.
2. 시작값과 마지막 값을 이용해 중간값을 계산한다.
3. 중간값을 기준으로 문제를 분할하여 재귀를 통해 연산한다.
'''
