import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': "chicago.csv",
              'new york': "new_york_city.csv",
              'washington': "washington.csv"}
def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = city_info()
    month = month_info()
    day = day_info()

    return city,month,day
def city_info():
    while True:
        try:
            city = input('Would you like to explore Chicago, New York City, or Washington?\n').title()
            if city == 'Chicago' or city == 'chicago':
                        return 'chicago'
                    
            elif city == 'New York City' or city == 'new york city':
                    return 'new_york_city'
            elif city == 'Washington' or city == 'washington':
                    return 'washington'
            else:
                print('City names include: Chicago, New York City, or Washington')
        except  NameError:
              print('City names include: Chicago, New York City, or Washington')
        return city
                        # TO DO: get user input for month (all, january, february, ... , june)
def month_info():
    month = input("Specify month of interest, type all for no filter")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
def day_info():
    day = input("Day of the week, type all for no filter")
    print('-'*40)

 ##return city, month, day

def load_data(city, month, day):
    
    ##bikeshare['city'] = pd.read_csv(CITY_DATA[city])
    bikeshare = pd.read_csv(CITY_DATA[city])
    bikeshare['Start Time'] = pd.to_datetime(bikeshare['Start Time'])
    bikeshare['month'] = bikeshare['Start Time'].dt.month
    bikeshare['day']=bikeshare['Start Time'].dt.weekday_name

if month != 'all':
   months = ['january','february','march','april','may','june']
   month = months.index(month) + 1
   bikeshare = bikeshare[bikeshare['month'] == month]

else:
    pass

if day != 'all':
   bikeshare = bikeshare[bikeshare['day'] == day.title()]

#return bikeshare
def time_stats(bikeshare):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    bikeshare['month']=bikeshare['Start Time'].dt.month
    common_month = bikeshare['month'].mode()[0]
    print('Most Common Month:',common_month)
    # TO DO: display the most common day of week
    bikeshare['day_of_week']=bikeshare['Start Time'].dt.weekday_name
    common_day = bikeshare['day_of_week'].mode()[0]
    print('Most Common day:',common_day)
    # TO DO: display the most common start hour
    bikeshare['hour']=bikeshare['Start Time'].dt.hour
    common_hour = bikeshare['hour'].mode()[0]
    print('Most Common hour:',common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    popular_start_station = bikeshare['Start Station'].mode()[0]
    print('Most popular start station is:', popular_start_station)
   # TO DO: display most commonly used end station
    popular_start_station = bikeshare['End Station'].mode()[0]
    print('Most popular End station is:', popular_start_station)
    # TO DO: display most frequent combination of start station and end station trip
    Start_end_station = bikeshare.groupby(['Start Station','End Station']).value_counts()
    print('Most frequent combination of start and end station is:', start_end_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_travel_time = bikeshare['travel time'].sum()
    print('Total travel time is:', total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = bikeshare['travel time'].mean()
    print('Mean Travel time is:',mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types = bikeshare['User Type'].value_counts()
    print(user_types)
    # TO DO: Display counts of gender
    Gender = bikeshare['Gender'].value_counts()
    print(Gender)
    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_YOB = bikeshare['year of birth'].min()
    print('Earliest year of birth:',earliest_YOB)
    Most_recent_YOB = bikeshare['year of birth'].max()
    print('Most recent year of birth:',Most_recent_YOB)
    Most_common_YOB = bikeshare['year of birth'].mean()
    print('Most recent year of birth:',Most_common_YOB)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def main():
    while True:
        city, month, day = get_filters()
        bikeshare = load_data(city, month, day)
        time_stats(bikeshare)
        station_stats(bikeshare)
        trip_duration_stats(bikeshare)
        user_stats(bikeshare)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
        main()
