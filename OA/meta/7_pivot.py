def solution(numbers, pivot):
    # countGreater - strictly greater than pivot
    # countLess - strctly less than pivot
    # greater/smaller/tie
    countGreater, countLess = 0, 0
    for n in numbers:
        if n > pivot:
            countGreater += 1
        elif n < pivot:
            countLess += 1
    
    if countGreater > countLess:
        return "greater"
    elif countGreater < countLess:
        return "smaller"
    else:
        return "tie"

print(solution([1,3,0,-1,1,4,3], 2))
print(solution([3,4,5,1,0], 3))