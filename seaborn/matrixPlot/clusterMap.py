import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

cs_df = pd.read_csv('../computerSale.csv')

cs = cs_df.select_dtypes(include=np.number)

# sns.clustermap(cs)

sns.clustermap(cs,cmap='Blues' , standard_scale=1)

plt.show()