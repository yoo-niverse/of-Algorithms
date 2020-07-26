''' 주어진 리스트에서 원하는 합(search_num)을 만들 수 있는 조합이 있는지 확인하는 코드 '''
def sum_in_list(search_sum, sorted_list):
    i = 0
    j = 1
    while i < len(sorted_list)-1 and j < len(sorted_list)-1:
        # 인덱스 i와 j가 각각 리스트의 길이보다 작은 동안 반복문이 수행된다.
        if search_sum == sorted_list[i] + sorted_list[j]:
            return True
            # 찾고자 하는 합이 이루어진다면 True를 반환하고 종료
        else:
            i += 1
            # 합이 일치하지 않을 경우 i만 +1 증가시켜 반복문을 다시 수행

        if i == len(sorted_list) - 1 and j < len(sorted_list)-1:
            # i가 가장 마지막 인덱스에 도달했고, j가 아직 마지막 인덱스보다 작다면
            j += 1
                # j의 값을 +1 증가시키고
            i = j + 1
                # i는 j 다음 인덱스부터 탐색

    return False
        # 반복문 수행이 모두 종료되었음에도 결과가 도출되지 않으면 False를 반환


print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))
