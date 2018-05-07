import pandas
data = pandas.read_csv("./ch06_tsmc.csv", index_col = "Date")
data.plot()
import matplotlib.pyplot as plt
plt.show()