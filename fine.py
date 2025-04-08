import matplotlib.pyplot as plt

# Data for Fine-Grain Locking (throughput for different thread counts, list sizes, and operation mixes)
data_fine = {
    "threads": [1, 2, 4, 8, 16, 32, 64, 128],
    "100-0-0_1024": [233.94, 306.98, 426.66, 512.53, 232.59, 117.22, 74.52, 2.73],
    "80-10-10_1024": [390.16, 241.06, 332.97, 491.61, 225.22, 239.54, 251.72, 5.76],
    "20-40-40_1024": [387.25, 241.16, 333.63, 496.85, 226.48, 247.87, 257.17, 5.40],
    "0-50-50_1024": [387.58, 241.52, 334.60, 495.64, 226.96, 242.27, 260.20, 9.92],
    "100-0-0_8192": [29.23, 50.64, 80.64, 161.94, 67.79, 31.94, 14.29, 0.29],
    "80-10-10_8192": [39.24, 38.09, 56.39, 85.84, 50.07, 54.35, 62.24, 0.30],
    "20-40-40_8192": [40.40, 35.28, 53.29, 82.16, 47.36, 59.53, 89.58, 0.30],
    "0-50-50_8192": [40.05, 35.15, 52.93, 81.11, 47.34, 58.95, 91.28, 0.33]
}

# Correct Serial Throughput for Fine-Grain Locking
serial_throughput_1024 = {
    "100-0-0": 1572.93,
    "80-10-10": 2062.37,
    "20-40-40": 1611.64,
    "0-50-50": 1513.32
}

serial_throughput_8192 = {
    "100-0-0": 152.41,
    "80-10-10": 67.43,
    "20-40-40": 81.64,
    "0-50-50": 89.17
}

# Data
threads = data_fine["threads"]
scenarios = ["100-0-0", "80-10-10", "20-40-40", "0-50-50"]
list_sizes = [1024, 8192]

# Define a color map for the scenarios
scenario_colors = {
    "100-0-0": 'b',  # Blue
    "80-10-10": 'g',  # Green
    "20-40-40": 'r',  # Red
    "0-50-50": 'c'   # Cyan
}

# Separate the plots into two individual figures
for list_size in list_sizes:
    # Create a new figure for each list size
    plt.figure(figsize=(8, 6))  # Adjust the figure size if necessary

    # Loop through each scenario to plot the data
    for scenario in scenarios:
        key = f"{scenario}_{list_size}"
        
        # Evenly spaced threads for x-axis (positions of the data points)
        evenly_spaced_threads = range(len(threads) + 1)  # Create space for serial execution (one extra point)
        
        # Add the serial throughput as the first data point
        serial_throughput = serial_throughput_1024[scenario] if list_size == 1024 else serial_throughput_8192[scenario]
        data_with_serial = [serial_throughput] + data_fine[key]  # Add serial data before the threads
        
        # Plot the data for the current scenario
        plt.plot(evenly_spaced_threads, data_with_serial, marker='o', label=scenario, color=scenario_colors[scenario])
    
    # Set the title, labels, and x-ticks
    plt.title(f"Fine-Grain Locking Throughput (List Size = {list_size})")
    plt.xlabel("Threads")
    plt.ylabel("Throughput (Kops/sec)")
    
    # Set the x-ticks to be evenly spaced and correspond to the actual threads, including the serial point
    plt.xticks(range(len(threads) + 1), ['Serial'] + [str(t) for t in threads])  # Add 'Serial' before threads
    
    # Add grid and legend
    plt.grid(True)
    plt.legend()

    # Adjust layout to prevent overlap and display the figure
    plt.tight_layout(pad=2.0)
    plt.show()
