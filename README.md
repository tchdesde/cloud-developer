# Exploring US Bike Share Data
In this project, I used Python to explore data related to bike share systems of three major cities — Chicago, New York City, and Washington, DC. I wrote the code to import the data and answer interesting questions about it by computing descriptive statistics. I also also wrote a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

# Datasets
The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

	Start Time (e.g., 2017-01-01 00:07:57)
	End Time (e.g., 2017-01-01 00:20:53)
	Trip Duration (in seconds - e.g., 776)
	Start Station (e.g., Broadway & Barry Ave)
	End Station (e.g., Sedgwick St & North Ave)
	User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

	Gender
	Birth Year

# Files
I used data provided by Motivate, a national bike share system provider. In order to run the program, the following files are needed.

	chicago.csv
	new_york_city.csv
	washington.csv

# Software
The program was written using:

	Python 3
	NumPy and Pandas were installed using Anaconda

# Statistics Computed
Following statistics are computed in this program : 

	Popular times of travel (i.e., occurs most often in the start time)
		most common month
		most common day of week
		most common hour of day

	Popular stations and trip
		most common start station
		most common end station
		most common trip from start to end (i.e., most frequent combination of start station and end station)

	Trip duration
		total travel time
		average travel time

	User info
		counts of each user type
		counts of each gender (only available for NYC and Chicago)
		earliest, most recent, most common year of birth (only available for NYC and Chicago)