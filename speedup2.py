import matplotlib.pyplot as plt
import numpy as np

# Data
block_sizes = ["32", "48", "64", "128", "238", "512", "1024"]  # Exclude "Sequential" for speedup
seq_time = 73645.657063 # Sequential time (ms)
times = [8802.838087, 10204.066038, 13932.308197, 13978.338957, 14711.920023, 15059.644938, 15298.150063]


# Compute total execution times for each block size


# Compute speedup for each block size
speedups = [seq_time / total for total in times]

# Bar Plot
plt.figure(figsize=(10, 6))
plt.bar(block_sizes, speedups, color="skyblue", edgecolor="black")
plt.xlabel("Block Size")
plt.ylabel("Speedup (Sequential / Total Time)")
plt.title("Speedup vs Block Size (Naive GPU)")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
