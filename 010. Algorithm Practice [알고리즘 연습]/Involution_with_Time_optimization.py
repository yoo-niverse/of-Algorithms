''' 거듭제곱 함수를 시간복잡도 O(lg n)으로 구현하기 위한 최적화 코드 작성 '''
def power(x, y):
    total = 1
    if y == 1:
        return x
        # 재귀를 사용했기 때문에 BASE CASE로 1의 제곱이 될 때는 그대로 x를 반환

    sub_power = power(x, y//2)
        # 시간복잡도를 O(lg n)으로 낮추기 위해서는 문제를 절반으로 나누어야한다.
        # x^1 이상의 거듭제곱은 결국 하위 제곱의 곱으로 이루어지므로 y를 절반으로 나누어 부분문제로 만들었다.


    total = sub_power * sub_power
            # 거듭제곱하려는 횟수가 짝수인 경우 부분문제를 2번 곱하여 결과를 만들어낸다.
    if y % 2 != 0:
        total *= x
            # 홀수일 경우에는 짝수의 결과에 x를 곱하는 방법으로 결과를 도출한다.

    return total


print(power(3, 5))
print(power(5, 6))
print(power(7, 9))
