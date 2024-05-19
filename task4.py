from task1 import get_days_from_today
from datetime import datetime, timedelta

def handle_weekedns(congrats_date: datetime):
    if congrats_date.isoweekday() == 6:
        congrats_date += timedelta(days=2)
    elif congrats_date.isoweekday() == 7:
        congrats_date += timedelta(days=1)
    return congrats_date

def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    upcoming_birthdays = []
    for user in users:
        birthday_date = datetime.strptime(user.get("birthday"), "%Y.%m.%d").date()
        birthday_this_year = birthday_date.replace(year=datetime.now().year)
        congrats_date = handle_weekedns(birthday_this_year)
        days_from_today = get_days_from_today(str(congrats_date))
        #handle last 7 days of the year
        if days_from_today < 0:
            birthday_next_year = birthday_date.replace(year=datetime.now().year+1)
            congrats_date = handle_weekedns(birthday_next_year)
            days_from_today = get_days_from_today(str(congrats_date))
        if days_from_today <= 7:
            upcoming_birthdays.append({
                "name": user.get("name"), 
                "congratulation_date":congrats_date.strftime("%Y.%m.%d")})
    return upcoming_birthdays