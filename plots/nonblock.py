import matplotlib.pyplot as plt

# Data for Non-blocking Synchronization (throughput for different thread counts, list sizes, and operation mixes)
data_non_blocking = {
    "threads": [1, 2, 4, 8, 16, 32, 64, 128],
    "100-0-0_1024": [737.75, 1467.55, 2804.14, 5119.38, 4373.67, 2794.47, 19777.20, 29752.51],
    "80-10-10_1024": [1050.75, 1404.85, 1368.37, 1927.91, 1472.14, 6235.36, 9177.41, 7212.78],
    "20-40-40_1024": [998.02, 1281.72, 1284.70, 1794.72, 1264.25, 4846.43, 8420.48, 4880.87],
    "0-50-50_1024": [969.29, 1250.75, 1266.25, 1755.52, 1229.42, 4491.66, 7498.16, 4416.07],
    "100-0-0_8192": [80.86, 177.15, 355.66, 648.33, 1313.06, 2619.88, 4964.47, 5006.40],
    "80-10-10_8192": [63.82, 123.43, 231.06, 328.10, 499.21, 853.37, 910.44, 609.03],
    "20-40-40_8192": [61.20, 120.38, 228.10, 339.44, 520.77, 842.50, 1036.83, 617.93],
    "0-50-50_8192": [61.20, 119.61, 225.84, 336.36, 503.69, 835.42, 905.76, 594.56]
}

# Correct Serial Throughput for Non-blocking Synchronization
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
threads = data_non_blocking["threads"]
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
        data_with_serial = [serial_throughput] + data_non_blocking[key]  # Add serial data before the threads
        
        # Plot the data for the current scenario
        plt.plot(evenly_spaced_threads, data_with_serial, marker='o', label=scenario, color=scenario_colors[scenario])
    
    # Set the title, labels, and x-ticks
    plt.title(f"Non-blocking Synchronization Throughput (List Size = {list_size})")
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
