def getSecondaryInfluencerSum(g_nodes, g_from, g_to):
    # Write your code here
    # 1. graph
    graph = {i: [] for i in range(1, 1+g_nodes)}
    for f, t in zip(g_from, g_to):
        graph[f].append(t)
        graph[t].append(f)
    
    # 2. dfs: find the mx and sum of the primary influencers
    path = [0] * (1+g_nodes)
    
    def dfs(node, visited, dis, val):
        if node in visited: 
            return dis-1, val
        
        visited.add(node)
        max_dis = dis
        for nei in graph[node]:
            cur_dis, val = dfs(nei, visited, dis+1, val)
            if cur_dis > max_dis:
                max_dis = cur_dis
                val += nei
             
        return max_dis, val
    for i in range(1, 1+g_nodes):
        path[i], val = dfs(i, set(), 0, i)
        
    mx = max(path)
    node = 0
    for i in range(1, 1 + g_nodes):
        if path[i] == mx:
            node = i
            break
    
    # 3. find the ans
    _, val = dfs(node, set(), 0, node)
    return (1+g_nodes)*g_nodes//2 - val


g_nodes=4
g_from =[1,1,2]
g_to=[2,3,4]
print(getSecondaryInfluencerSum(g_nodes, g_from, g_to)) # 0
print(getSecondaryInfluencerSum(g_nodes=6, g_from=[1,1,2,2,5], g_to=[3,2,5,4,6])) # 4
print(getSecondaryInfluencerSum(g_nodes=5, g_from=[5,1,1,2,2], g_to=[4,2,3,4,5])) # 0