# date_difference.py
from datetime import datetime

def calculate_date_difference(start_date, end_date):
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
    end_datetime = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")

    difference = end_datetime - start_datetime

    days = difference.days
    hours, remainder = divmod(difference.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    years = end_datetime.year - start_datetime.year
    months = end_datetime.month - start_datetime.month

    if end_datetime.day < start_datetime.day:
        months -= 1

    if months < 0:
        months += 12
        years -= 1

    return {
        "days": days,
        "months": months,
        "years": years,
        "hours": hours,
        "minutes": minutes
    }
    