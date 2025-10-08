import matplotlib.pyplot as plt
import numpy as np

# Example Data

block_sizes = ["Sequential", "32", "48", "64", "128", "238" , "512", "1024"]
gpu_times = [0, 618.847823*10,  773.089194*10, 1104.576111*10, 1115.328836*10, 1184.107900*10,  1206.266189*10, 1248.311424*10]  # Example times
transfer_times = [0,  6.540871*10, 6.711102*10, 7.500291*10, 7.285929*10, 7.273793*10, 6.772113*10,  7.316256*10]  # Example transfer times
cpu_times = [74820, 229.581881*10, 251.105785*10, 278.724766*10 ,282.789445*10, 285.081649*10, 293.129683*10, 289.178896*10 ]  # Example CPU times

# Stacked Bar Plot
x = np.arange(len(block_sizes))
plt.figure(figsize=(10, 6))
plt.bar(x, gpu_times, label="GPU Time", color="lightblue")
plt.bar(x, transfer_times, bottom=gpu_times, label="Transfer Time", color="orange")
plt.bar(x, cpu_times, bottom=np.array(gpu_times) + np.array(transfer_times), label="CPU Time", color="lightgreen")

# Add labels and title
plt.xticks(x, block_sizes)
plt.xlabel("Block Size")
plt.ylabel("Execution Time (ms)")
plt.title("Execution Time Breakdown (Naive GPU vs Sequential)")
plt.legend()
plt.tight_layout()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
