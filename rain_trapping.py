# 2차원 평면에 x축으로 늘어선 Bar 들이 있다. 물을 채웠을시 물이 차지하는 크기를 구하는 코드를 작성하라.
# 예) [1,3,2,6,3,5] 같은 list 입력 받는다고 치면 각 값은 Bar의 높이 값이다. 두개의 bar 사이에 공간이 있으면 물이 채워질 것이다.

def solution(bars) :
    
    # 투 포인트 방식 접근
    left, right = 0, len(bars) - 1
    left_max, right_max = 0,0
    answer = 0

    while left < right:
        left_max, right_max = max(left_max, bars[left]), max(right_max, bars[right])

        if left_max <= right_max:
            answer += left_max - bars[left]
            left += 1
        else:
            answer += right_max - bars[right]
            right -= 1

    return answer

print(solution([5,0,1,2,12]))

