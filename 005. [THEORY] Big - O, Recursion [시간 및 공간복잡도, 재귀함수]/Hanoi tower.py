''' 재귀함수를 이용하여 하노이의 탑 해결과정을 구현하는 코드 '''
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    pegs = [] # 기둥에 존재하는 disk를 저장하기 위한 list
    for i in range(start_peg, end_peg+1):
        pegs.append(0)
            # end_peg의 값에 따라 기둥별 리스트 공간을 추가

    pegs[start_peg-1] = num_disks
        # 첫번째 기둥에는 파라미터로 받은 num_disks 즉, disk를 전체 저장

    if num_disks == 1:
        pegs[start_peg-1] = 0
        pegs[end_peg-1] = 1
        return move_disk(1, start_peg, end_peg)
            # BASE CASE : disk가 1개인 경우, 1번 기둥에서 마지막 기둥(end_peg)으로 바로 이동 후 종료

    if num_disks == 0:
        return None
            # BASE CASE : disk가 0개인 경우, None을 반환하며 종료

    if num_disks > 1:
        return (???)
            # disk가 1개 이상인 경우 : 어떻게 디스크의 크기를 구분하여 이동시킬 것인가?

    pegs[start_peg-1] -= 1
    pegs[end_peg-1] += 1
    move_disk(num_disks, start_peg, end_peg)
        # 가장 큰 원판 마지막 기둥으로 이동 / 마지막에 처리해야함(작은 원판부터 처리)

    # 원판의 크기를 어떻게 식별해야할까?


    print(pegs)



# 테스트 코드
hanoi(3, 1, 3)
hanoi(1, 1, 9)
