import matplotlib.pyplot as plt

# Data
num_threads_new = ['Serial', 1, 2, 4, 8, 16, 32, 64]
execution_time_new = [95.7318, 34.5155, 26.5464, 17.8797, 13.2704,12.5821, 12.7340, 16.5983]

# Convert all elements in num_threads_new to strings for compatibility
num_threads_new = list(map(str, num_threads_new))

# Bar colors: orange for Serial, blue for others
colors_new = ['orange'] + ['blue'] * (len(num_threads_new) - 1)

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(num_threads_new, execution_time_new, color=colors_new)

# Adding labels and title
plt.xlabel("Number of Threads", fontsize=12)
plt.ylabel("Execution Time (seconds)", fontsize=12)
plt.title("Execution Time vs Number of Threads (BSIZE = 128)", fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Save the plot as an image
plt.tight_layout()
plt.savefig("Execution_Time_vs_Threads_BSIZE128.png", dpi=300)
plt.show()
