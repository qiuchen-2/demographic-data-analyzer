import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men= df[df['sex'] == 'Male']['age']
    average_age_men = round(men.mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors= df[df['education']=='Bachelors']
    percentage_bachelors = round((len(bachelors['education'])/len(df['education']))*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_ed = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_ed =df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    higher_education_rich_nonpercent = higher_ed[higher_ed['salary'] == '>50K']
    lower_education_rich_nonpercent = lower_ed[lower_ed['salary'] == '>50K']

    higher_education_rich = round(len(higher_education_rich_nonpercent)/len(higher_ed)*100,1)
    lower_education_rich = round(len(lower_education_rich_nonpercent)/len(lower_ed)*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = round(len(num_min_workers[num_min_workers.salary == '>50K'])/len(num_min_workers)*100,1)

    # What country has the highest percentage of people that earn >50K?
    #List of countries with salary >50K count
    highest_earning_countries_list = df[df['salary'] == '>50K']['native-country'].value_counts()
    #Country counts in the dataframe
    country_count = df['native-country'].value_counts()
    #Salary over 50K in all those countries divided by all country counts to find country with highest earnings
    highest_earning_country = (highest_earning_countries_list/country_count*100).idxmax() #output is Iran

    #Percentage of people that earn 50K in Iran (highest_earning_country)
    total_in_highest_earning_country = df[df['native-country'] == 'Iran']
    highest_total_in_highest_earning_country = total_in_highest_earning_country[total_in_highest_earning_country['salary'] == '>50K']
    highest_earning_country_percentage = round(len(highest_total_in_highest_earning_country)/len(total_in_highest_earning_country)*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    #dataframe for filtering India
    India_df = df[df['native-country'] == 'India']
    # Count occupations
    occupation_count = India_df['occupation'].value_counts()
    # Count those that have salary over 50 K
    rich_in_India = India_df[India_df['salary'] == '>50K']
    # Count of occupations that have salary over 50K
    rich_occupation = rich_in_India['occupation'].value_counts()

    top_IN_occupation = rich_occupation.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
