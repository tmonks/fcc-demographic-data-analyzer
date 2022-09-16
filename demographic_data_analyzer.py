import pandas as pd

def make_pcnt(n):
    return round(n * 100, 1)


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    ### How many of each race are represented in this dataset? 
    # Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    ### What is the average age of men?
    average_age_men = df[df['sex'] == 'Male'].age.mean()
    average_age_men = round(average_age_men, 1)

    ### What is the percentage of people who have a Bachelor's degree?
    bachelors_mask = df['education'] == 'Bachelors'
    percentage_bachelors = make_pcnt(bachelors_mask.mean())

    ### What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

    # create a mask showing who has one of the advanced degrees
    advanced_degrees = ['Bachelors', 'Masters', 'Doctorate']
    advanced_degree_mask = df['education'].isin(advanced_degrees)

    # add a boolean column for whether salary is '>50K'
    df['over-50k'] = (df['salary'] == '>50K')

    # percentage with advanced degree and salary >50K
    higher_education_rich = (df[advanced_degree_mask]['over-50k']).mean()
    higher_education_rich = make_pcnt(higher_education_rich)

    ### What percentage of people without advanced education make more than 50K?

    # percentage without advanced degree and salary >50K
    lower_education_rich = (df[~advanced_degree_mask]['over-50k']).mean()
    lower_education_rich = make_pcnt(lower_education_rich)

    ### What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    ### What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    # create a mask of only the people working the minimum number of hours
    min_workers_mask = (df['hours-per-week'] == min_work_hours)

    # find the percentage of those making >50K
    rich_percentage = (df[min_workers_mask]['over-50k']).mean()
    rich_percentage = make_pcnt(rich_percentage)

    ### What country has the highest percentage of people that earn >50K?

    # Create a Series containing the percentage >50K in each country
    country_rich_pcnts = df.groupby('native-country')['over-50k'].mean()

    # get the max percentage 
    highest_earning_country_percentage = make_pcnt(country_rich_pcnts.max())

    # get the ID of the maximal row
    highest_earning_country = country_rich_pcnts.idxmax()

    # Identify the most popular occupation for those who earn >50K in India.
    india_rich_mask = (df['native-country'] == 'India') & (df['over-50k'])
    top_IN_occupation = df[india_rich_mask]['occupation'].value_counts().idxmax()

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
