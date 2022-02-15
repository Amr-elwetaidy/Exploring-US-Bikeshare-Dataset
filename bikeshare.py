from sys import exit
import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
I_HAVE_BEEN_CALLED = [False, False, False]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n* Hello! Let\'s explore some US bikeshare data!\n', '-' * 40, '\n')
    print('* Note: you can use 3 letter abbreviation (e.g., chi=chicago, mar=march, mon=monday)\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Choose a city to analyze (chicago, new york, washington): ').lower().strip()
        for C in CITY_DATA:
            if (city in C) and (len(city) >= 3) and (city[0:3] in C[0:3]):
                city = C
                break
        if city in CITY_DATA:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter the name of the month to filter by, or "all" to apply no month filter: ').lower().strip()
        if month == 'all':
            break
        for M in MONTHS:
            if (month in M) and (len(month) >= 3) and (month[0:3] in M[0:3]):
                month = M
                break
        if month in MONTHS:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter the name of the day of week to filter by, or "all" to apply no day filter: ').lower().strip()
        if day == 'all':
            break
        for D in DAYS:
            if (day in D) and (len(day) >= 3) and (day[0:3] in D[0:3]):
                day = D
                break
        if day in DAYS:
            break

    print('-' * 40)
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

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df['start_hour'] = pd.to_datetime(df['Start Time']).dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTHS.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # use the index of the days list to get the corresponding int
        day = DAYS.index(day) + 1

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\n* Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    if month == 'all' and day == 'all':
        print(f'Filters: City->{city}, Month->all, Day->all\n')
    elif month == 'all':
        print(f'Filters: City->{city}, Month->all, Day->{DAYS[df["day_of_week"].mode()[0] - 1]}\n')
    elif day == 'all':
        print(f'Filters: City->{city}, Month->{MONTHS[df["month"].mode()[0] - 1]}, Day->all\n')
    else:
        print(f'Filters: City->{city}, Month->{MONTHS[df["month"].mode()[0] - 1]}, Day->{DAYS[df["day_of_week"].mode()[0] - 1]}\n')

    # TO DO: display the most common month
    if month == 'all':
        print(f'Most popular month\t: {MONTHS[df["month"].mode()[0] - 1]}\t\tWith count: {df["month"].value_counts().max()}')

    # TO DO: display the most common day of week
    if day == 'all':
        print(f'Most popular day\t: {DAYS[df["day_of_week"].mode()[0] - 1]}\tWith count: {df["day_of_week"].value_counts().max()}')

    # TO DO: display the most common start hour
    print(f'Most popular hour\t: {df["start_hour"].mode()[0]}:00\t\tWith count: {df["start_hour"].value_counts().max()}')

    t1 = time.time() - start_time
    print("\nThis took %s seconds." % t1)
    print('-' * 40)
    return t1


