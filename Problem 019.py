import datetime

def count_sundays_on_first():
    count = 0
    for year in range(1901, 2000 + 1):
        for month in range(1, 13):
            if datetime.date(year, month, 1).weekday() == 6:
                count += 1
    return count

result = count_sundays_on_first()

print(result)
