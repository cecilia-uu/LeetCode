# busiest month

# dataList: [str]
# return string: '07' latest one

def solution(dataList) -> str:
    month = {}
    for d in dataList:
        string = d[5:7]
        if string not in month:
            month[string] = 1
        else:
            month[string] += 1
    ma = max(month.values())
    ans = "01"
    for m in month.keys():
        if month[m] == ma and int(m) > int(ans):
            ans = m
    return ans

print(solution(["2023-01-01", "2022-01-15", "2023-02-20", "2023-01-01", "2023-02-28"]))