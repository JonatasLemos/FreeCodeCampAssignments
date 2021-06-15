def add_time(start, duration, day_of_week=False):

    total = start+" "+duration
    split = total.split(" ")
    start_time = split[0].split(":")[0]
    duration = split[-1].split(":")[0]
    pm_am = split[1].split(":")[0]
    start_minute = split[0].split(":")[1]
    duration_minute = split[-1].split(":")[1]

    if pm_am == "PM" and start_time != 12:
        start_time = 12 + int(start_time)
    elif pm_am == "AM" and start_time == 12:
        start_time = 0

    def mod_values(time_span, value):
        return time_span % value

    time_elapsed = int(start_time) + int(duration)
    minutes_elapsed = int(start_minute) + int(duration_minute)

    if minutes_elapsed >= 60:
        time_elapsed += 1
        minutes_elapsed = mod_values(minutes_elapsed, 60)

    n_of_days = 0
    if time_elapsed >= 24:
        n_of_days += int(time_elapsed / 24)
    final_hour = mod_values(time_elapsed, 24)

    char_before = ""
    if minutes_elapsed < 10:
        char_before = "0"
    minute_part = f":{char_before}{minutes_elapsed}"
    bracket_section = ""
    if n_of_days == 1:
        bracket_section = " (next day)"
    elif n_of_days > 1:
        bracket_section = f" ({n_of_days} days later)"

    if day_of_week:
        today = day_of_week.capitalize()
        list_of_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        day_index = list_of_days.index(today)
        day_after_duration = mod_values(day_index+n_of_days, 7)
        day = list_of_days[day_after_duration]
        bracket_section = f", {day}"
        if n_of_days > 1:
            bracket_section = f", {day} ({n_of_days} days later)"
        elif n_of_days == 1:
            bracket_section = f", {day} (next day)"

    def get_hour(am_pm):
        return f"{final_hour}{minute_part} {am_pm}{bracket_section}"

    complete_hour = get_hour("PM")
    if final_hour > 12:
        final_hour = 12 - (24-final_hour)
        complete_hour = get_hour("PM")
    elif final_hour < 12:
        if final_hour == 0:
            final_hour = 12
        complete_hour = get_hour("AM")

    return complete_hour
