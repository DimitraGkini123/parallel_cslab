import matplotlib.pyplot as plt
import numpy as np

# Data
processes= ["1", "2", "4", "8", "16", "32", "64"] 
times_openmp = [5.1689, 2.6082, 1.3649, 0.6908, 0.3791, 0.4035, 0.3478]
times_mpi =  [14.1306, 7.0946, 3.5594, 1.8048, 0.8990,0.4624, 0.2549]

# Bar width and x positions
width = 0.4
x = np.arange(len(processes))

# Create bar plot
plt.figure(figsize=(12, 6))
plt.bar(x - width/2,times_openmp, width, label="OpenMP", color="royalblue")
plt.bar(x + width/2, times_mpi, width, label="MPI", color="darkorange")

# Labels and formatting
plt.xticks(x, processes)
plt.xlabel(" Processes (cores)")
plt.ylabel("Total Execution Time (ms)")
plt.title("Comparison OpenMP and MPI")
plt.legend()
plt.tight_layout()
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show plot
plt.show()

