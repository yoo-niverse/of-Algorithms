''' 파라미터 some_list를 거꾸로 뒤집는 함수 '''
def flip(some_list):
    length = len(some_list)
        # 파라미터 some_list의 길이를 length에 저장
    if length == 1 or length == 0:
        return some_list
        # 파라미터 list의 길이가 0또는 1인 경우는 BASE CASE. 즉, 뒤집는 연산이 불필요하므로 그대로 return

    return some_list[-1:] + flip(some_list[:-1])
        # 그 외의 경우에는 마지막 index에 재귀호출의 결과(0번 ~ 마지막 전 index까지 list를 파라미터로)를 연결

# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)

''' ------ 동작 설명 ------
1. 파라미터로 뒤집는 연산을 하기 위한 list를 전달받는다.
2. 파라미터의 길이가 1이나 0인 경우에는 수행이 불필요한 BASE CASE이므로 파라미터를 그대로 return 한다.
3. 그 외의 경우에는 파라미터의 마지막 index 요소를 분리하여 맨 앞에 두고, 나머지 요소들을 파라미터로 하여 재귀호출한다.
4. 마지막 index 요소와 재귀호출의 결과를 연결하여 return 한다. 

 ------ 어려웠던 점 ------
 지금까지 해결했던 예제 중 가장 오랜 시간 붙잡고 있었던 것 같다.
 떠오른 내용으로 코드를 작성하면 자꾸 오류가 발생하거나 제대로 동작하지 않았다.
 그래서 처음으로 힌트도 7개 모두 써버리고 말았다. 마지막 요소를 분리하고 나머지를 파라미터로 하여 재귀호출한다는 생각은 비슷했다.
 그러나 나는 some_list(length).append(flip(some_list[0:length-1]))의 꼴로 코드를 작성했다.
 모범 답안에 비해 더 복잡하기도 하고, 결론적으로 동작하지 않는 코드였다.
 
 이렇게까지 긴 시간이 걸린 이유로는 
 BASE CASE와 RECURSIVE CASE를 분리하는 연습이 부족했고,
 떠오른 내용을 코드로 구현하는 능력이 아직 많이 부족했기 때문인 것 같다. 더 많이 연습해야겠다.'''
