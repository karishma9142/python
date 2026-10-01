import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

cs_df = pd.read_csv('../computerSale.csv')

sns.pairplot(cs_df ,hue='Sex' , palette='Blues')
plt.show()