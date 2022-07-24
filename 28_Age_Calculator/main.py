
from datetime import datetime


def calculate_age():

    actual_year = datetime.now().year
    actual_month = datetime.now().month
    actual_day = datetime.now().day

    b_year = int(input("Enter your birthday year: ").strip())
    b_month = int(input("Enter your birthday month: ").strip())
    b_day = int(input("Enter your birthday day: ").strip())

    age_in_years = actual_year - b_year

    if b_month > actual_month:

        age_in_years = age_in_years - 1

    elif b_month == actual_month:
        if b_day >= actual_day:
            age_in_years = age_in_years

        else:
            age_in_years = age_in_years - 1

    elif b_month < actual_month:
        age_in_years = age_in_years

    print(age_in_years)


calculate_age()
calculate_age()
calculate_age()
calculate_age()
calculate_age()
calculate_age()
calculate_age()
