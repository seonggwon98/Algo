import math
N, K = map(int, input().split())
# N개의 성별 여 0 남 1 과 학년 주어짐
info = [tuple(map(int, input().split())) for _ in range(N)]
student = {(0, 1): 0,
           (0, 2): 0,
           (0, 3): 0,
           (0, 4): 0,
           (0, 5): 0,
           (0, 6): 0,
           (1, 1): 0,
           (1, 2): 0,
           (1, 3): 0,
           (1, 4): 0,
           (1, 5): 0,
           (1, 6): 0,
           }
for i in range(N):
    student[info[i]] += 1
room = 0
for value in student.values():
    if value == 0:
        continue
    elif value <= K:
        room +=1
    else:
        room += math.ceil(value/K)
print(room)


