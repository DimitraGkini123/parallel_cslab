import matplotlib.pyplot as plt
import numpy as np

# Sequential execution time
seq_time = 14.1306  

# Number of processes
processes = [2, 4, 8, 16, 32, 64]  

# Execution times for each number of processes
times = [7.0946, 3.5594, 1.8048, 0.8990, 0.4624, 0.2549]  

# Compute speedup
speedups = [seq_time / total for total in times]

# Line Plot
plt.figure(figsize=(10, 6))
plt.plot(processes, speedups, marker='o', linestyle='-', color="skyblue", markerfacecolor='black', markersize=8)

# Labels and title
plt.xlabel("Number of processes")
plt.ylabel("Speedup")
plt.title("MPI Kmeans Speedup")
plt.xticks(processes)  # Set x-ticks to match the number of processes
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the plot
plt.show()
