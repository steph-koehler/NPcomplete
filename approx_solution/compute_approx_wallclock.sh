#!/bin/bash

# Directories for test cases and results
TEST_CASE_DIR="plot_tests"  # Modify this to the desired test case directory
RESULTS_DIR="test_results"
mkdir -p $RESULTS_DIR

# Python scripts to run
APPROX_PROGRAM="./cs412_tsp_approx.py"  # Approximation program
EXACT_PROGRAM="../exact_solution/cs412_tsp_exact.py"    # Exact program

# Check if the programs exist
if [[ ! -f "$APPROX_PROGRAM" ]]; then
  echo "Error: Python program '$APPROX_PROGRAM' not found!"
  exit 1
fi

if [[ ! -f "$EXACT_PROGRAM" ]]; then
  echo "Error: Python program '$EXACT_PROGRAM' not found!"
  exit 1
fi

# Ensure the test case directory exists
if [[ ! -d "$TEST_CASE_DIR" ]]; then
  echo "Error: Test case directory '$TEST_CASE_DIR' not found!"
  exit 1
fi

# Files to store timing results
APPROX_TIMING_LOG="$RESULTS_DIR/approx_timing.log"
EXACT_TIMING_LOG="$RESULTS_DIR/exact_timing.log"

# Clear previous logs
> $APPROX_TIMING_LOG
> $EXACT_TIMING_LOG

# Process each test case
for TEST_FILE in "$TEST_CASE_DIR"/*; do
  if [[ -f "$TEST_FILE" ]]; then
    TEST_NAME=$(basename "$TEST_FILE")  # Get the test case name
    echo "Running test case: $TEST_NAME"
    
    # Run approximation program
    echo "Running $APPROX_PROGRAM on $TEST_NAME"
    START_TIME=$(date +%s.%N)
    python3 "$APPROX_PROGRAM" < "$TEST_FILE" > "$RESULTS_DIR/$TEST_NAME.approx.out"
    END_TIME=$(date +%s.%N)
    APPROX_ELAPSED_TIME=$(echo "$END_TIME - $START_TIME" | bc)
    echo "$TEST_NAME: $APPROX_ELAPSED_TIME seconds" >> "$APPROX_TIMING_LOG"

    # Run exact program
    echo "Running $EXACT_PROGRAM on $TEST_NAME"
    START_TIME=$(date +%s.%N)
    python3 "$EXACT_PROGRAM" < "$TEST_FILE" > "$RESULTS_DIR/$TEST_NAME.exact.out"
    END_TIME=$(date +%s.%N)
    EXACT_ELAPSED_TIME=$(echo "$END_TIME - $START_TIME" | bc)
    echo "$TEST_NAME: $EXACT_ELAPSED_TIME seconds" >> "$EXACT_TIMING_LOG"
  fi
done

# Generate a plot for the timing information
PLOT_SCRIPT="$RESULTS_DIR/plot_times.py"

# Create a Python script to plot the timing data
cat <<EOF > $PLOT_SCRIPT
import matplotlib.pyplot as plt

# Read timing logs
approx_data = []
exact_data = []

with open("$APPROX_TIMING_LOG", "r") as f:
    approx_data = [line.strip().split(":") for line in f]

with open("$EXACT_TIMING_LOG", "r") as f:
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
plot_path = "$RESULTS_DIR/execution_times_comparison.png"
plt.savefig(plot_path)
print(f"Plot saved to {plot_path}")
EOF

# Run the plotting script
python3 $PLOT_SCRIPT

echo "All test cases processed. Results, timing information, and plot saved in $RESULTS_DIR."
