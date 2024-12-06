import matplotlib.pyplot as plt
import os

# File paths for the results
approx_results_dir = "test_results"
exact_results_dir = "test_results"

# Collect results from output files
def collect_results(result_dir, extension):
    results = {}
    for file_name in os.listdir(result_dir):
        if file_name.endswith(extension):
            test_name = file_name.replace(extension, "")
            with open(os.path.join(result_dir, file_name), 'r') as f:
                try:
                    result_value = float(f.read().strip())
                    results[test_name] = result_value
                except ValueError:
                    print(f"Could not parse result for {file_name}")
    return results

# Load approximation and exact results
approx_results = collect_results(approx_results_dir, ".approx.out")
exact_results = collect_results(exact_results_dir, ".exact.out")

# Ensure both have the same keys
common_keys = set(approx_results.keys()) & set(exact_results.keys())
if not common_keys:
    print("No matching test cases found between the two sets of results.")
    exit()

# Extract common test case names and values
test_cases = sorted(common_keys)
approx_values = [approx_results[tc] for tc in test_cases]
exact_values = [exact_results[tc] for tc in test_cases]

# Plot results
plt.figure(figsize=(12, 6))
x_indices = range(len(test_cases))

plt.plot(x_indices, approx_values, label="Approximation Results", marker='o', color='skyblue')
plt.plot(x_indices, exact_values, label="Exact Results", marker='s', color='salmon')

# Customize the plot
plt.xlabel("Test Cases", fontsize=12)
plt.ylabel("Result Value", fontsize=12)
plt.title("Comparison of Approximation and Exact Program Results", fontsize=14)
plt.xticks(x_indices, test_cases, rotation=45, ha='right', fontsize=10)
plt.legend()
plt.tight_layout()

# Save and show the plot
plot_path = os.path.join(approx_results_dir, "results_comparison.png")
plt.savefig(plot_path)
print(f"Plot saved to {plot_path}")
plt.show()
