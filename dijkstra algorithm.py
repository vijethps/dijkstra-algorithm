import heapq
import sys
from collections import defaultdict

def dijkstra(graph,source,destination):
    priority_queue = []
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[source] = 0
    heapq.heappush(priority_queue,(0,source))
    while priority_queue:
        current_distance,current_node = heapq.heappop(priority_queue)
        if current_node == destination:
            return current_distance
        if current_distance > shortest_distances[current_node]:
            continue
        for neighbor,weight in graph[current_node]:
            distance = current_distance + weight
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(priority_queue,(distance,neighbor))
    return -1
def main():
    input_data = input().strip().split()
    index = 0
    N = int(input_data[index]); index +=1
    M = int(input_data[index]); index +=1
    graph = defaultdict(list)
    for _ in range(M):
        u = int(input_data[index]); index +=1
        v = int(input_data[index]); index +=1
        weight = int(input_data[index]); index +=1
        graph[u].append((v, weight))
        graph[v].append((u, weight))
    source = int(input_data[index]); index+= 1
    destination = int(input_data[index])
    result = dijkstra(graph,source,destination)
    print(result)

if __name__ == "__main__":
    main()
