import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please select a city from the following options: Chicago, New York City, Washington: ").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        print("Invalid city. Please try again.")
        city = input("Please select a city from the following options: Chicago, New York City, Washington: ").lower()


    # get user input for month (all, january, february, ... , june)
    month = input("Please select a month from the following options: January, February, March, April, May, June: ").lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june']:
        print("Invalid month. Please try again.")
        month = input("Please select a month from the following options: January, February, March, April, May, June: ").lower()



    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please select a day of the week from the following options: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday: ").lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        print("Invalid day. Please try again.")
        day = input("Please select a day of the week from the following options: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday: ").lower()


    print('-'*40)
    return city, month, day


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
    df = pd.DataFrame(pd.read_csv(CITY_DATA[city]))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        df = df[df['month'] == months.index(month) + 1]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]




    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("MOST COMMON MONTH", df['month'].mode()[0])

    # display the most common day of week
    print("MOST COMMON DAY", df['day_of_week'].mode()[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("MOST COMMON HOUR", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    # df['Start Station'] = df['Start Station'].mode()[0]
    print("MOST COMMON START STATION", df['Start Station'].mode()[0])


    # display most commonly used end station
    # df['End Station'] = df['End Station'].mode()[0]
    print("MOST COMMON END STATION", df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'] + df['End Station']
    print("MOST COMMON START AND END STATION", df['Start End'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Total_Travel_Time = df['Trip Duration'].sum()
    print("TOTAL TRAVEL TIME(Days)", Total_Travel_Time / 86400) # display total travel time in days


    # display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print("MEAN TRAVEL TIME(Minutes)", Mean_Travel_Time / 60) # display mean travel time in minutes


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_Types= df['User Type'].value_counts().to_frame()
    print("COUNTS OF USER TYPES", user_Types)



    # Display counts of gender
    if "Gender" in df:
        print(df['Gender'].value_counts().to_frame())
    

    

    if "Birth Year" in df:
        # Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = int(df['Birth Year'].min())
        recent_birth_year = int(df['Birth Year'].max())
        most_common_year_of_birth = int(df['Birth Year'].mode()[0])
        print("EARLIEST YEAR OF BIRTH", earliest_year_of_birth)
        print("MOST RECENT YEAR OF BIRTH", recent_birth_year)
        print("MOST COMMON YEAR OF BIRTH", most_common_year_of_birth)

    else:
        print("No data available for this city" )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    print('\nYou can check the raw data below...\n')
    i = 0

    while True:
        user_input = input('Would you like to view the first 5 rows of data? Please enter "yes" or "no": ').lower()
        if user_input not in ['yes', 'no']:
            print('Sorry, please type "yes" or "no".')
        elif user_input != 'yes':
            print('Thank you.')
            break
        else:
            while i + 5 < df.shape[0]:
                print(df.iloc[i:i+5])
                i += 5
                user_input = input('Would you like to view the next 5 rows of data? Please enter "yes" or "no": ').lower()
                if user_input != 'yes':
                    print('Thank you.')
                    break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
