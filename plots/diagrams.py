import matplotlib.pyplot as plt

# Data for Coarse-Grain Locking (throughput for different thread counts, list sizes, and operation mixes)
data_coarse = {
    "threads": [1, 2, 4, 8, 16, 32, 64, 128],
    "100-0-0_1024": [1530.87, 1443.03, 1343.15, 1205.79, 533.96, 705.73, 563.39, 240.59],
    "80-10-10_1024": [2036.79, 1688.04, 965.41, 318.77, 302.24, 309.43, 239.10, 94.97],
    "20-40-40_1024": [1484.63, 1399.78, 735.42, 310.67, 199.93, 269.28, 161.49, 128.76],
    "0-50-50_1024": [1468.32, 1328.25, 728.62, 311.04, 283.75, 208.24, 219.20, 91.93],
    "100-0-0_8192": [151.04, 150.16, 143.29, 120.25, 111.79, 127.92, 127.08, 66.62],
    "80-10-10_8192": [75.16, 72.83, 69.30, 50.02, 37.19, 41.93, 31.18, 18.65],
    "20-40-40_8192": [85.86, 84.90, 74.90, 44.52, 33.14, 38.49, 28.21, 9.87],
    "0-50-50_8192": [91.18, 88.21, 77.91, 52.13, 33.01, 46.83, 31.79, 11.29]
}

# Serial Throughput for list_size = 1024 and 8192 (from the tables)
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
threads = data_coarse["threads"]
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
        data_with_serial = [serial_throughput] + data_coarse[key]  # Add serial data before the threads
        
        # Plot the data for the current scenario
        plt.plot(evenly_spaced_threads, data_with_serial, marker='o', label=scenario, color=scenario_colors[scenario])
    
    # Set the title, labels, and x-ticks
    plt.title(f"Coarse-Grain Locking Throughput (List Size = {list_size})")
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
