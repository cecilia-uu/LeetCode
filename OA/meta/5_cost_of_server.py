# startupTimes [str]
# shutdownTimes [str]
# currentTieme 24-hour format

def calculate(a, b) -> int:
    # a - b
    x = int(a[:2]) * 60 + int(a[3:])
    y = int(b[:2]) * 60 + int(b[3:])
    return x - y

def format(x) -> int:
    # "12:30" -> 1230
    return int(x[:2] + x[3:])

def solution(startupTimes, shutdownTimes, currentTime) -> int:
    ans = 0
    for s, e in zip(startupTimes, shutdownTimes):
        # current > s -> 0
        if format(currentTime) < format(s):
            continue
        # s <= current <= e -> current - s
        elif e == "None" or format(s) <= format(currentTime) <= format(e):
            ans += calculate(currentTime, s)
        # current > e -> e - s
        else:
            ans += calculate(e, s)
    return ans

print(solution(["12:30", "14:00", "19:55"], ["15:00", "17:00", "None"], "20:00"))