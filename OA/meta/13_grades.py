# list: 1-5 name: grade
# different grades
# highest average grade

from collections import defaultdict
def solution(records):
    grade = defaultdict(list)
    for r in records:
        name, g = r.split(":")
        g = int(g.strip())
        if name not in grade.keys():
            grade[name] = [g, 1]
        else:
            grade[name][0] += g
            grade[name][1] += 1
            
    ans = ""
    max_grade = 0
    for name, record in grade.items():
        r = record[0]//record[1]
        if r > max_grade:
            max_grade = r
            ans = name
    return ans

print(solution(["John: 5", "Michael: 4", "Ruby: 2", "Ruby: 5", "Michael: 5"]))