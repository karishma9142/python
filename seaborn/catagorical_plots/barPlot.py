import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

cs_df = pd.read_csv('../computerSale.csv')

sns.barplot(x='Sex' , y='Age' , data=cs_df , estimator=np.median)
plt.show()