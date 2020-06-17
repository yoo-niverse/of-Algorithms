def is_palindrome(word):
    count = 0
        # 일치하는 단어수를 count하기 위한 변수
    for i in range(0, len(word) // 2):
            # 0부터 단어 글자수의 절반-1까지 반복 수행

        if word[(len(word)-i)-1] == word[i]:
            count += 1
                # word[(len(word)-i)-1] : 단어의 맨 끝 글자
                # 단어의 첫글자와 끝글자부터, 정중앙을 기준으로 서로 쌍을 이루는 글자를 상호 비교하여
                # 같은 글자일 경우 count를 +1 증가시킨다.

    if count == (len(word) // 2):
        return True
        # 반복문 수행이 종료된 후 count의 개수가 글자수의 절반과 같다면 팔린드롬이므로 True를 반환
        # for문 내부에 있는 if문에서 한번에 2개의 단어를 비교하므로 count == len(word)가 아님.
    else:
        return False

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))

''' ------ 동작 설명 ------ 
1. 팔린드롬 여부를 판별하고자 하는 단어를 파라미터로 넘겨받는다.
2. for 반복문을 통해 단어의 0번째 index부터, (글자수의 절반 - 1)번째 index까지 반복한다.
3. 단어의 첫글자 - 마지막(n번째) 글자, 두번째 글자와 n-1번째 글자 등 이와 같은 방법으로 각 글자를 비교한다.
4. 만약 글자를 비교하며 두 글자가 일치한다면 count 변수를 +1 증가시켜준다.
5. 반복문 수행이 종료된 후 count의 값이 글자수의 절반과 같다면 팔린드롬이므로 True를 반환한다.
   * 글자수의 절반과 비교하는 이유? 한번에 두 글자씩 비교하였기 때문에 count 값은 절반 이상이 될 수 없음
   
   ------ 어려웠던 점 ------
   문제의 조건에서 append, insert 메소드를 사용하지 말라고 했다.
   이 예제는 파이썬 프로그래밍 기초를 수강하며 해결했던 문제였지만, 그때 사용했던 방법을 쓰지않고
   하려고 하니 애를 먹었는데 어떤식으로 진행해야할지는 금방 떠올릴 수 있었다.
   그럼에도 시간이 오래걸린 이유는 반복문의 수행을 글자수의 절반만큼만 해야한다는 것을 생각하지 못했기 때문이었다. '''
