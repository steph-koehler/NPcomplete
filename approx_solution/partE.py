# https://www.tutorialspoint.com/data_structures_algorithms/dsa_travelling_salesman_approximation_algorithm.htm 

# same inputs on min spanning tree and then analysis. good for error bounding. 
# Know that answer might not be completely right, but you know how much it can be wrong by
#     may have to create a whole bunch of test cases. 
#     run lower lound and approx solution on a bunch of test cases that the exact solution will not run on.

# add lightest remaining edge that isnt in the mst after it completes. needs enough edges to make full cycle. 
# changes from v-1 to v.
# you add lightest because you dont actually know which one to add and this is a lower bound

'''approx: perfrom prims alg on the graph -> in each iteration, find the vertex with the smallest key that hasn't been added to the mst,
          add the vertex to the mst, and then update the key and parent (parent stores the structure of the mst parent[v] is the parent vertex of v)
    -  add root note at the end
    -  calculate the cost, sum the cost
    -  print the order that they are visited, and the cost?'''

    # how to analyze the outcome? how does it compare to the output of the approx. solution?

import math


def dfs_preorder(tree, node, visited, path):
    visited[node] = True
    path.append(node)
    for child in tree[node]:
        if not visited[child]:
            dfs_preorder(tree, child, visited, path)

def min_key(key, mst_set):
    min_val = float('inf')
    min_idx = -1
    for v in range(len(key)):
        if not mst_set[v] and key[v] < min_val:
            min_val = key[v]
            min_idx = v
    return min_idx

# use prim's algorithm
def primMst(graph, n):
    key = [float('inf')] * n
    parent = [-1] * n
    key[0] = 0
    mst_set = [False] * n

    for _ in range(n):
        u = min_key(key, mst_set)
        mst_set[u] = True
        for v in graph[u]:
            if not mst_set[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u
    return parent

def tsp_approx(graph, rev_map):
    n = len(graph)
    parent = primMst(graph, n)

    # construct the mst as adjacency list
    mst = {i: [] for i in range(n)}
    for i in range(1, n):
        u, v = parent[i], i
        mst[u].append(v)
        mst[v].append(u)

    visited = [False] * n
    path = []
    # preorder traversal
    dfs_preorder(mst, 0, visited, path)

    # add root to end of path to form cycle
    path.append(path[0])

    # calculate total cost of path
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]

    # print cost rounded to 4 decimal places
    print(f"{cost:.4f}")

    # print order of stops visited
    print(" ".join(rev_map[v] for v in path))


def main():
    vertices, edges = map(int, input().strip().split())
    graph = {i: {} for i in range(vertices)}
    vertex_map = {}
    rev_map = {}
    for _ in range(edges):
        u, v, weight = input().strip().split()
        weight = float(weight)
        if u not in vertex_map:
            vertex_map[u] = len(vertex_map)
            rev_map[vertex_map[u]] = u
        if v not in vertex_map:
            vertex_map[v] = len(vertex_map)
            rev_map[vertex_map[v]] = v
        u_idx, v_idx = vertex_map[u], vertex_map[v]
        graph[u_idx][v_idx] = weight
        graph[v_idx][u_idx] = weight
    
    tsp_approx(graph, rev_map)

    
if __name__ == '__main__':
    main()