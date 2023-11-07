from typing import List
import math
from collections import defaultdict
import heapq


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    edges = defaultdict(list)
    for start, end, weight in times:
        edges[start].append((weight, end))
        
    queue = []
    heapq.heappush(queue, (0, k))
    visited = set()
    distance = defaultdict(lambda: math.inf)
    distance[k] = 0
    ans = 0
    
    while queue:
        cur_weight, cur_node = heapq.heappop(queue)
        
        if cur_node in visited:
            continue
        visited.add(cur_node)
        
        ans = max(ans, cur_weight)
        
        for nei_weight, nei_node in edges[cur_node]:
            cost = cur_weight + nei_weight
            if cost < distance[nei_node]:
                distance[nei_node] = cost
                heapq.heappush(queue, (cost, nei_node))
    return ans if len(visited) == n else -1
