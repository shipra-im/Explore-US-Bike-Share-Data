import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():#city,month,day):
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    month_comp = ['all','january','february','march','april','may','june']
    day_comp = ['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    #HINT: Use a while loop to handle invalid inputs
    flag=True
    while flag==True:
        print('get user input for city only like chicago, new york city or washington')
        city=input('Enter a city: ')
        city=city.lower()
        print(city)

    # get user input for month (all, january, february, ... , june)
        print('get user input for month  like all, january, february, ... , june')
        month=input('Enter a month: ')
        print(month)
        # get user input for day of week (all, monday, tuesday, ... sunday)
        print('get user input for day of week like all, monday, tuesday, ... sunday')
        day=input('Enter a day: ')
        print(day)
        #if ((city =='chicago' or city =='washington' or city == 'new york city')
            #and (month=='all' or month=='january'or month=='february' or month=='march'
                #or month=='april' or month=='may' or month=='june')
            #and (day=='all' or day=='monday' or day=='tuesday' or day=='wednesday'
                #or day=='thursday' or day=='friday' or day=='saturday' or day=='sunday')):
        if((city == 'chicago' or city == 'washington' or city == 'new york city') and (month.lower() in month_comp) and (day.lower() in day_comp)):
            print('i am here')
                  #return city, month, day
            city=city
            month=month.lower()
            day=day.lower()
            return city,month,day

        else:

            print('Entered wrong input.Please input as directed on screen ')
            print('')
            print('')
            city=''
            month=''
            day=''
            flag=False
            #get_filters()
    print('before returning func')
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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    #print('df when only month and day of week are extracted',df)
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        #print('month', month)
        # filter by month to create the new dataframe
        #print('df[month]',df['month'])
        df = df[df['month'] == month]
        #print('inside monthdf',df)

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        #print('inside day df ',df )
    #print('outside df',df)


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    #df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    most_common_month=df['month'].mode()[0]
    print('most common month',most_common_month)

    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    most_commom_weekday=df['day_of_week'].mode()[0]
    print('most common weekday',most_commom_weekday)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    #print(df['hour'])
    # find the most common hour (from 0 to 23)
    count=df['hour'].value_counts()
    #print(count)
    popular_hour = df['hour'].mode()[0]
    print('most common hour is',popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    max_station = df['Start Station'].value_counts().index.tolist()
    start_station_common_name = max_station[0]
    print('most common start station is',start_station_common_name)
    # display most commonly used end station
    end_station = df['End Station'].value_counts().index.tolist()
    end_station_commom_name = end_station[0]
    print('most common end station is',end_station_commom_name)
    # display most frequent combination of start station and end station trip
    trip_combination = df["Start Station"].astype(str) + " to " + df["End Station"].astype(str)
    popular_trip=trip_combination.describe()['top']
    print('most popular trip is',popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('total trip duration',df['Trip Duration'].sum())

    # display mean travel time
    print('mean travel time',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('the count of user types is\n',df['User Type'].value_counts())
    if city =='chicago' or city=='new york city':
    # Display counts of gender
        print('the counts of gender is',df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
        print('the most earliest year of birth is',df['Birth Year'].min())
        print('the most recent year of birth is',df['Birth Year'].max())
        print('the most common year of birth is',df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()

        if city == '' or month =='' or day=='':
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
        else:
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
        #added city parameter to below function
            user_stats(df,city)

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
	main()
