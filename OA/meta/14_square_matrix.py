# n is odd
# 0/1/2
def calculate_changes(matrix, n, y_value, background_value):
    changes = 0
    center = n // 2
    
    # 遍历整个矩阵
    for i in range(n):
        for j in range(n):
            # 判断是否在 "Y" 形状内
            if (i == j and i <= center) or (i + j == n - 1 and i <= center) or (i >= center and j == center):
                # 该格子应该是 "Y" 的一部分
                if matrix[i][j] != y_value:
                    changes += 1
            else:
                # 该格子是背景部分
                if matrix[i][j] != background_value:
                    changes += 1
    return changes

def min_changes_to_form_y(matrix, n):
    # 定义所有可能的值
    values = [0, 1, 2]
    min_changes = float('inf')
    
    # 尝试所有的 Y 值和背景值组合
    for y_value in values:
        for background_value in values:
            if y_value != background_value:
                # 计算要变成当前组合需要的修改次数
                changes = calculate_changes(matrix, n, y_value, background_value)
                min_changes = min(min_changes, changes)
    
    return min_changes

# 示例使用：
matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]
n = 3
print(min_changes_to_form_y(matrix, n))  # 输出应该是最少的修改次数
