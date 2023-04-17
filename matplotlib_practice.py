import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# x = np.arange(-10, 10, 0.01)

# plt.xlabel("x value")
# plt.ylabel("f(x) value")

# plt.axis([-5, 5, 0, 25])
# plt.xticks([i for i in range(-5, 5, 1)])
# plt.yticks([i for i in range(0, 27, 4)])

# plt.title("y = x^2 graph")

# plt.plot(x, x**2, label="trend")

# plt.legend()

# plt.show()

# x = np.arange(20)
# y = np.random.randint(0, 20, 20)

# # plt.axis([0, 20, 0, 20])
# plt.xticks(np.arange(0, 20, 2))
# plt.yticks([0, 5, 10, 15, 20])
# plt.title("Box plot of y")

# # plt.bar(x, y)
# plt.hist(y, bins=np.arange(0, 20, 2))
# plt.show()

# z = [100, 200, 300, 400]

# plt.pie(z, labels=['one', 'two', 'three', 'four'])
# plt.show()

# x = np.arange(0, 22, 2)
# y = np.random.randint(0, 20, 20)

# plt.hist(y, bins=x)
# plt.show()

# sns.kdeplot(y, shade=True)
# vote_df = pd.DataFrame({"name":["Andy", "Bob", "Cat"], "vote":[True, True, False]})

# vote_count = vote_df.groupby('vote').count()

# plt.bar(x=[False, True], height=vote_count["name"])
# sns.countplot(x=vote_df["vote"])

covid = pd.read_csv("country_wise_latest.csv")
# s = sns.catplot(x="WHO Region", y="Confirmed", data=covid, kind="violin")
# s.fig.set_size_inches(10, 6)

# sns.stripplot(x="WHO Region", y="Recovered", data=covid)

# sns.swarmplot(x="WHO Region", y="Recovered", data=covid)

# print(covid.corr())

sns.heatmap(covid.corr())

plt.show()