import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cs_df = pd.read_csv('../computerSale.csv')

sns.jointplot(y='Sale Price' , x='Profit' , data=cs_df , kind='hex')
plt.show()