import matplotlib.pyplot as plt

# Read timing logs
approx_data = []
exact_data = []

with open("test_results/approx_timing.log", "r") as f:
    approx_data = [line.strip().split(":") for line in f]

with open("test_results/exact_timing.log", "r") as f:
    exact_data = [line.strip().split(":") for line in f]

# Extract test names and times
test_names = [d[0] for d in approx_data]
approx_times = [float(d[1].split()[0]) for d in approx_data]
exact_times = [float(d[1].split()[0]) for d in exact_data]

# Create the plot
plt.figure(figsize=(12, 6))
x_indices = range(len(test_names))

plt.bar(x_indices, approx_times, width=0.4, label="Approximation", color='skyblue', align='center')
plt.bar(x_indices, exact_times, width=0.4, label="Exact", color='salmon', align='edge')

# Customize the plot
plt.xlabel('Test Cases', fontsize=12)
plt.ylabel('Execution Time (seconds)', fontsize=12)
plt.title('Execution Times: Approximation vs Exact', fontsize=14)
plt.xticks(x_indices, test_names, rotation=45, ha='right', fontsize=10)
plt.legend()
plt.tight_layout()

# Save the plot
plot_path = "test_results/execution_times_comparison.png"
plt.savefig(plot_path)
print(f"Plot saved to {plot_path}")
