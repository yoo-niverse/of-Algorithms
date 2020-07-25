''' 입력받은 수 stairs개만큼의 계단을 올라가는 방법의 수를 반환하는 코드(possible_steps는 한번에 올라갈 수 있는 계단 수) '''

def staircase(stairs, possible_steps):
    if stairs < 0:
        return 0
        # 오를 계단이 0개 미만(음수)인 경우에는 경우의 수를 카운팅할 수 없으므로 0 반환

    if stairs <= 1:
        return 1
        # 계단이 1개 또는 0개인 경우 가능한 경우는 무조건 1개 (BASE CASE)

    count = 0         # 각 경우의 수에 대한 합을 저장
    for i in possible_steps:
        count += staircase(stairs-i, possible_steps)
    return count

print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))
