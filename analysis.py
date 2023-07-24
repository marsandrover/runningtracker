# load the packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load csv file
dataframe = pd.read_csv("stage_data.csv")
dataframe.head()
# prints the info from the csv file
print(dataframe.info())
print(dataframe.describe())
# explore the properties
plt.figure(figsize=(15, 19))
plt.hist(dataframe["rank"], bins=20, edgecolor="black")
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.title("Properties of Ranks for Various Stages")
plt.show()

# Explore the properties of ages of racers
plt.figure(figsize=(15, 10))
plt.hist(dataframe["age"], bins=20, edgecolor="blue")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Properties of Ages of Racers")
plt.show()

# Explore the correlation between rank and time
plt.figure(figsize=(15, 10))
plt.scatter(dataframe["rank"], dataframe["time"].dt.total_seconds(), alpha=0.10)
plt.xlabel("Rank")
plt.ylabel("Time (seconds)")
plt.title("Correlation between Rank and Time")
plt.show()
# handle missing values using drop rows
dataframe.dropna(inplace=True)

# convert elasped column to a timedata format
# this is easier for manipulation
dataframe["elapsed"] = pd.to_timedelta(dataframe["elapsed"])

# do the same except we are doing it for time
dataframe["time"] = pd.to_timedelta(dataframe["time"])

# we check if the first rows of the dataframe to verify changes
print(dataframe.head())
