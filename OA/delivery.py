from collections import defaultdict
import heapq

def minimum_cost(map, source, target):
    mapping = defaultdict(list)
    for m in map:
        m = m.split(":")
        s, e, tool, cost = m
        mapping[s].append((e, int(cost), tool))

    pq = [(0, source)]
    visited = set()

    while pq:
        cost, country = heapq.heappop(pq)

        if country == target:
            return cost
        
        if country in visited:
            continue
        visited.add(country)

        for nei, delivery_cost, tool in mapping[country]:
            if nei not in visited:
                heapq.heappush(pq, (cost+delivery_cost, nei))
    return -1

map = ["US:UK:UPS:4", "US:UK:DHL:5", "UK:CA:FedEx:10" , "AU:JP:DHL:20", "US:UK:UPS:1"]
source = "US"
target = "UK"
print(minimum_cost(map, source, target))

source = "CA"
target = "AU"
print(minimum_cost(map, source, target))