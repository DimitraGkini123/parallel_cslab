import matplotlib.pyplot as plt
import numpy as np

# Data
block_sizes = ["32", "48", "64", "128", "238", "512", "1024"]  # Exclude "Sequential" for speedup
seq_time = 73645.657063 # Sequential time (ms)
gpu_times = [6188.47823, 7730.89194, 11045.76111, 11153.28836, 11841.079, 12062.66189, 12483.11424]
transfer_times = [65.40871, 67.11102, 75.00291, 72.85929, 72.73793, 67.72113, 73.16256]
cpu_times = [2295.81881, 2511.05785, 2787.24766, 2827.89445, 2850.81649, 2931.29683, 2891.78896]

# Compute total execution times for each block size
total_times = [gpu + transfer + cpu for gpu, transfer, cpu in zip(gpu_times, transfer_times, cpu_times)]

# Compute speedup for each block size
speedups = [seq_time / total for total in total_times]

# Bar Plot
plt.figure(figsize=(10, 6))
plt.bar(block_sizes, speedups, color="skyblue", edgecolor="black")
plt.xlabel("Block Size")
plt.ylabel("Speedup (Sequential / Total Time)")
plt.title("Speedup vs Block Size (Naive GPU)")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
