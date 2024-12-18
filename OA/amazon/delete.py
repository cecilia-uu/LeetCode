def getMaximumCharge(charge, n):
    mx = charge[0]
    sumEven = sumOdd = 0
    for i in range(n):
        mx = max(mx, charge[i])
        if i % 2 == 0:
            sumEven += max(charge[i], 0)
        else:
            sumOdd += max(charge[i], 0)
    return mx if sumEven == 0 and sumOdd == 0 else max(sumOdd, sumEven)

# example
charge1 = [-2, 4, 3, -2, 1]
n1 = 5
print(getMaximumCharge(charge1, n1))

charge2 = [-3, 1, 4, -1, 5, -9]
n2 = 6
print(getMaximumCharge(charge2, n2))

charge3 = [-1, 3, 2]
n3 = 3
print(getMaximumCharge(charge3, n3))


