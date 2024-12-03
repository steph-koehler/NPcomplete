import matplotlib.pyplot as plt

def plot_runtime(input_file, output_file="runtime_plot.png"):
    """
    Plot runtime data for TSP based on input file.

    Args:
        input_file (str): Path to the file containing runtime data.
                         Each line should be in the format: `num_cities runtime`.
        output_file (str): Path to save the output graph image.
    """
    # Read data from file
    num_cities = []
    runtimes = []

    with open(input_file, "r") as file:
        for line in file:
            try:
                cities, runtime = line.strip().split()
                num_cities.append(int(cities))
                runtimes.append(float(runtime))
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")

    # Plot the data
    plt.figure(figsize=(8, 6))
    plt.plot(num_cities, runtimes, marker="o", label="Measured Runtime")
    plt.xlabel("Number of Cities (n)")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime of TSP Exact Solution")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Save the plot
    plt.savefig(output_file)
    print(f"Runtime plot saved as '{output_file}'.")

    # Show the plot
    plt.show()

# Example usage
if __name__ == "__main__":
    input_file = "runtime_data.txt"  # Replace with your runtime data file
    plot_runtime(input_file)
