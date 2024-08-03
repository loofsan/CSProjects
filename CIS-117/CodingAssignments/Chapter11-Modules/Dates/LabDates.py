from datetime import datetime, timedelta

def read_date():
    """Reads a date input in yyyy-mm-dd format and returns a datetime object."""
    date_str = input().strip()
    return datetime.strptime(date_str, '%Y-%m-%d')

# Step 1: Read four unique dates and store them in a list
dates = []
for _ in range(4):
    dates.append(read_date())

# Step 2: Sort the list of dates, earliest first
sorted_dates = sorted(dates)

# Step 3: Output the sorted_dates in mm/dd/yyyy format
formatted_dates = [date.strftime('%m/%d/%Y') for date in sorted_dates]
for date_str in formatted_dates:
    print(date_str)

# Step 4: Output the number of days between the last two dates in sorted_dates
days_difference = (sorted_dates[-1] - sorted_dates[-2]).days
print(days_difference)

# Step 5: Output the date that is 3 weeks from the most recent date
three_weeks_delta = timedelta(weeks=3)
three_weeks_from_recent = sorted_dates[-1] + three_weeks_delta
print(three_weeks_from_recent.strftime('%B %d, %Y'))

# Step 6: Output the full name of the day of the week of the earliest day
earliest_day_of_week = sorted_dates[0].strftime('%A')
print(earliest_day_of_week)