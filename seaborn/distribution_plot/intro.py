import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cs_df = pd.read_csv('../computerSale.csv')

sns.distplot(cs_df['Age'] , kde=True , bins=5)
# sns.distplot(cs_df['Sale Price'])
plt.show()