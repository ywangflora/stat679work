homework 2: merging data files
==============================

# Background and target

- Data are collected every month from each system:
- hot water: hourly data on the hot water *temperature*
- electricity: daily data on the *energy* produced by a photovoltaic system.

- The goal of the exercise is to produce a script that could be used monthly
to merge the 2 data files of the month, where the energy value from each day
is matched to the temperature value at the nearest time, with no need for any
manual copy-paste operation. The script is meant to be used repeatedly,
so it should accept 2 file names as arguments:
the names of the temperature file and of the energy file.

# Process

##Firstly, I create a function called openfile.
- This function has two arguments, `waterfile` and `energyfile`. The first argument is the name of the waterTemperature csv file while the second argument is the name of the energy csv file. I want the function to do the following things.
- First thing is that I want the function to read the energyfile line by line and store all columns with several lists. What's more, I can check two things. The first one is whether all dates are at 00:00:00. If the assumption is broken, the console will print **the time is not all 00:00:00**. The second one is whether dates are ordered. If the assumption is broken, the console will print **the date is not ordered**. Additionally, with the time modulus, the time in energyfile should be changed to a standard time expression with strptime function.
- Second thing is that I want to function to read the waterfile line by line and store all columns with several lists. Additionally, with the time modulus, the time in waterfile should be changed to a standard time expression with strptime function.
- Then the function needs to compare times and choose the nearest match time. With the time modulus, I use mktime function to derive the difference between energy time and water time. Finally, I got two new columns. The first column is called **match**. It records all the match value divided by 1000. The second column is called **match_1000**. It records all the match value initially.
- Finally, the function needs to create an output called **output_hw2.csv** with the merged data, in csv format(comma-separated variables).

## How to derive the output file
- The python script I wrote is called `hw2_code.py`. If I want to run it in shell(suppose the first argument is `waterTemperature.csv` and the second argument is `energy.csv`), I can type in `python hw2_code.py waterTemperature.csv  energy.csv` in shell. The output file called **output_hw2.csv** will be created at the same working directory.
