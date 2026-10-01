import matplotlib.pyplot as plt
import numpy as np

# plot 📈

x = np.array([2023, 2024, 2025, 2026])
y = np.array([15, 25, 300, 20])
y2 = np.array([17,135,23,120])
y3 = np.array([40,230,450,153])

line_style = dict (marker=".",
    markersize=30,
    markerfacecolor="#31c7f5",
    markeredgecolor="#31c7f5",
    linestyle="solid",
    linewidth=3)

plt.title('Class Size' , fontsize = 25,
                         fontweight = 'bold',
                          family = 'Arial',
                          color = '#11379e')

plt.xlabel('Year' , fontsize = 25,
                         fontweight = 'bold',
                          family = 'Arial',
                          color = '#11379e')

plt.ylabel('Students' , fontsize = 25,
                         fontweight = 'bold',
                          family = 'Arial',
                          color = '#11379e')

plt.tick_params(axis="both" , colors = "#11379e")

plt.plot(
    x, y,**line_style
)

plt.plot(
    x, y2,**line_style
)

plt.plot(
    x,y3,**line_style
)

plt.xticks(x)

plt.show()