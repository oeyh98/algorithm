from collections import deque

def solution(progresses, speeds):
    answer = []
    dq = deque(progresses)
    speeds = deque(speeds)

    while dq:
        cnt = 0

        while dq and dq[0] >= 100:
            dq.popleft()
            speeds.popleft()
            cnt += 1

        if cnt > 0:
            answer.append(cnt)

        for i in range(len(speeds)):
            dq[i] += speeds[i]

    return answer