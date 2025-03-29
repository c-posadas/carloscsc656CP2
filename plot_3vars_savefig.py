"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot, and saves it to a file named "myplot.png"

Inputs: the named file "sample_data_3vars.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""

import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data
fname = "sample_data_3vars.csv"
df = pd.read_csv(fname, comment="#")
print(df)

# Extract column names
var_names = list(df.columns)
print("var names =", var_names)

# Extract problem sizes and metric data
problem_sizes = df[var_names[0]].values.tolist()
mflops = df[var_names[1]].values.tolist()       # MFLOP/s
bandwidth = df[var_names[2]].values.tolist()    # Memory Bandwidth (%)
latency = df[var_names[3]].values.tolist()      # Memory Latency (ns)

xlocs = [i for i in range(len(problem_sizes))]

# MFLOP/s Plot
plt.figure()
plt.title("MFLOP/s vs Problem Size")
plt.xticks(xlocs, problem_sizes)
plt.plot(mflops, "r-o")
plt.xlabel("Problem Sizes")
plt.ylabel("MFLOP/s")
plt.grid(axis='both')
plt.savefig("mflops_plot.png", dpi=300)
plt.show()  # Display the MFLOP/s plot

# Memory Bandwidth Utilization Plot
plt.figure()
plt.title("Memory Bandwidth Utilization")
plt.xticks(xlocs, problem_sizes)
plt.plot(bandwidth, "b-x")
plt.xlabel("Problem Sizes")
plt.ylabel("% Peak Bandwidth")
plt.grid(axis='both')
plt.savefig("bandwidth_plot.png", dpi=300)
plt.show()  # Display the Memory Bandwidth plot

# Memory Latency Plot
plt.figure()
plt.title("Memory Latency")
plt.xticks(xlocs, problem_sizes)
plt.plot(latency, "g-^")
plt.xlabel("Problem Sizes")
plt.ylabel("Latency (ns)")
plt.grid(axis='both')
plt.savefig("latency_plot.png", dpi=300)
plt.show()  # Display the Memory Latency plot

# EOF
