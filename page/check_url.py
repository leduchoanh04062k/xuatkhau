import re
from datetime import datetime, timedelta, date
import random
import string

def is_valid_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, url) is not None
    
def is_valid_phone(phone):
    pattern = r"^(0[2-9]|84[2-9])[0-9]{8}$"
    return re.match(pattern, phone)

def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))    

def generate_month_choices():
    today = date.today()
    current_year = today.year
    current_month = today.month
    choices = []
    for year in range(current_year, current_year + 4):
        for month in range(1, 13):
            if year == current_year and month < current_month:
                continue
            month_str = f"{month:02d}/{year}"
            choices.append(month_str)
    return choices    