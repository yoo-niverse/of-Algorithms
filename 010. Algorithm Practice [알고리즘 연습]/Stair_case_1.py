''' 입력받은 수 n개만큼의 계단을 올라가는 방법의 수를 반환하는 코드 '''
def staircase(n):
    if n <= 1:
        return 1

    case_count = []
    case_count.append(1)         # 계단을 1칸씩만 올라가서 도달하는 경우의 수는 항상 1개
    case_count.append(n-1)       # 딱 한번만 2칸을 올라가서 도달하는 경우의 수는 n-1개
    left_stairs = n

    count_two_more = n // 2      # 두 계단을 오르는 횟수가 최대 몇번까지 가능한지 계산하여 저장

    for i in range(2, count_two_more+1):
        arrange = n-i            # 두 계단을 오르는 횟수에 대한 자릿수를 계산하여 저장
        # 순열 공식을 어떻게 구현하지?
        case_count.append(arrange * (arrange-1) // i)

    return sum(case_count)















# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
