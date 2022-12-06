water_requirements = [
    None,
    224,
    224,
    224,
    224,
    224,
    192,
    128
]
# water_remaining = 0
water_consumed = 0
water_log = []


def water_tracker(ounces, water_consumed, water_log, year, month, day, requirements):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    day = datetime.date(year, month, day).isocalendar().weekday
    if water_log[len(water_log)-1][1] > date:
        water_consumed = 0
        requirements = water_reguirements[day]
    water_consumed += ounces
    remaining = requirements - water_consumed
    log_entry = water_log.push([month,date,hour,minute,second,day,water_consumed,remaining])
    print(f'ADDED: [{hour}:{minute} -> {ounces} oz. -> {remaining} oz. remaining]')
    return water_log, water_consumed, remaining