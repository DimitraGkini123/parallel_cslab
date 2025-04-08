import matplotlib.pyplot as plt
import numpy as np

# Data for Transpose GPU KMeans
block_sizes = ["Sequential", "32", "48", "64", "128", "238", "512", "1024"]
gpu_times = [0, 412.140775, 415.227103, 412.445712, 412.298036, 419.099307, 411.031055, 410.577154]  # GPU times
transfer_times = [0, 4.515719, 4.546189, 4.495096, 4.518819, 4.495406, 4.519558, 4.487491]  # Transfer times
cpu_times = [6901.863694, 136.153603, 136.311197, 134.935403, 134.236574, 135.018873, 135.332227, 135.354686]  # CPU times


# Stacked Bar Plot
x = np.arange(len(block_sizes))
plt.figure(figsize=(12, 7))
plt.bar(x, gpu_times, label="GPU Time", color="lightblue")
plt.bar(x, transfer_times, bottom=gpu_times, label="Transfer Time", color="orange")
plt.bar(x, cpu_times, bottom=np.array(gpu_times) + np.array(transfer_times), label="CPU Time", color="lightgreen")

# Add labels and title
plt.xticks(x, block_sizes)
plt.xlabel("Block Size")
plt.ylabel("Execution Time (ms)")
plt.title("Execution Time Breakdown (Transpose GPU KMeans)")
plt.legend()
plt.tight_layout()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
