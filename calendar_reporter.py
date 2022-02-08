from datetime import *
import calendar

users = [
    {
        "name":"Bill",
        "birthday": date(1998, 2, 9)
    },
    {
        "name":"Giil",
        "birthday":date(1999, 2, 10)
    },
    {
        "name":"Till",
        "birthday":date(2000, 2, 15)
    },
    {
        "name": "Nora",
        "birthday": date(1990, 2, 12)
    },
    {
        "name": "Gala",
        "birthday": date(1999, 2, 24)
    },
    {
        "name": "Tom",
        "birthday": date(2000, 2, 13)
    }
]

def get_birthdays_per_week(users):
    today = date.today()
    last_day = today + timedelta(weeks=1)
    #get the list of the dates of the next week
    modified_day = today
    next_week_dates = [today]
    while modified_day < last_day:
        modified_day += timedelta(days=1)
        next_week_dates.append(modified_day)

    birthdays_of_the_week = {"Monday":[],"Tuesday":[],
                             "Wednesday":[],"Thursday":[],
                             "Friday":[],"Saturday":[],
                             "Sunday":[]
                             }

    for user in users:
        try:
            birthday_this_year = user["birthday"].replace(year=today.year)
        except ValueError:
            birthday_this_year = user["birthday"].replace(year=today.year, day = 28)


        if birthday_this_year in next_week_dates:
            if calendar.day_name[birthday_this_year.weekday()] in birthdays_of_the_week:
                birthdays_of_the_week[calendar.day_name[birthday_this_year.weekday()]].append(user['name'])

    # move birthdays from Sunday and Saturday to Monday
    for day, names in birthdays_of_the_week.items():
        if day == "Sunday" or day == "Saturday":
            birthdays_of_the_week["Monday"].extend(names)

    # make output
    for day, names in birthdays_of_the_week.items():
        if names != [] and day != "Sunday" and day != "Saturday":
            names_str = str(names)[1:-1].replace('"', '').replace("'", '')
            print('{:<10} : {:<10} '.format(day, names_str))



get_birthdays_per_week(users)