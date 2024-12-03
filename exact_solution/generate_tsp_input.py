import random

def generate_tsp_input(n):
    vertices = [chr(i) for i in range(97, 97 + n)]  # 'a', 'b', ...
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append(f"{vertices[i]} {vertices[j]} {random.uniform(1, 10):.2f}")

    with open("largeInput.txt", "w") as f:
        f.write(f"{n} {len(edges)}\n")
        f.write("\n".join(edges))

generate_tsp_input(12)
