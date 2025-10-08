import matplotlib.pyplot as plt
import numpy as np

# Data
processes= ["1", "2", "4", "8", "16", "32", "64"] 
times = [14.1306, 7.0946, 3.5594, 1.8048, 0.8990,0.4624, 0.2549]

# Bar Plot
plt.figure(figsize=(10, 6))
plt.bar(processes, times, color="skyblue", edgecolor="black")
plt.xlabel("Number of processes")
plt.ylabel("Execution Time")
plt.title("MPI Kmeans Execution Times ")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
