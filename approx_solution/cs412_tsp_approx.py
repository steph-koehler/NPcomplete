# use simulated annealing
import random
import sys
import time


def nearest_neighbor_tour(graph, vertices):  # n^2
    visited = [False] * vertices
    start = random.choice(list(graph))
    tour = [start]  # start at vertex 0
    visited[start] = True
    for _ in range(vertices - 1):
        last = tour[-1]
        next_vertex = min(
            (v for v in range(vertices) if not visited[v]),
            key=lambda v: graph[last][v],
        )  # sorts the neighbors by edge weights
        tour.append(next_vertex)
        visited[next_vertex] = True
    tour.append(tour[0])  # return to start
    total_weight = calculate_tour_weight(tour, graph)
    return tour, total_weight


def adjust(tour, graph, weight):  # O(n^3)
    best_tour = tour[:]
    best_weight = weight
    improved = True
    n = len(tour)
    for i in range(1, n-2):  # runs n time
        while improved:  # runs up to n times (almost definitely less)
            improved = False
            j = random.randint(1, n - 2)
            while j == i :
                j = random.randint(1, n - 2)
            new_tour = best_tour[:]  
            temp = new_tour[i] 
            new_tour[i] = new_tour[j]
            new_tour[j] = temp 
            new_weight = calculate_tour_weight(new_tour, graph)  # runs n times
            if new_weight < best_weight:
                    best_tour = new_tour
                    best_weight = new_weight
                    improved = True
    return best_tour, best_weight


def calculate_tour_weight(tour, graph):
    weight = 0
    for i in range(len(tour) - 1):
        u = tour[i]
        v = tour[i + 1]
        weight += graph[u][v]
    return weight


def main():
    data = sys.stdin.read().strip().split("\n")
    vertices, edges = map(int, data[0].strip().split())
    graph = {i: {} for i in range(vertices)}
    vertex_map = {}
    rev_map = {}

    for line in data[1:]:  # O(n^2)
        u, v, weight = line.strip().split()
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

    best_weight = float('inf')
    best_tour = None
    start_time = time.time()
    # run in 45 seconds
    while time.time() - start_time < 45:
        tour, weight = nearest_neighbor_tour(graph, vertices)
        tour, weight = adjust(tour, graph, weight) 
        if weight < best_weight:
            best_weight = weight
            best_tour = tour

    print(f"{best_weight:.4f}")
    mapped_tour = [rev_map[vertex] for vertex in best_tour]
    print(' '.join(mapped_tour))


if __name__ == '__main__':
    main()
