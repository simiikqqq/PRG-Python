def seconds_to_str(time_in_sec) -> str:
  if time_in_sec < 60:
    return f"{time_in_sec} seconds"
  elif time_in_sec < 3600:
    return f"{time_in_sec // 60} minutes"
  elif time_in_sec < 86400:
    return f"{time_in_sec // 3600} hours"
  else:
    return f"{time_in_sec // 86400} days"
    


def trasfer_time(file_size, unit="KiB", ethernet_speed=10) -> float:
    if unit == "KiB":
        file_size *= 1024
    elif unit == "MiB":
        file_size *=1024**2
    elif unit == "GiB":
        file_size *= 1024**3
    file_size_bits = file_size*8
    return file_size_bits / (ethernet_speed*1e6)
        

print(trasfer_time(80, unit="KiB", ethernet_speed=1000))
print(seconds_to_str(trasfer_time(80, unit="GiB", ethernet_speed=100)))
