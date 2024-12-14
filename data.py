import matplotlib.pyplot as plt
import matplotlib.style as style
import pandas as pd
from colorama.ansi import set_title

data = pd.read_csv('D:\pythonProject\master_metadata_index.csv',low_memory=False)

def subplotElectrodes (electrodes):

    style.use('dark_background')
    f, plt_arr = plt.subplots (len(electrodes), sharex=True, figsize=(10, 7))

    f.suptitle('Frequencies of Electrodes')

    for i in electrodes:

        plt_arr[(electrodes.index(i))].plot(data[i])

        plt_arr[(electrodes.index(i))].set_title(i)
    plt.tight_layout()
    plt.show()
filePath = 'D:\pythonProject\master_metadata_index.csv'
with open(filePath, 'r') as file:
    reader = pd.read_csv(file, nrows=1, header=None,low_memory=False)
    columns = reader.iloc[0,0:].tolist()
subplotElectrodes(columns)