def station_stats(df, city, month, day):
    """Displays statistics on the most popular stations and trip."""

    print('\n* Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    if month == 'all' and day == 'all':
        print(f'Filters: City->{city}, Month->all, Day->all\n')
    elif month == 'all':
        print(f'Filters: City->{city}, Month->all, Day->{DAYS[df["day_of_week"].mode()[0] - 1]}\n')
    elif day == 'all':
        print(f'Filters: City->{city}, Month->{MONTHS[df["month"].mode()[0] - 1]}, Day->all\n')
    else:
        print(f'Filters: City->{city}, Month->{MONTHS[df["month"].mode()[0] - 1]}, Day->{DAYS[df["day_of_week"].mode()[0] - 1]}\n')

    # TO DO: display most commonly used start station
    print(f'Most popular start station\t\t: {df["Start Station"].mode()[0]}\t\tWith count: {df["Start Station"].value_counts().max()}')

    # TO DO: display most commonly used end station
    print(f'Most popular end station\t\t: {df["End Station"].mode()[0]}\t\tWith count: {df["End Station"].value_counts().max()}')

    # TO DO: display most frequent combination of start station and end station trip
    print(f'Most popular start-end stations\t: {df[df["Start Station"] == df["End Station"]]["Start Station"].mode()[0]}\t\tWith count: {df[df["Start Station"] == df["End Station"]]["Start Station"].value_counts().max()}')

    t2 = time.time() - start_time
    print("\nThis took %s seconds." % t2)
    print('-' * 40)
    I_HAVE_BEEN_CALLED[0] = True
    return t2


def trip_duration_stats(df, city, month, day):
    """Displays statistics on the total and average trip duration."""

    print('\n* Calculating Trip Duration...\n')
    start_time = time.time()

    if month == 'all' and day == 'all':
        print(f'Filters: City->{city}, Month->all, Day->all\n')
    elif month == 'all':
        print(f'Filters: City->{city}, Month->all, Day->{DAYS[df["day_of_week"].mode()[0] - 1]}\n')
    elif day == 'all':
        print(f'Filters: City->{city}, Month->{MONTHS[df["month"].mode()[0] - 1]}, Day->all\n')
    else:
        print(f'Filters: City->{city}, Month->{MONTHS[df["month"].mode()[0] - 1]}, Day->{DAYS[df["day_of_week"].mode()[0] - 1]}\n')

    # TO DO: display total travel time
    print(f'Total travel time\t: {df["Trip Duration"].sum()}')

    # TO DO: display mean travel time
    print(f'Mean travel time\t: {df["Trip Duration"].mean()}')

    t3 = time.time() - start_time
    print("\nThis took %s seconds." % t3)
    print('-' * 40)
    I_HAVE_BEEN_CALLED[1] = True
    return t3


def user_stats(df, city, month, day):
    """Displays statistics on bikeshare users."""

    print('\n* Calculating User Stats...\n')
    start_time = time.time()

    if month == 'all' and day == 'all':
        print(f'Filters: City->{city}, Month->all, Day->all\n')
    elif month == 'all':
        print(f'Filters: City->{city}, Month->all, Day->{DAYS[df["day_of_week"].mode()[0] - 1]}\n')
    elif day == 'all':
        print(f'Filters: City->{city}, Month->{MONTHS[df["month"].mode()[0] - 1]}, Day->all\n')
    else:
        print(
            f'Filters: City->{city}, Month->{MONTHS[df["month"].mode()[0] - 1]}, Day->{DAYS[df["day_of_week"].mode()[0] - 1]}\n')

    # TO DO: Display counts of user types
    print(f'User types:\nSubscriber\t: {df[df["User Type"] == "Subscriber"]["User Type"].count()}')
    print(f'Customer\t: {df[df["User Type"] == "Customer"]["User Type"].count()}')

    if city != 'washington':
        # TO DO: Display counts of gender
        print(f'\nGender:\nMale\t: {df[df["Gender"] == "Male"]["Gender"].count()}')
        print(f'Female\t: {df[df["Gender"] == "Female"]["Gender"].count()}\n')

        # TO DO: Display earliest, most recent, and most common year of birth
        print(f'Earliest year of birth\t\t: {df["Birth Year"].min()}')
        print(f'Latest year of birth\t\t: {df["Birth Year"].max()}')
        print(f'Most common year of birth\t: {df["Birth Year"].mode()[0]}')

    t4 = time.time() - start_time
    print("\nThis took %s seconds." % t4)
    print('-' * 40)
    I_HAVE_BEEN_CALLED[2] = True
    return t4


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        t1 = time_stats(df, city, month, day)

        t2, t3, t4, restart = 0, 0, 0, 'no'

        while True:
            print('* if you want to see more stats type \"next\"...')
            print('* if you want to restart type \"yes\"...')
            print('* if you want to exit type \"no\"...')
            status = input().lower().strip()
            print('-' * 40)
            if status == 'next':
                if not I_HAVE_BEEN_CALLED[0]:
                    t2 = station_stats(df, city, month, day)
                    continue
                elif not I_HAVE_BEEN_CALLED[1]:
                    t3 = trip_duration_stats(df, city, month, day)
                    continue
                elif not I_HAVE_BEEN_CALLED[2]:
                    t4 = user_stats(df, city, month, day)
                    break
            elif status == 'yes':
                restart = 'yes'
                break
            elif status == 'no':
                print(f"\n{'-' * 40}\nTotal time is {t1 + t2 + t3 + t4} seconds.\n{'-' * 40}")
                exit(0)

        print(f"\nTotal time is {t1 + t2 + t3 + t4} seconds.\n{'-' * 40}")
        if restart == 'no':
            restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        I_HAVE_BEEN_CALLED[0:3] = False, False, False


if __name__ == "__main__":
    main()
