from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users):
    today = date.today()
    horizon = today + timedelta(days=7)
    result = []

    for user in users:
        # Parse DOB and set to this year (handle Feb 29 on leap year → Mar 1)
        try:
            dob = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            bday = dob.replace(year=today.year)
        except ValueError:  #Feb 29 in a non-leap year
            bday = date(today.year, 3, 1)

        # If this year's birthday already passed, use next year
        if bday < today:
            try:
                bday = dob.replace(year=today.year + 1)
            except ValueError:
                bday = date(today.year + 1, 3, 1)

        # Consider only birthdays within [today, today+7]
        if today <= bday <= horizon:
            dow = bday.weekday()
            # Shift to next Monday if weekend: Sat→+2, Sun→+1
            if dow >= 5:
                shift = (7 - dow) % 7  
            else: 
                shift = 0
            congrats = bday + timedelta(days=shift)

            result.append({
                "name": user["name"],
                "congratulation_date": congrats.strftime("%Y.%m.%d"),
            })

    return result


users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Pol Smith", "birthday": "1990.10.11"},
        {"name": "John Smith", "birthday": "1990.07.6"},
        {"name": "Kate Roe", "birthday": "1994.10.17"},
        {"name": "Nate Boe", "birthday": "1994.10.18"},
        {"name": "Nate Woe", "birthday": "1994.10.19"},
        {"name": "Jane Trinity", "birthday": "1990.07.10"},
        {"name": "Phill Smith", "birthday": "1990.07.07"},
        {"name": "Phill Smith", "birthday": "1998.02.29"}
        ]

upcoming_birthdays = get_upcoming_birthdays(users)
print("List of upcoming congratulations:\n", upcoming_birthdays)