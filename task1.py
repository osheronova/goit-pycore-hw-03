# Calculates the number of days between the current date and a given date string
from datetime import datetime

def get_days_from_today(date):
    try:
        # Parse the input string into a datetime object
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
        # Capture today's date
        today = datetime.today()
        # Calculate the time difference 
        diff = today- parsed_date
        # Return the difference in days as an integer
        return diff.days
    except ValueError:
        return "Invalid date format. Enter date in 'YYYY-MM-DD' format."

print(get_days_from_today("2025-10-11"))