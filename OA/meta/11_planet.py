# matrix
def solution(matrix) -> int:
    bottom, right = len(matrix), len(matrix[0])
    left, top = 0, 0
    res = []

    while left < right and top < bottom:
        # top row: left -> right
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1

        # right column: top -> bottom
        for i in range(top, bottom):
            res.append(matrix[i][right-1])
        right -= 1

        if not (left < right and top < bottom):
            break

        # bottom row: right -> left
        for i in range(right-1,left-1,-1):
            res.append(matrix[bottom-1][i])
        bottom -= 1

        # left column: bottom -> top
        for i in range(bottom-1, top-1, -1):
            res.append(matrix[i][left])
        left += 1

    print(res)
    ans = 0
    for i, n in enumerate(res):
        if i % 3 == 0:
            ans += n
    return ans

print(solution(matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]))
