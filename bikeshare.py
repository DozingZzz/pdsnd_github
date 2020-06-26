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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    While True:
        try:
            city = input('Enter a city name (chicago, new york city, washington): ')
            city = city.lower()
            break
        except:
            print('That\'s not a valid city name.')

        finally:
            print('\nAttempted Input\n')


    # TO DO: get user input for month (all, january, february, ... , june)
    While True:
        try:
            month = input('Enter a month (january, february, ... , june, or all): ')
            month = month.lower()
            break
        except:
            print('That\'s not a valid month entry.')

        finally:
            print('\nAttempted Input\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    While True:
        try:
            day = input('Enter a day of week (all, monday, tuesday, ... sunday): ')
            day = day.lower()
            break
        except:
            print('That\'s not a valid day of week.')

        finally:
            print('\nAttempted Input\n')

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
    df = pd.read_csv(CITY_DATA.get(city))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month_name().str.lower()
    df['DOW']   = df['Start Time'].dt.day_name().str.lower()

    if month != 'all':
        df = df.loc[df['Month'] == month]

    if day != 'all':
        df = df.loc[df['DOW'] == day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is {}.'.format(df['Month'].mode()[0]))

    # TO DO: display the most common day of week
    print('The most common day of week is {}.'.format(df['DOW'].mode()[0]))

    # TO DO: display the most common start hour
    print('The most common start hour is {}.'.format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print(df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    round_trip = df['Start Station'] + ' - ' + df['End Station']
    print(round_trip.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print("Earliest year of birth is {}".format(df['Birth Year'].min()))
    print("Most recent year of birth is {}".format(df['Birth Year'].max()))
    print("Most common year of birth is {}".format(df['Birth Year'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
