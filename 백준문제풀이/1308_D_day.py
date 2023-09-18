def is_leap_year(year):
    if not (year % 400):
        return 1
    elif not (year % 100):
        return 0
    elif not (year % 4):
        return 1
    else:
        return 0


# 캠프 며칠 남았는지
# 윤년 기준
# 4로 나누어 떨어지는 해 우선 윤년 2004 2008
# 100으로 나누어 떨어지는 해는 평년 2100 2200
# 400으로 나누어 떨어지는 다시 윤년으로 1600 2000
sy, sm, sd = map(int, input().split())
dy, dm, dd = map(int, input().split())
# 윤년일 경우
leap_y = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 평년일 경우
normal_y = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
result = 0
# 캠프가 너무 길 경우 먼저 해결
if dy - sy > 1000:
    print("gg")
elif dy - sy == 1000 and dm > sm:
    print("gg")
elif dy - sy == 1000 and dm == sm and dd >= sd:
    print("gg")
else:
    # 먼저 같은 해의 경우 월을 일로 바꾼 후 비교
    if dy - sy == 0:
        sds = 0
        dds = 0
        if is_leap_year(dy):
            for i in range(1, sm):
                sds += leap_y[i]
            sds += sd
            for j in range(1, dm):
                dds += leap_y[j]
            dds += dd
            result = dds - sds
        else:
            for i in range(1, sm):
                sds += normal_y[i]
            sds += sd
            for j in range(1, dm):
                dds += normal_y[j]
            dds += dd
            result = dds - sds
    elif dy - sy == 1:
        sds = 0
        dds = 0
        if is_leap_year(sy):
            for i in range(1, sm):
                sds += leap_y[i]
            sds += sd
            sds = 366 - sds
        else:
            for i in range(1, sm):
                sds += normal_y[i]
            sds += sd
            sds = 365 - sds
        if is_leap_year(dy):
            for j in range(1, dm):
                dds += leap_y[i]
            dds += dd
            result = dds + sds
        else:
            for j in range(1, dm):
                dds += normal_y[i]
            dds += dd
            result = dds + sds
    else:
        sds = 0
        dds = 0
        if is_leap_year(sy):
            for i in range(1, sm):
                sds += leap_y[i]
            sds += sd
            sds = 366 - sds
        else:
            for i in range(1, sm):
                sds += normal_y[i]
            sds += sd
            sds = 365 - sds
        if is_leap_year(dy):
            for j in range(1, dm):
                dds += leap_y[j]
            dds += dd
            result = dds + sds
        else:
            for j in range(1, dm):
                dds += normal_y[j]
            dds += dd
            result = dds + sds
        for ny in range(sy + 1, dy):
            if is_leap_year(ny):
                result += 366
            else:
                result += 365
    print(f"D-{result}")
