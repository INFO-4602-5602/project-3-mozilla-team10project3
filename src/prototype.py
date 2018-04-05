import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
import pandas as pd

data = pd.read_csv('region_vpn.csv')
plt.figure()
parallel_coordinates(data, 'Sub-Region')
plt.show()


