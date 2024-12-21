import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datafiles = ["cooing_sample_C.txt","cooling_samp1_A.txt","cooling_samp2_A.txt", "cooling_sample_B.txt"]
dataframes = []

L1 =1.1
L2 =1.3
L = L1

#Cross section
S = L1*L2
def resistivity(R,S,L):
    R = np.array(R)
    return R*S/L
resistivity1 = []
# print(dataframes[0][:,1])
for i in range(len(datafiles)):
    rety = resistivity((dataframes[i][:,1]),S,L)
    resistivity1.append(rety)

name = ['Cooling Sample C', 'Cooling Sample A1','Cooling Sample A2', 'Cooling Sample B'] 
sub = [221,222,223,224]
plt.figure(figsize = (15,10), constrained_layout=True)
for i in range(len(datafiles)):
    plt.subplot(sub[i])
    plt.gca().set_title(name[i], fontsize = 16)
    ind = np.where( dataframes[i][:,0] != 0)[0]
    plt.plot(dataframes[i][:,0][ind], resistivity1[i][ind])
    plt.xlabel('Temps (K)', fontsize = 14)
    plt.ylabel(r'Resistivity $(m \Omega \cdot m)$',fontsize = 14)
    plt.xticks(fontsize = (14))
    plt.yticks(fontsize = (14))
    plt.grid()