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
    print("I have this change in README.me to documentation branch")
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("City name: Chicago, New Yoek City or Washington").lower()
        if city not in  CITY_DATA:
            print("invalid")
            continue
        else:
            break
    
    while True:
        time = input("Are you think a month need to a filter?, day, all or none").lower()
        if time == "month":
            month = input("A month January, Feburary, March, April, May or June").lower()
            day = "all"
            break
        elif time == "day":
            month = "all"
            day = input("A day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday").lower()
            break
        
        elif time == "all":
            month = input("A month January, Feburary, March, April, May or June").lower()
            day = input("A day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday").lower()
            break
        
        elif time == "none":
            month = "all"
            day = "all"
            break
        else:
            input("FALSE WORD, try again")
            break
    
    print(city)
    print(month)
    print(day)
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
    df = pd.read_csv(CITY_DATA[city])
    
                     
    df["Start Time"] = pd.to_datetime(df["Start Time"])           
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()
                     
                     
    if month != "all":
       months = ["january", "february", "march", "april", "may", "june"]
       month = months.index(month) +1
       df = df[df["month"] == month]
                     
                     
                     
    if day != "all":
       df=df[df["day_of_week"] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
                     
    # TO DO: display the most common month
    common_month = df["month"].mode()[0]
    print(common_month)
                     
    # TO DO: display the most common day of week
    common_day_of_week = df["day_of_week"].mode()[0]
    print(common_day_of_week)

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    common_hour = df["hour"].mode()[0]
    print(common_hour)
                     
                     
                     
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df["Start Station"].mode()[0]
    print(common_start)
    
    # TO DO: display most commonly used end station
    common_end = df["End Station"].mode()[0]
    print(common_end)

    # TO DO: display most frequent combination of start station and end station trip
    df["combination"] = df["Start Time"] + " to " + df["End Station"]
    common_combination = df["combination"].mode()[0]
    print(common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = ["Trip Duration"].sum()
    print(total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = ["Trip Duration"].mean()
    print(mean_travel_time)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User type"].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if "Gender" in df:
                     gender = df["Gender"].value_counts()
                     print(gender)
    else:
        print("NO INFORMATION ABOUT THIS GENDER IN THIS CITY")
                

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth_Year" in df:
        earliest = df["Birth_Year"].min()
        print(earliest)
        most_recent = df["Birth_Year"].max()
        print(most_recent)
        most_common_year_of_birth = df["Birth_Year"].mode()[0]
        print(most_common_year_of_birth)
    else:
        print("NO INFORMATION ABOUT THIS BIRTH YEAR IN THIS CITY")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def data(df):
    raw_data = 0
    while True:
        answer = input("Have you need to see raw data? Yes or No").lower()
        if answer not in ["yes","no"]:
            answer = ("FALSE WORD, try again").lower()
        elif answer == "yes":
            raw_data += 5
            print(df.iloc[raw_data : raw_data + 5])
            try_again = input("Have you need see more? Yes or No").lower()
            if try_again == "no":
                break
            elif answer == "no":
                return
            
def main():
    city = ""
    month = ""
    day = ""
    while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)
        
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
              break


if __name__ == "__main__":
	     main()
