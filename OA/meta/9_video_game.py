# deltas - health value change
# mini health value = 0, max = 100

def solution(deltas, initialHealth):
    # return final health
    if initialHealth < 0: initialHealth = 0
    for d in deltas:
        initialHealth += d
        if initialHealth < 0: 
            initialHealth = 0
        elif initialHealth > 100:
            initialHealth = 100
    return initialHealth

print(solution([-4,-12,6,2], 12))