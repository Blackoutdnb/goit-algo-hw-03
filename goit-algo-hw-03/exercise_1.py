from datetime import date

def get_days_from_today(date_str):
    date_now = date.today()
    date_string = datetime.strptime(date_str,"%Y-%m-%d").date()
    delta_days = date_now - date_string
    return delta_days.days
