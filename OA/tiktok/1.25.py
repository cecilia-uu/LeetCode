# 1. class inheritance B
# 2. B
# 3. C
# 4. B
# 5. C ok
# 6. similar passwords

def is_similar_passwords(password_attempts, stored_passwords) -> list[int]:
    def is_similar(attempt, stored):
        if attempt == stored:
            return 1
        m, n = len(attempt), len(stored)
        half = m//2
        if m == n and m % 2 == 0:
            a1, a2 = attempt[:half], attempt[half:]
            s1, s2 = stored[:half], stored[half:]
            if a1 == s1 and a2 == s2 or a1 == s2 and a2 == s1:
                return 1
        return 0
    
    ans = []
    for a, s in zip(password_attempts, stored_passwords):
        ans.append(is_similar(a, s))
    return ans

print(is_similar_passwords(["abcd"], ["dcab"])) # [0]
print(is_similar_passwords(["ab"], ["dcab"])) # [0]
print(is_similar_passwords(["abcd"], ["cdab"])) # [1]

# 7.
from collections import defaultdict, deque

def count_viral_sequences(category_nodes, category_from, category_to, viral_val, k):
    # 构建邻接表
    adj = defaultdict(list)
    for i in range(len(category_from)):
        u = category_from[i]
        v = category_to[i]
        val = viral_val[i]
        adj[u].append((v, val))
        adj[v].append((u, val))
    
    def dfs(node, parent, length, has_viral):
        """递归 DFS 遍历所有可能的长度 k 路径"""
        if length == k:
            return 1 if has_viral else 0  # 只有至少有一条 viral = 1 的边才计数

        count = 0
        for neighbor, viral in adj[node]:
            if neighbor != parent:  # 防止回溯
                count += dfs(neighbor, node, length + 1, has_viral or (viral == 1))
            
        return count
    
    total = 0
    for i in range(category_nodes):
        total += dfs(i, -1, 1, False)
    return total

# 示例输入
category_nodes = 4
category_from = [0, 1, 2]
category_to = [1, 2, 3]
viral_val = [0, 1, 0]
k = 3

# 计算并输出结果
result = count_viral_sequences(category_nodes, category_from, category_to, viral_val, k)
print(result)  # 输出应为 4

# example2
category_nodes = 5
category_from = [0, 1, 1, 3]
category_to = [1, 2, 3, 4]
viral_val = [0, 1, 0, 1]
k = 3

# 计算并输出结果
result = count_viral_sequences(category_nodes, category_from, category_to, viral_val, k)
print(result)  # 6
            
