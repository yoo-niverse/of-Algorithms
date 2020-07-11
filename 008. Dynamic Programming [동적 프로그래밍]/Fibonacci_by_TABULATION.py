''' n번째 피보나치 수를 찾아주는 함수 fib_memo를 Tabulation 기법으로 작성하기 '''
def fib_tab(n):
    fibofibo = [1, 1]
        # 피보나치 수열의 1번, 2번항은 항상 1이므로 리스트에 이 값을 미리 저장해둔다.

    i = 3
        # i = 3일때,
    while i < n+1:
        fibofibo.append(fibofibo[i-2] + fibofibo[i-3])
            # 피보나치 수열의 공식에 따라 list에 n-1번, n-2번 항을 합한 값을 추가한다.
            # 이 때, n-2 / n-3의 꼴로 인덱스가 지정된 것은 리스트의 0번 인덱스가 초항 a1을 의미하기 때문이다.
        i += 1

    return fibofibo[n-1]
        # fibofibo[0]은 a1을 의미하므로, n번째 인덱스가 아닌 n-1번째 인덱스를 return해야 한다.

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))
