from datetime import date, datetime
def get_days_from_today(date_str):
    try:
        date_string = datetime.strptime(date_str,"%Y-%m-%d").date()
    except ValueError:
        return 0
    
    date_now = date.today()
    delta_days = date_now - date_string
    
    return delta_days.days
