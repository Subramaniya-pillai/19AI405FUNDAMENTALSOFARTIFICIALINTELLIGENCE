from collections import defaultdict
from collections import deque

def bfs(graph, start, visited, path):
    queue = deque()
    path.append(start)
    queue.append(start)
    visited[start] = True
    while len(queue) != 0:
        tmp_node = queue.popleft()
        for neighbour in graph[tmp_node]:
            if not visited[neighbour]:
                path.append(neighbour)
                queue.append(neighbour)
                visited[neighbour] = True
    return path

graph = defaultdict(list)

# Get the number of nodes and edges from the user
n, e = map(int, input("Enter the number of nodes and edges: ").split())

print("Enter the edges: ")
for i in range(e):
    u, v = map(int, input().split())
    u, v = str(u), str(v)  # Convert to strings for node labels
    graph[u].append(v)
    graph[v].append(u)

start = input("Enter the starting node: ")
visited = defaultdict(bool)
path = []
traversed_path = bfs(graph, start, visited, path)
print("BFS Traversal Path:", traversed_path)
