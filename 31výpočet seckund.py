def seconds_to_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds

total_seconds = 350000
hours, minutes, seconds = seconds_to_time(total_seconds)
print(f"{total_seconds} seconds is {hours} hours, {minutes} minutes, and {seconds} seconds.")