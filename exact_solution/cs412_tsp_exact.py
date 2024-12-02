from itertools import permutations
import sys

def parse_input():
    """
    Parse input from stdin and create the cost matrix.
    Input format:
    - First line: number of vertices n and edges m
    - Next m lines: edge information in "u v w" format, where u and v are vertices and w is the weight
    """
    n, m = map(int, input().split())
    vertices = {}
    index = 0
    edges = []
    
    # Parse edge list
    for _ in range(m):
        u, v, w = input().split()
        w = float(w)
        if u not in vertices:
            vertices[u] = index
            index += 1
        if v not in vertices:
            vertices[v] = index
            index += 1
        edges.append((vertices[u], vertices[v], w))
    
    # Create cost matrix
    cost_matrix = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        cost_matrix[i][i] = 0  # No self-loops
    
    for u, v, w in edges:
        cost_matrix[u][v] = w
        cost_matrix[v][u] = w  # Undirected graph
    
    return n, cost_matrix, {v: k for k, v in vertices.items()}  # n, cost matrix, reverse vertex map


def calculate_cost(path, cost_matrix):
    """
    Calculate the total cost of a given path using the cost matrix.
    """
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += cost_matrix[path[i]][path[i + 1]]
    total_cost += cost_matrix[path[-1]][path[0]]  # Return to start
    return total_cost


def exact_tsp(n, cost_matrix):
    """
    Solve the TSP using brute force. Finds the exact optimal path and cost.
    """
    best_cost = float('inf')
    best_path = None

    for path in permutations(range(n)):
        cost = calculate_cost(path, cost_matrix)
        if cost < best_cost:
            best_cost = cost
            best_path = path

    return best_path, best_cost


import time

def main():
    n, cost_matrix, vertex_map = parse_input()
    
    # Measure runtime
    start_time = time.time()
    best_path, best_cost = exact_tsp(n, cost_matrix)
    end_time = time.time()
    runtime = end_time - start_time

    # Map indices back to vertex names
    best_path_named = [vertex_map[i] for i in best_path] + [vertex_map[best_path[0]]]

    # Print results
    print(f"{best_cost:.4f}")
    print(" ".join(best_path_named))

    # Save runtime data
    with open("runtime_data.txt", "a") as file:
        file.write(f"{n} {runtime:.4f}\n")

if __name__ == "__main__":
    main()
