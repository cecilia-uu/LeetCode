
def scorePoints(points, tokens: str) -> int:
    res = 0 if tokens[0] == "E" else points[0]
    n = len(points)
    
    for i in range(1, n):
        if tokens[i] == "T":
            res += points[i]
        if tokens[i] == tokens[i-1] == "T":
            res += 1
    return res

points = [3, 4, 5, 2, 3]
tokens = "TEETT"
print(scorePoints(points, tokens)) # 9

points = [3, 2, 1, 2, 2]
tokens = "ETTTE"
print(scorePoints(points, tokens)) # 7

points = [2, 2, 2, 2]
tokens = "TTTT"
print(scorePoints(points, tokens)) # 11

