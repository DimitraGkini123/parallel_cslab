import matplotlib.pyplot as plt
import numpy as np

# Data for Naive GPU KMeans
block_sizes = ["32", "48", "64", "128", "238", "512", "1024"]  # Exclude "Sequential" for speedup
seq_time = 67671.686888  # Sequential time (ms)
fulloffload_times = [3156.818151, 3234.960794 ,  2398.117065, 3712.370872,  4355.791092,  4223.322868, 4203.163147]
reduction_times = [ 4204.200029, 3418.098927,  2588.639021 , 2706.935883, 4308.304071 ,  4213.155031,  4198.495865 ]


fullofload_speedups = [seq_time / total for total in fulloffload_times]


reduction_speedups = [seq_time / total for total in reduction_times]


# Combined Speedup Bar Plot
x = np.arange(len(block_sizes))  # Bar positions
bar_width = 0.35  # Width of each bar

plt.figure(figsize=(12, 7))

# Naive Speedup Bars
plt.bar(x - bar_width / 2, fullofload_speedups, bar_width, label="all-gpu", color="skyblue", edgecolor="black")

# Transpose Speedup Bars
plt.bar(x + bar_width / 2, reduction_speedups, bar_width, label="all-gpu delta reduction", color="orange", edgecolor="black")

# Add labels and title
plt.xticks(x, block_sizes)
plt.xlabel("Block Size")
plt.ylabel("Speedup (Sequential / Total Time)")
plt.title("Speedup Comparison: all-gpu vs  all-gpu delta reduction")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
