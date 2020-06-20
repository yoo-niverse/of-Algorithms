''' 1부터 n까지 정수의 합을 return하는 코드 '''
def triangle_number(n):
    if n == 1:
        return 1
        # 파라미터 정수가 1인 경우에는 1을 반환하고 수행을 종료한다.
    return (n + triangle_number(n-1))
        # 그 외의 경우에는 (n-1)을 파라미터로 재귀호출하고, 그 결과와 n을 합하여 return

# 테스트: triangle_number(1)부터 triangle_number(10)까지 출력
for i in range(1, 11):
    print(triangle_number(i))

''' ------ 동작 설명 ------
1. 삼각수를 구할 n을 파라미터로 전달 받아서 재귀호출을 통해 결과를 return 한다.
'''
