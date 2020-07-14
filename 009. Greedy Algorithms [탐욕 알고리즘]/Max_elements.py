''' 튜플에 저장된 값의 범위가 서로 겹치지 않도록 가장 많은 요소를 선택하는 코드 '''
def course_selection(course_list):
    course_table = []
        # 가장 많은 결과를 반환하기위해 각 요소를 저장하는 리스트

    course_list.sort(key=lambda x: x[1])
        # ★리스트에 들어있는 튜플을 정렬하면 [0] index를 기준으로 정렬된다. 이때 다른 요소를 기준으로 정렬하고자 한다면
        # 위와 같이 sort 메소드에 key 옵션을 추가해주면 된다.

    course_table.append(course_list[0])
        # 끝점을 기준으로 튜플을 모두 정렬했으므로, 가장 첫 요소는 필수적으로 선택된다.

    for i in range(1, len(course_list)):
        if course_table[len(course_table)-1][1] < course_list[i][0]:
            course_table.append(course_list[i])
                # for문을 통해 table 리스트에 들어있는 튜플의 끝점과 i번째 요소의 시작점을 비교하고,
                # 시작점의 크기가 끝점보다 클 경우 table 리스트에 추가한다.

    return course_table

# 테스트 - 튜플의 [0]번 요소는 시작점 / [1]번 요소는 끝점
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))

'''
1. 최적 부분구조가 존재하는가?
YES. 주어진 요소(튜플)들 중 어떤 요소를 가장 먼저 선택할 것이냐에 따라 선택할 수 있는 튜플이 달라진다.

2. 탐욕적 속성이 존재하는가?
YES. 끝점이 가장 작은 튜플부터 선택함으로써 최대한 많은 요소를 선택할 수 있다.
'''
