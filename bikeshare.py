import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



MONTHS_DATA = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAYS_DATA = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    try:
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        while True:
            city = input('Please enter the name of the city you would like to analyze (Chicago, New York City or Washington) : ').lower()
            if city not in CITY_DATA:
                print('\nInvalid city name!\n')
                continue   
            else:
                break
     

        # TO DO: get user input for month (all, january, february, ... , june)
        while True:
            month = input('Which month would you like to analyze? January, Feburary, March, April, May, June or ALL : ').lower()
            if month not in MONTHS_DATA:
                print('\nInvalid month name!\n')
                continue   
            else:
                break

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        while True:
            day = input('Which day would you like to analyze? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or ALL : ').lower()
            if day not in DAYS_DATA:
                print('\nInvalid day name!\n')
                continue   
            else:
                break
        
        print('-'*40)
        print('Your selection is that\nCity : {} , Month : {} , Day : {} '.format(city.title(),month.title(),day.title()))
        print('-'*40)
        
        return city, month, day
        
    except Exception as e:
        print('An exception has been occurred : {}'.format(e))
    

        

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    try:
        df = pd.read_csv(CITY_DATA[city])
     
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name 
        df['hour'] = df['Start Time'].dt.hour

        # filter by month if applicable
        if month != 'all':
        # use the index of the months list to get the corresponding int
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = MONTHS_DATA.index(month) + 1 
    
            # filter by month to create the new dataframe
            df = df[df['month'] == month]

        # filter by day of week if applicable
        if day != 'all':
            # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day.title()] 
        return df
    except Exception as e:
        print('An exception has been occurred during loading data: {}'.format(e))

def time_stats(df, city):
    """Displays statistics on the most frequent times of travel according to city selected."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    try:
        common_month_num = df['Start Time'].dt.month.mode()[0]
        common_month = MONTHS_DATA[common_month_num-1].title()
        print('The most common month in', city.title(), 'is:', common_month.title())
    except Exception as e:
        print('An exception has been occurred while displaying most common moth : {}'.format(e))

    # TO DO: display the most common day of week
    try:
        common_day_of_week = df['day_of_week'].mode()[0]
        print('The most common weekday in', city.title(), 'is:',common_day_of_week.title())
    except Exception as e:
        print('An exception has been occurred while displaying most common moth day of week: {}'.format(e))


    # TO DO: display the most common start hour
    try:
        common_start_hour = df['hour'].mode()[0]
        print('The most common starting hour in', city.title(), 'is:',common_start_hour)
    except Exception as e:
        print('An exception has been occurred while displaying most common start hour: {}'.format(e))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df, city):
    """Displays statistics on the most common stations and trip according to city selected."""

    print('\nCalculating The Most common Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    try:
        common_start_station = df['Start Station'].mode()[0]
        common_start_station_amount = df['Start Station'].value_counts()[0]
        print('The most commonly used start station in', city.title(), 'is:',common_start_station, 'and was used', common_start_station_amount, 'times.')
    except Exception as e:
        print('An exception has been occurred while displaying most commonly used start station : {}'.format(e))
        
    # TO DO: display most commonly used end station
    try:
        common_end_station = df['End Station'].mode()[0]
        common_end_station_amount = df['End Station'].value_counts()[0]
        print('The most commonly used end station in', city.title(), 'is:',common_end_station, 'and was used', common_end_station_amount, 'times.')
    except Exception as e:
        print('An exception has been occurred while displaying most commonly used end station: {}'.format(e))
    
    # TO DO: display most frequent combination of start station and end station trip
    try:
        common_trip = df.loc[:, 'Start Station':'End Station'].mode()[0:]
        common_trip_amt = df.groupby(["Start Station", "End Station"]).size().max()
        print('The most frequent combination of start station and end station trip is:\n', common_trip, '\n and was driven', common_trip_amt,'times')
    except Exception as e:
        print('An exception has been occurred while displaying most frequent combination of start station and end station trip : {}'.format(e))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def trip_duration_stats(df, city):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    try:
        df['Time Delta'] = df['End Time'] - df['Start Time']
        total_time_delta = df['Time Delta'].sum()
        print('The total travel time :', total_time_delta)
    except Exeption as e:
        print('An exception has been occurred while displaying total travel time: {}'.format(e))
        
    # TO DO: display mean travel time
    try:
        total_mean = df['Time Delta'].mean()
        print('The mean travel time :', total_mean)
    except Exception as e:
        print('An exception has been occurred while displaying mean travel time: {}'.format(e))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        print('The counts of user types in', city.title(), 'are as follows:\n', df['User Type'].value_counts())
    except Exception as e:
        print('An exception has been occurred while displaying counts of user type: {}'.format(e))
        
    # TO DO: Display counts of gender
    try:
        print('The counts of gender in', city.title(), 'are as follows:\n',df['Gender'].value_counts())
    except Exception as e:
        print('An exception has been occurred while displaying counts of gender: {}'.format(e))
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()
        print('The earliest, most recent, and most common year of birth in', city.title(), 'is:\n' 'The earliest birth date is:', int(earliest_year),'\n' 'The most recent birth date is:', int(most_recent_year),'\n' 'The most common year of birth is:', int(most_common_year))
    except Exception as e:
        print('An exception has been occurred while displaying earliest, most recent, and most common year of birth: {}'.format(e))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    raw_data = 0

    try:

        while True:
            answer = input("Do you want to see the raw data? Please type Yes or No : ").lower()
            if answer not in ['yes', 'no']:
                print('\nInvalid answer!\n')
                continue
            elif answer == 'yes':
                print(df.iloc[raw_data : raw_data + 5])
                raw_data += 5
                while True :
                    again = input("Do you want to see more 5 lines of raw data? Please type Yes or No : ").lower()
                    if again not in ['yes', 'no']:
                        print('\nInvalid answer!\n')
                        continue
                    elif again == 'yes':
                        print(df.iloc[raw_data : raw_data + 5])
                        raw_data += 5
                    else:
                        break
                break
            else:
                break

           
    except Exception as e:
        print('An exception has been occurred while displaying raw data : {}'.format(e))
    
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, city)
        station_stats(df, city)
        trip_duration_stats(df, city)
        user_stats(df,city)
        
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()