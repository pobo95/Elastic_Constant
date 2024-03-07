import os
import numpy as np
from glob import glob
import matplotlib.pyplot as plt

# Function to extract last TotEng and Volume values from log file
def extract_last_values(log_file):
    # Initialize variables to store the last TotEng and Volume values
    last_tot_eng = []
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


    # Return the last extracted values
    return last_tot_eng, last_volume


def coeff():
    d = glob("*/")
    p = []
    energies = []  # Initialize data before the loop
    for i in range(0, len(d)):
        s = d[i]
        p.append(s[s.find('_')+1:s.find('/')])
        #===============================================
        # Use the log file directly in the current directory
        log_file = os.path.join(d[i], "log.lammps")

        if os.path.exists(log_file):
            last_tot_eng, _ = extract_last_values(log_file)
            energies.append(last_tot_eng) # Append last_tot_eng to energies list
 
            if "strain_0.00" in s:
                log_file = os.path.join(d[i], "log.lammps")
                if os.path.exists(log_file):
                   _, last_volume = extract_last_values(log_file)


    # Write energies to a file named "log_energy"
    with open("log_energy", "w") as f:
        for energy in energies:
            f.write(str(energy) + "\n")

    # Write volume to a file named "log_volume"
    with open("log_volume", "w") as f:
        f.write(f"{last_volume}\n")


    DataIn = np.loadtxt('log_energy')
    data=DataIn-np.amin(DataIn)

    Vol = np.loadtxt('log_volume')

    #===============================================
    pp=[float(k) for k in p]
    out=np.stack((np.array(pp), data), axis=-1)
    out2 = out[out[:,0].argsort()]
    np.savetxt('Result.txt', out2,fmt='%5.7f')
    x=out2[:,0]
    y=out2[:,1]/Vol
    z = np.polyfit(x,y,2)
    #=============================================
    constant=z[0]*160.2176621
    #==============================================
    poly=np.poly1d(z)
    new_x = np.linspace(x[0], x[-1])
    new_y = poly(new_x)
    valeur_T=x
    valeur_min=y
    yhat = poly(valeur_T)
    ybar = sum(valeur_min)/len(valeur_min)
    SST = sum((valeur_min - ybar)**2)
    SSreg = sum((yhat - ybar)**2)
    R2 = SSreg/SST
    image = 'plot.jpg'
    lege = 'R^2='+str(R2)
    #=================================
    plt.plot(x, y, "o", new_x, new_y)
    plt.legend([lege])
    plt.savefig(image)
    plt.close()
    return constant

