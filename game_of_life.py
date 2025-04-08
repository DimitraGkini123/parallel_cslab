import matplotlib.pyplot as plt
import numpy as np

# Δεδομένα
cores = [1, 2, 4, 6]
sizes = [64, 1024, 4096]
times = {
    64: [0.023105, 0.013586, 0.010090, 0.009024],
    1024: [10.980672, 5.465605, 2.725075, 1.831561],
    4096: [176.026231, 88.303525, 44.580126, 37.439299]
}

# Δημιουργία bar plot για Speedup
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
for i, size in enumerate(sizes):
    ax = axes[i]
    speedups = [times[size][0] / time for time in times[size]]  # Υπολογισμός βελτίωσης σε σχέση με 1 core
    ax.bar(cores, speedups, color=['blue', 'orange', 'green', 'red'])
    ax.set_title(f'Size {size}x{size}')
    ax.set_xlabel('Cores')
    ax.set_ylabel('Speedup (relative to 1 core)' if i == 0 else "")
    ax.set_xticks(cores)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.suptitle("Speedup for Different Grid Sizes and Core Counts", fontsize=16, y=1.02)
plt.show()

# Δημιουργία bar plot για Χρόνους Εκτέλεσης
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
for i, size in enumerate(sizes):
    ax = axes[i]
    ax.bar(cores, times[size], color=['blue', 'orange', 'green', 'red'])
    ax.set_title(f'Size {size}x{size}')
    ax.set_xlabel('Cores')
    ax.set_ylabel('Execution Time (s)' if i == 0 else "")
    ax.set_xticks(cores)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.suptitle("Execution Times for Different Grid Sizes and Core Counts", fontsize=16, y=1.02)
plt.show()
