''' 모든 피보나치항을 기억할 필요가 없을 때, 리스트 대신 변수를 이용하여 공간복잡도를 O(n) → O(1)로 최적화한 코드 '''
def fib_optimized(n):
    current = 1
        # 현재 항
    previous = 0
        # 이전 항
    tmp = 0
        # 다음 항을 계산하는 과정에서 현재항을 임시 보관하기 위한 변수

    i = 1
    while i < n:
        tmp = current
        current += previous
        previous = tmp
        i += 1

    return current

# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
