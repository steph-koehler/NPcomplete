import random
import string

def get_vertex_name(index):
    """
    Generate vertex names based on the index (like a, b, c, ..., z, aa, ab, ac, ...)
    """
    base = string.ascii_lowercase  # 'a' to 'z'
    name = ''
    
    while index >= 0:
        name = base[index % 26] + name
        index = index // 26 - 1  # Adjust to move to the next "digit" in base 26

    return name

def generate_complete_graph(n, weight_range=(1, 10)):
    """
    Generate a complete graph with `n` vertices and weighted edges.
    The graph will be represented in the form:
    n m
    u v weight
    """
    edges = []
    
    # Generate all edges for a complete graph (undirected)
    for u in range(n):
        for v in range(u + 1, n):  # Avoid duplicate edges and self-loops
            weight = random.uniform(*weight_range)  # Random weight between weight_range
            u_name = get_vertex_name(u)
            v_name = get_vertex_name(v)
            edges.append((u_name, v_name, weight))
    
    # The number of edges in a complete graph with `n` vertices is n * (n - 1) / 2
    m = len(edges)
    
    # Output the graph in the required format
    print(f"{n} {m}")
    for u, v, weight in edges:
        print(f"{u} {v} {weight:.4f}")

# Example usage
generate_complete_graph(100)  # Adjust the number of vertices as needed
