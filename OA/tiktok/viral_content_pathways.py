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
    
    # BFS 预处理父节点
    parent = [ -1 ] * category_nodes  # 记录每个节点的父节点
    q = deque()
    q.append(0)  # 假设根节点是 0
    parent[0] = -1  # 根节点没有父节点

    while q:
        u = q.popleft()
        for v, val in adj[u]:
            if parent[v] == -1 and v != parent[u]:  # 避免重复访问父节点
                parent[v] = u
                q.append(v)
    
    # 动态规划表
    # dp[u][l][has_viral]：从节点 u 出发，长度为 l，是否包含病毒传播潜力为 1 的边的路径数量
    dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(category_nodes)]
    
    # 初始化：长度为 1 的路径
    for u in range(category_nodes):
        dp[u][1][0] = 1  # 长度为 1 的路径，没有 viral = 1 的边
    
    # 填充 dp 表
    for l in range(2, k + 1):  # 路径长度
        for u in range(category_nodes):  # 当前节点
            for v, val in adj[u]:  # 下一个节点
                if v == parent[u]:  # 避免回头路径
                    continue
                for prev_has_viral in [0, 1]:  # 之前是否包含 viral = 1 的边
                    if dp[u][l - 1][prev_has_viral]:
                        dp[v][l][prev_has_viral or (val == 1)] += dp[u][l - 1][prev_has_viral]
    
    # 计算结果：所有长度为 k 且包含至少一条 viral = 1 的边的路径数量
    total = 0
    for u in range(category_nodes):
        total += dp[u][k][1]
    
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