''' 입력받은 수 n개만큼의 계단을 올라가는 방법의 수를 반환하는 코드 '''
def staircase(n):
    if n <= 1:
        return 1

    ONLY_1STAIR = 1
        # 계단을 1칸씩만 올라가서 도달하는 경우의 수는 항상 1개

    once_2stairs = n-1
        # 딱 한번만 2칸을 올라가서 도달하는 경우의 수는 n-1개



# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
