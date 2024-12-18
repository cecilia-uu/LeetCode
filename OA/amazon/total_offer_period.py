def getTotalOfferPeriods(sales):
    n = len(sales)

    # 预处理所有区间内的最大值 O(n^2)
    max_middle = [[0] * n for _ in range(n)]
    for i in range(n):
        max_middle[i][i] = sales[i]
        for j in range(i+1, n):
            max_middle[i][j] = max(max_middle[i][j-1], sales[j])
    
    res = 0
    for start in range(n-2):
        for end in range(start+2, n):
            min_edge = min(sales[start], sales[end])
            max_middle_value = max_middle[start+1][end-1]

            if min_edge > max_middle_value:
                res += 1
    return res

# examples
sales = [5,2,1,3,6]
print(getTotalOfferPeriods(sales)) # 3

sales = [10, 6, 8, 5, 11, 9]
print(getTotalOfferPeriods(sales)) # 3

sales = [3,2,8,6]
print(getTotalOfferPeriods(sales)) # 1