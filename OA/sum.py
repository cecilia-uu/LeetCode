def getSecondaryinfluencerSum(g_nodes, g_from, g_to) -> int:
    # 1. draw the graph
    graph = {i: [] for i in range(1, g_nodes + 1)}
    for f, t in zip(g_from, g_to):
        graph[f].append(t)
        graph[t].append(f)

    # 2. find the mx
    path = [0] * (1 + g_nodes)
    def dfs(node, visited, dis, val): 
        if node in visited:
            return dis - 1, val
        
        visited.add(node)
        max_dis = dis
        for neighbor in graph[node]:
            cur_dis, val = dfs(neighbor, visited, dis+1, val)
            if cur_dis > max_dis:
                max_dis = cur_dis
                val += neighbor
                # print(val)
        return max_dis, val
    
    for i in range(1, 1 + g_nodes):
        max_dis, val = dfs(i, set(), 0, i)
        # print(i, val)
        path[i] = max_dis

    print("path", path)
    mx = max(path)
    node = 0
    for i in range(1, 1 + g_nodes):
        if path[i] == mx:
            node = i
            break
    
    # 3. find the path
    _, val = dfs(node, set(), 0, node)
    
    return (1+g_nodes)*g_nodes//2 - val

print(getSecondaryinfluencerSum(g_nodes=4, g_from=[1,1,2], g_to=[2,3,4])) # 0
print(getSecondaryinfluencerSum(g_nodes=6, g_from=[1,1,2,2,5], g_to=[3,2,5,4,6])) # 4
print(getSecondaryinfluencerSum(g_nodes=5, g_from=[5,1,1,2,2], g_to=[4,2,3,4,5])) # 0