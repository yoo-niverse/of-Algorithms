''' n번째 피보나치 수를 찾아주는 함수 fib_memo를 Memoization 기법으로 작성하기 '''

def fib_memo(n, cache):
        # 입력받은 정수 n의 피보나치 수열을 계산하고, 사전에 저장하는 함수
    cache[1] = cache[2] = 1
        # 피보나치 수열의 1번, 2번 항은 항상 1이다.

    if n in cache.keys():
        return cache[n]
            # 만약 정수 n을 key로 하는 value가 사전에 이미 저장되어 있다면, value를 return

    else:
        result = fib_memo(n-1, cache) + fib_memo(n-2, cache)
        cache[n] = result
            # 그렇지 않을 경우 재귀호출을 통해 n-1번, n-2번 항을 계산하고 해당 값을 사전에 추가

    return cache[n]
        # 사전에 저장된 값들 중 key가 n인 값을 return

def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))
