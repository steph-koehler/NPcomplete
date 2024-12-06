# use simulated annealing
import random
import sys
import time

"""
def random_tour(graph, vertices):  # O(n)
    tour = list(range(vertices))
    random.shuffle(tour)  # shuffles the vertices to get a random order
    tour.append(tour[0])  # back to start

    # total_weight = sum(graph[tour[i]][tour[i+1]] for i in range(vertices))
    total_weight = calculate_tour_weight(tour, graph)

    return tour, total_weight
"""

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
        )
        tour.append(next_vertex)
        visited[next_vertex] = True
    tour.append(tour[0])  # return to start
    total_weight = calculate_tour_weight(tour, graph)
    return tour, total_weight



def adjust(tour, graph, weight, vertices):
    if vertices > 500 :
        sample_fraction = 0.3
    elif vertices > 200 :
        sample_fraction = 0.6
    else :
        sample_fraction = 1.0

    best_tour = tour[:]
    best_weight = weight
    improved = True
    n = len(tour)
    while improved:
        improved = False
        all_pairs = [(i, j) for i in range(1, n - 2) for j in range(i + 1, n - 1)]
        sampled_pairs = random.sample(all_pairs, int(len(all_pairs) * sample_fraction))

        for i, j in sampled_pairs:  # runs as a percent of the input times
            new_tour = best_tour[:]  # create a copy of best_tour
            # swap at positions i and j
            temp = new_tour[i] 
            new_tour[i] = new_tour[j]
            new_tour[j] = temp           
            new_weight = calculate_tour_weight_incremental(new_tour, graph, weight, i, j) # this changed
    
            # check if the new tour is better
            if new_weight < best_weight:
                best_tour = new_tour
                best_weight = new_weight
                improved = True

    return best_tour, best_weight


def calculate_tour_weight_incremental(tour, graph, weight, i, j):
    # get rid of old edges
    weight -= graph[tour[i-1]][tour[i]]
    weight -= graph[tour[j]][tour[j+1]]
    # add new edges
    weight += graph[tour[i-1]][tour[j]]
    weight += graph[tour[i]][tour[j+1]]

    return weight

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
        tour, weight = adjust(tour, graph, weight, vertices) 
        if weight < best_weight:
            best_weight = weight
            best_tour = tour

    best_weight = calculate_tour_weight(best_tour, graph)
    print(f"{best_weight:.4f}")

    mapped_tour = [rev_map[vertex] for vertex in best_tour]
    print(' '.join(mapped_tour))


if __name__ == '__main__':
    main()
