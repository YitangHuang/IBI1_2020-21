import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
#  import the packages needed

os.chdir("E:/covid data/")      # change the working directory
covid_data = pd.read_csv("full_data.csv")        # import the data and read the .csv file
print(covid_data.info())                           # print all the columns.
print(covid_data.iloc[0:11:2, :])               # print every second row between 0 to 10 (including 0 and 10）

# define a function f to search in the dataset to find the corresponding data
# we can try different value of x so that we can get different data we want
def f(x):                 # define the function
    L = []                 # create a new empty list
    for i in range(0, 7996):                   # for loop is to search in the database
        if covid_data.iloc[i, 1] == x:          # If command is to check whether the data is consistent with the data we want
            a = True
        else:
            a = False                              # use a Boolean to show any kinds of data for all rows corresponding to what we want.
        L.append(a)
    return L                                        # return the results

world_new_cases = covid_data.loc[f("World"),"new_cases"]         # define the world_new_cases with the function(you can also say with Booleas)
mean = np.mean(world_new_cases)
median = np.median(world_new_cases)                                    # calculate the mean and the median using numpy
print('The mean of the world new cases is ', mean)
print('The median of the world new cases  is ', median)                    # output the mean and median of he world new cases

# making the boxplot
plt.boxplot(world_new_cases)            # create a boxplot
plt.xlabel('World dates')               # label the x
plt.ylabel('World new cases')            # label the y
plt.title('World Cases')                 # title the plot
plt.show()                                # show the boxplot


# making the plot
world_dates=covid_data.loc[f("World"),"date"]         # define the dates with function f
world_new_deaths=covid_data.loc[f("World"),"new_deaths"]            # define the number of new deaths with function f
plt.plot(world_dates,world_new_cases,label="new cases")             # making one curve and label it
plt.plot(world_dates,world_new_deaths,label="new deaths")          # making another curve and label it
plt.xticks(rotation=-90)                                           # flip the x-value to help the user better read the plot
plt.title("World new cases and new deaths by covid-19")             # title the plot
plt.legend()                                                       # enable the legend
plt.show()                                                         # show the box plot
# maximize the window to get the best view
# maximize the window to get the best view
# maximize the window to get the best view
# ---------------------------------------------------------------------------------------------------------------------------------------
# question part:
# How have new cases and total cases developed over time in Spain?
spain_new_cases = covid_data.loc[f("Spain"), "new_cases"]
spain_total_cases = covid_data.loc[f("Spain"), "total_cases"]
spain_dates=covid_data.loc[f("Spain"),"date"]         # define the dates with function f
plt.plot(spain_dates, spain_new_cases, label="new cases of Spain")             # making one curve and label it
plt.plot(spain_dates, spain_total_cases, label="total cases of Spain")          # making another curve and label it
plt.xticks(rotation=-90)                                           # flip the x-value to help the user better read the plot
plt.title("Spain new cases and total cases by covid-19")             # title the plot
plt.legend()                                                       # enable the legend
plt.show()                                                           # show the plot

# According to the plot,
# we can clear see that around 3/20/20, the infections began to appear in Spain.
# And then there was an increasing rate of total cases growth.
#  The number of new cases per day also increased overall, but declined slightly after the 26th.

