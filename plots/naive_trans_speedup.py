import matplotlib.pyplot as plt
import numpy as np

# Data for Naive GPU KMeans
block_sizes = ["32", "48", "64", "128", "238", "512", "1024"]  # Exclude "Sequential" for speedup
seq_time = 67671.686888  # Sequential time (ms)
naive_times = [8802.838087, 10204.066038, 13932.308197, 13978.338957, 14711.920023, 15059.644938, 15298.150063]
transpose_times = [ 5463.775873, 5493.335009, 5465.106964, 5507.776022,5550.864935, 5465.818882, 5464.527130 ]


naive_speedups = [seq_time / total for total in naive_times]


transpose_speedups = [seq_time / total for total in transpose_times]


# Combined Speedup Bar Plot
x = np.arange(len(block_sizes))  # Bar positions
bar_width = 0.35  # Width of each bar

plt.figure(figsize=(12, 7))

# Naive Speedup Bars
plt.bar(x - bar_width / 2, naive_speedups, bar_width, label="Naive GPU", color="skyblue", edgecolor="black")

# Transpose Speedup Bars
plt.bar(x + bar_width / 2, transpose_speedups, bar_width, label="Transpose GPU", color="orange", edgecolor="black")

# Add labels and title
plt.xticks(x, block_sizes)
plt.xlabel("Block Size")
plt.ylabel("Speedup (Sequential / Total Time)")
plt.title("Speedup Comparison: Naive vs Transpose GPU KMeans")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
