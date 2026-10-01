import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

cs_df = pd.read_csv('../computerSale.csv')

sns.countplot(x='Sex' , data=cs_df )
plt.show()