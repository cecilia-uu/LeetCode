from collections import deque 
def getSecondaryinfluencerSum(g_nodes, g_from, g_to) -> int:
    # 1. draw the graph
    graph = {i: [] for i in range(1, g_nodes + 1)}
    for f, t in zip(g_from, g_to):
        graph[f].append(t)
        graph[t].append(f)
    # Helper function for DFS to find the farthest node and distance
    def dfs(node, visited):
        visited.add(node)
        max_dis, max_node = 0, node
        for neighbor in graph[node]:
            if neighbor not in visited:
                cur_dis, cur_node, _ = dfs(neighbor, visited)
                cur_dis += 1
                if cur_dis > max_dis:
                    max_dis, max_node = cur_dis, cur_node
        return max_dis, max_node, visited
    
    # 2. Find the farthest node from any node (let's start from node 1)
    _, farthest_node, _ = dfs(1, set())
    
    # 3. Perform DFS again from the farthest node to find the node at the other end of the longest path
    max_distance, second_farthest_node, _ = dfs(farthest_node, set())
    
    # 4. Now we have the longest path, and `second_farthest_node` is one end of it
    _, _, visited = dfs(second_farthest_node, set())
    
    # Calculate the sum of unvisited nodes
    unvisited = set(range(1, g_nodes + 1)) - visited
    return sum(unvisited)


g_nodes=4
g_from =[1,1,2]
g_to=[2,3,4]
print(getSecondaryinfluencerSum(g_nodes, g_from, g_to)) # 0
print(getSecondaryinfluencerSum(g_nodes=6, g_from=[1,1,2,2,5], g_to=[3,2,5,4,6])) # 4
print(getSecondaryinfluencerSum(g_nodes=5, g_from=[5,1,1,2,2], g_to=[4,2,3,4,5])) # 0