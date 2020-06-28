''' n으로 넘겨받은 파라미터 각 자릿수의 합을 return'''
def sum_digits(n):
    number = str(n)
    length = (len(number)-1)
        # 넘겨받은 정수 n을 문자열로 변환하고(number), 그 문자열의 마지막 index를 length에 저장
    if length <= -1:
        return 0
        # length = (len(number)-1) 이므로 length == -1이 되는 경우에는 0번 index까지의 연산이 끝났다는 의미. 수행종료

    sum = int(number[(length)]) + int(sum_digits(number[0:length]))
        # 자릿수의 합 sum은 파라미터의 마지막 인덱스의 값과 마지막 인덱스를 제외한 나머지 부분을 파라미터로 재귀호출하여 처리한 값을 저장
    return sum
        # 자릿수의 합을 반환


# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))

''' ------ 동작 설명 ------
1. 자릿수의 합을 계산할 정수 n을 파라미터로 전달받는다.
2. n을 indexing하기 위하여 문자열 number로 변환해주고, 마지막 인덱스는 length 변수에 (len(number)-1)로 저장한다.
3. 만약 length가 -1보다 작은 경우에는 최초 전달받은 정수의 0번 index까지 모두 처리한 것이므로, 0을 return하여 연산을 종료한다.
4. 그 외의 경우에는 주어진 파라미터의 마지막 index를 int형으로 변환하고, 마지막을 제외한 나머지 부분을 파라미터로 재귀호출한 값과 더하여 sum을 반환한다.

 ------ 어려웠던 점 ------
 정수를 문자열로 casting하여 index를 활용하면 되겠다고 생각했으나, 어떤식으로 재귀호출을 해야할지 생각하기 힘들었다.
 고민 끝에 마지막 index를 int형으로 casting하여 더하고 나머지 부분을 slicing하여 재귀호출하는 방법으로 결정했으나
 자꾸 오류가 발생했다. None type에는 int() 캐스팅을 적용할 수 없다는 TypeError가 계속 발생했는데
 대체 뭐가 문제인지 감을 잡지 못하다가, None은 값이 없다는 의미라는 것을 다시 떠올리며 함수 수행 후 값을 반환하지 않는다는 것을 알게 되었다.
 그래서 마지막에 sum을 return하는 구문을 추가해주었고, 다행히 정상 작동되었다.
 '''
