import matplotlib.pyplot as plt
import numpy as np

# Data
block_sizes = ["Sequential", "32", "48", "64", "128", "238", "512", "1024"]
total_times_2d = [152151.949883, 8265.897989, 9178.273916, 8025.648832, 8070.544004, 8290.822983, 8057.861805, 8092.447042]
total_times_32d = [ 67171,8802.838087, 10204.066038, 13932.308197, 13978.338957, 14711.920023, 15059.644938, 15298.150063]

total_times_tranpose_2d =[153163.781881,  5900.572777,7275.214195,  6128.694057 ,  6155.532837,  6363.370895,  6163.568020, 6533.499002]
total_times_tranpose_32d = [74820.519209 , 5463.775873, 5493.335009, 5465.106964, 5507.776022,5550.864935, 5465.818882, 5464.527130 ]
# Bar width and x positions
width = 0.4
x = np.arange(len(block_sizes))

# Create bar plot
plt.figure(figsize=(12, 6))
plt.bar(x - width/2, total_times_2d, width, label="Total Time (2D)", color="royalblue")
plt.bar(x + width/2, total_times_32d, width, label="Total Time (32D)", color="darkorange")

# Labels and formatting
plt.xticks(x, block_sizes)
plt.xlabel("Block Size")
plt.ylabel("Total Execution Time (ms)")
plt.title("Comparison of Total Execution Time (2D vs 32D)")
plt.legend()
plt.tight_layout()
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show plot
plt.show()

width = 0.4
x = np.arange(len(block_sizes))

# Create bar plot
plt.figure(figsize=(12, 6))
plt.bar(x - width/2, total_times_tranpose_2d, width, label="Total Time (2D)", color="royalblue")
plt.bar(x + width/2, total_times_tranpose_32d, width, label="Total Time (32D)", color="darkorange")

# Labels and formatting
plt.xticks(x, block_sizes)
plt.xlabel("Block Size")
plt.ylabel("Total Execution Time (ms)")
plt.title("Comparison of Total Execution Time (2D vs 32D)")
plt.legend()
plt.tight_layout()
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show plot
plt.show()
