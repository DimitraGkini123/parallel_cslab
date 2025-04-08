import matplotlib.pyplot as plt

# Data for Optimistic Synchronization (throughput for different thread counts, list sizes, and operation mixes)
data_optimistic = {
    "threads": [1, 2, 4, 8, 16, 32, 64, 128],
    "100-0-0_1024": [643.44, 693.82, 775.93, 694.76, 205.70, 179.58, 326.47, 166.54],
    "80-10-10_1024": [901.34, 804.99, 640.82, 814.36, 509.26, 1765.44, 2517.69, 233.86],
    "20-40-40_1024": [881.90, 809.66, 660.78, 866.69, 538.48, 1777.85, 2464.77, 207.58],
    "0-50-50_1024": [878.83, 811.21, 663.96, 871.21, 544.20, 1680.88, 2398.26, 206.11],
    "100-0-0_8192": [71.64, 95.33, 131.46, 133.79, 77.11, 86.74, 126.54, 67.24],
    "80-10-10_8192": [33.36, 61.72, 113.38, 159.75, 231.09, 376.96, 412.24, 219.15],
    "20-40-40_8192": [30.50, 59.53, 111.39, 161.19, 235.91, 380.39, 439.94, 227.35],
    "0-50-50_8192": [29.84, 59.51, 110.34, 163.92, 237.21, 375.38, 412.82, 229.28]
}

# Correct Serial Throughput for Optimistic Synchronization
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
threads = data_optimistic["threads"]
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
        data_with_serial = [serial_throughput] + data_optimistic[key]  # Add serial data before the threads
        
        # Plot the data for the current scenario
        plt.plot(evenly_spaced_threads, data_with_serial, marker='o', label=scenario, color=scenario_colors[scenario])
    
    # Set the title, labels, and x-ticks
    plt.title(f"Optimistic Synchronization Throughput (List Size = {list_size})")
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
