import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = {'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv'}
def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('Would you like to explore Chicago, New York City, or Washington? ').lower()
        if city not in CITY_DATA:
            print('Please choose a correct city name')

        else:
            break

    while True:
        month = input('Specify month of interest, type all for no filter: ').lower() 
        months = ['january','february','march','april','may','june']
        if month != 'all' and month not in months:
            print('Please enter a valid month name')
        else:
            break

    while True:
        day = input('Please specify the day of the week, or type "all" to display all days: ').lower()
        days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
        if day != 'all' and day not in days:
            print('Please enter valid day name')
        else:
            break
    print('-'*40)
    return city,month,day

def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.day_name

    if month != 'all':
       months = ['january','february','march','april','may','june']
       month = months.index(month) + 1
       df = df[df['month'] == month]

    if day != 'all':
       df = df[df['day'] == day.title()]
   

    return df

     
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
     # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month:',calendar.month_name[common_month])
    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print('Most Common day:',common_day)
    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common hour:',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most popular start station is:', popular_start_station)
   # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most popular End station is:', popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    start_end_station= (df['Start Station']+ ' - ' + df['End Station']).mode()[0]
    #Start_end_station = df.groupby(['Start Station','End Station']).value_counts()
    #Start_end_station = df.groupby(['Start Station','End Station']).count().idmax()[0]
    print('Most frequent combination of start and end station is:', start_end_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is:', total_travel_time,'seconds,or', total_travel_time/3600,'hours')
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel time is:',mean_travel_time,'seconds, or',mean_travel_time/3600, 'hours')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print ('Counts of User Types:\n', df['User Type'].value_counts());
    
    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('\n Counts of Gender:\n',df['Gender'].value_counts())
     
     # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_YOB = int(df['Birth Year'].min())
        print('\n Earliest year of birth:\n',earliest_YOB)
        Most_recent_YOB = int(df['Birth Year'].max())
        print('\n Most recent year of birth:\n',Most_recent_YOB)
        Most_common_YOB = int(df['Birth Year'].mode()[0])
        print('\n Most common year of birth:\n',Most_common_YOB)
        
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
        
        # TO DO: get user input for month (all, january, february, ... , june)
        restart = input('\n Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
        main()



### Source and guide - https://www.youtube.com/c/MikesCodingTutorials
