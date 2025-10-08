import matplotlib.pyplot as plt
import numpy as np

# Example Data

block_sizes = ["Sequential", "32", "48", "64", "128", "238" , "512", "1024"]
gpu_times = [0, 3059.99589 ,3796.21077, 2820.18805, 2829.96392, 3059.16715, 2870.72587, 2861.92298]  # Example times
transfer_times = [0, 1029.19698, 952.59023, 1051.10431, 1038.72895, 1108.10328, 943.57920, 1038.11288]  # Example transfer times
cpu_times = [ 152151.949883, 4176.62168,4429.39401, 4154.27732, 4201.76196, 4123.46697, 4243.48474, 4192.33537]  # Example CPU times


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
