# import heapq
# def getMaximumThroughput(throughput, scaling_cost, budget) -> int:
#     n = len(throughput)
#     # Initialize a min-heap with (current throughput, index, scaling cost)
#     # Using throughput[i] at first as the effective throughput
#     pq = [(throughput[i], throughput[i], scaling_cost[i]) for i in range(n)]
    
#     # Convert the list into a heap structure
#     heapq.heapify(pq)

#     # Track the amount of budget spent
#     spent_budget = 0

#     # Continue scaling as long as the budget allows
#     while spent_budget < budget:
#         # Get the service with the current smallest throughput
#         current_effective_throughput, base_throughput, cost = heapq.heappop(pq)

#         # Calculate how many times we can scale this service with the remaining budget
#         max_possible_upgrades = (budget - spent_budget) // cost
        
#         # If no upgrades can be made, break out of the loop
#         if max_possible_upgrades == 0:
#             heapq.heappush(pq, (current_effective_throughput, base_throughput, cost))
#             break

#         # Perform as many upgrades as possible
#         spent_budget += cost
#         new_throughput = current_effective_throughput + base_throughput
        
#         # Push the upgraded service back into the heap
#         heapq.heappush(pq, (new_throughput, base_throughput, cost))

#     # The final bottleneck throughput of the pipeline is the minimum in the heap
#     return pq[0][0]


import math
def getMaximumThroughput(throughput, scaling_cost, budget) -> int:
    n = len(throughput)
    left, right = min(throughput), max(throughput) + budget
    res = left

    while left <= right:
        mid = (left + right) // 2

        total_cost = 0
        for i in range(n):
            if throughput[i] < mid:
                incre = mid - throughput[i]
                cost = math.ceil(incre / throughput[i]) * scaling_cost[i]
                total_cost += cost

                if total_cost > budget:
                    break
        
        if total_cost <= budget:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res

throughput=[4, 2, 7]
scaling_cost=[3, 5,6]
budget = 32

print(getMaximumThroughput(throughput, scaling_cost, budget))