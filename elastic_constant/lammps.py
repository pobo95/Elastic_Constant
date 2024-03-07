#Importing necessary libraries
import numpy as np

# Path to your log file
log_file = 'log.lammps'

# Initialize variables to store the last TotEng and Volume values
last_tot_eng = None
last_volume = None

# Read the log file line by line
with open(log_file, 'r') as file:
    for line in file:
        # Skip lines until the line containing the desired data format is reached
        if line.startswith("Step Temp TotEng PotEng KinEng Press Pxx Pyy Pzz Pyz Pxz Pxy Volume"):
            break
    
    # Now, iterate through the rest of the file
    for line in file:
        # Break the loop if the line contains "Loop time"
        if "Loop time" in line:
            break
        
        # Split the line by whitespace
        parts = line.split()
        
        # Extract TotEng and Volume values
        if len(parts) >= 13:
            last_tot_eng = float(parts[3])
            last_volume = float(parts[-1])

# Printing the last extracted values
print("Last TotEng value:", last_tot_eng)
print("Last Volume value:", last_volume)
