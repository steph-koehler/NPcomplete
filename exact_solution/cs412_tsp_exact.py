import sys
from itertools import permutations

def parse_input():
    """
    Parses the input to build a complete weighted graph.
    The input is read from standard input.
    """
    n, m = map(int, sys.stdin.readline().strip().split())
    vertices = set()
    graph = {}

    for _ in range(m):
        u, v, w = sys.stdin.readline().strip().split()
        w = float(w)
        vertices.add(u)
        vertices.add(v)
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = w
        graph[v][u] = w  # Undirected graph

    return list(vertices), graph


def tsp_exact(vertices, graph):
    """
    Computes the exact solution to the TSP problem using brute force.
    Returns the minimum cost and the corresponding path.
    """
    min_cost = float('inf')
    best_path = []
    permutation_count = 0  # Debugging: Count permutations

    for perm in permutations(vertices):
        permutation_count += 1
        cost = 0
        valid_path = True
        for i in range(len(perm)):
            u = perm[i]
            v = perm[(i + 1) % len(perm)]  # Wrap around to form a cycle
            if v in graph[u]:
                cost += graph[u][v]
            else:
                valid_path = False
                break
        if valid_path and cost < min_cost:
            min_cost = cost
            best_path = list(perm) + [perm[0]]  # Append start vertex to complete the cycle

    print(f"Total permutations processed: {permutation_count}")  # Debugging
    return min_cost, best_path



def main():
    vertices, graph = parse_input()
    min_cost, best_path = tsp_exact(vertices, graph)
    print(f"{min_cost:.4f}")
    print(" ".join(best_path))


if __name__ == "__main__":
    main()
