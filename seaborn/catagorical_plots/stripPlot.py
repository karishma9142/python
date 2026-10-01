import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

cs_df = pd.read_csv('../computerSale.csv')

sns.stripplot(x='Age' , y='Profit' , data = cs_df, hue='Sex', jitter=True,dodge=True)
plt.legend(loc=0)
plt.show()