import matplotlib.pyplot as plt

# Data for Lazy Synchronization (throughput for different thread counts, list sizes, and operation mixes)
data_lazy = {
    "threads": [1, 2, 4, 8, 16, 32, 64, 128],
    "100-0-0_1024": [1561.44, 3110.83, 5982.78, 11071.61, 22114.89, 44227.15, 74198.00, 83426.93],
    "80-10-10_1024": [1906.54, 1793.41, 1386.58, 1810.66, 1300.08, 5268.07, 8163.98, 1316.44],
    "20-40-40_1024": [1503.52, 1403.49, 1263.78, 1711.05, 1119.93, 3794.37, 5990.93, 316.74],
    "0-50-50_1024": [1404.53, 1318.61, 1230.77, 1676.78, 1069.71, 3371.46, 5460.94, 256.86],
    "100-0-0_8192": [151.94, 302.40, 581.91, 1075.31, 2146.58, 4288.43, 8192.53, 8178.20],
    "80-10-10_8192": [59.77, 115.47, 216.03, 318.22, 493.79, 843.35, 869.87, 584.97],
    "20-40-40_8192": [63.32, 123.21, 230.79, 341.35, 500.55, 809.94, 926.49, 540.40],
    "0-50-50_8192": [65.98, 126.59, 237.01, 348.84, 499.71, 783.80, 874.17, 509.00]
}

# Correct Serial Throughput for Lazy Synchronization
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
threads = data_lazy["threads"]
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
        data_with_serial = [serial_throughput] + data_lazy[key]  # Add serial data before the threads
        
        # Plot the data for the current scenario
        plt.plot(evenly_spaced_threads, data_with_serial, marker='o', label=scenario, color=scenario_colors[scenario])
    
    # Set the title, labels, and x-ticks
    plt.title(f"Lazy Synchronization Throughput (List Size = {list_size})")
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
