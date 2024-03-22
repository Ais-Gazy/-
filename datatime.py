from datetime import datetime
def is_morning_person(wake_up, bed_time):
    morning_threshold = datetime.strptime("12:00", "%H:%M").time()
    evening_threshold = datetime.strptime("20:00","%H:%M").time()

    wake_up_time = datetime.strptime(wake_up,"%H:%M").time()
    bed_time = datetime.strptime(bed_time,"%H:%M").time()

    is_morning = wake_up_time <= morning_threshold
    is_evening = bed_time >= evening_threshold

    return is_morning and is_evening
