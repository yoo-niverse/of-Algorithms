''' 입력받은 수 stairs개만큼의 계단을 올라가는 방법의 수를 반환하는 코드(possible_steps는 한번에 올라갈 수 있는 계단 수) '''

def staircase(stairs, possible_steps):
    count_case = [1, 1]             # 계단이 0 또는 1개일 때의 경우의 수는 항상 1개

    for h in range(2, stairs+1):    # 2부터 stairs(입력받은 계단의 수)만큼 반복
        count_case.append(0)        # 0이라는 요소를 미리 리스트에 추가하여 이후 자유롭게 업데이트 가능하도록 함

        for step in possible_steps: # possible_stpes 리스트에 있는 오를 수 있는 계단수를 대입하며 반복
            if h >= step:           # 만약 현재 높이(h)가 step 이상이라면
                count_case[h] += count_case[h - step]
                                    # h번째 index의 요소를 업데이트 시켜준다.

    return count_case[stairs]

print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))

''' ------ 시간복잡도 ------
    for 문이 2개 중첩되긴 하였으나, O(n^2)은 아니다.
    첫번째 반복문은 stairs의 크기에 비례하는 반복문이므로 O(n)이고,
    두번째 반복문은 possible_steps의 길이에 비례하는 반복문이므로 O(m)이다.
    
    따라서 이 코드의 시간복잡도는 O(mn)이 된다.
    
    ------ 어려웠던 점 ------
    처음에는 재귀로 생각을 했으나, 재귀는 대부분 반복문보다 효율이 떨어진다.
    한참 고민해서 겨우 해결은 했지만 문제에서 제시한대로 효율이 좋은 코드를 만들려면
    결국 반복문을 이용해야 했다.
    
    그런데 단순반복문으로는 될 것 같지 않고, 동적 프로그래밍을 활용해야할 것 같긴했다.
    그 중에서도 Memoization 방식은 재귀를 활용해야하고 사전에 저장하기 복잡할 것 같아서
    Tabulation 방식을 선택해야한다는 생각까지는 할 수 있었지만..
    
    코드로 구현하기가 너무 어려웠다. 나는 steps로 stairs를 나누어서 규칙을 발견하려고만 했는데
    단순히 이렇게 업데이트를 하는 것만으로도 결과를 도출할 수 있다는게 너무 어이가 없다.
    수학공부를 조금 더 많이 해둘걸 그랬다. 후회스럽다.. 
    '''
