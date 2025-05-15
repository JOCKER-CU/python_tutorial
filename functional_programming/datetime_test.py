# Import datetime module
from datetime import datetime, date, time

# Get current date and time
current_datetime = datetime.now()
print(f"Current date and time: {current_datetime}")

# Get current date
current_date = date.today()
print(f"Current date: {current_date}")

# Get current time
current_time = current_datetime.time()
print(f"Current time: {current_time}")

# Create a specific date
specific_date = date(2023, 6, 15)
print(f"Specific date: {specific_date}")

# Create a specific time
specific_time = time(14, 30, 0)
print(f"Specific time: {specific_time}")

# Format date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date and time: {formatted_datetime}")

# Calculate time difference
future_date = datetime(2024, 1, 1)
time_difference = future_date - current_datetime
print(f"Time until 2024: {time_difference}")
