import matplotlib.pyplot as plt
import numpy as np

# Data
block_sizes = ["Sequential", "32", "48", "64", "128", "238", "512", "1024"]
total_times_2d_allgpu = [152151.949883, 3442.425013, 4378.498793, 3350.590944, 3332.427025, 3573.184967, 3395.361185, 3357.845068]
total_times_32d_allgpu = [ 67171, 3127.661943 , 3253.356934 , 2398.874998 , 3687.193871, 4355.051041, 4222.842932, 4200.931072]

# Bar width and x positions
width = 0.4
x = np.arange(len(block_sizes))

# Create bar plot
plt.figure(figsize=(12, 6))
plt.bar(x - width/2, total_times_2d_allgpu, width, label="Total Time (2D)", color="royalblue")
plt.bar(x + width/2, total_times_32d_allgpu, width, label="Total Time (32D)", color="darkorange")

# Labels and formatting
plt.xticks(x, block_sizes)
plt.xlabel("Block Size")
plt.ylabel("Total Execution Time (ms)")
plt.title("Comparison of Total Execution Time (2D vs 32D) for allgpu")
plt.legend()
plt.tight_layout()
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show plot
plt.show()

