import pandas as pd
import datetime as dt
from random import randint
import smtplib

MY_EMAIL = 'shivadey108@gmail.com'
MY_PASSWORD = 'wpbxpxfzayxtwpym'

PLACEHOLDER = '[NAME]'
birthday_person = None

now = dt.datetime.now()
today_date = now.day
today_month = now.month

today_tuple = (today_month, today_date)

data = pd.read_csv('./day-32/birthday-wisher-extrahard-start/birthdays.csv')
day = data.to_dict(orient='records')

random_number = randint(1,3)

birthday_rec = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}



if today_tuple in birthday_rec:
    birthday_person = birthday_rec[today_tuple]['name']
    with open(f'./day-32/birthday-wisher-extrahard-start/letter_templates/letter_{random_number}.txt', mode= 'r') as letter:
            letter_selected = letter.read()
            letter_birthday = letter_selected.replace(PLACEHOLDER,birthday_person)
    to_address_email = birthday_rec[today_tuple]['email']
    print(to_address_email)
    message = f"Subject:Happy Birthday {birthday_person}!\n\n{letter_birthday}"
    try: 
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, 
                                to_addrs=to_address_email, 
                                msg=message)
    except Exception as e:
        print(f'Unable to sent email due to: {e}')
    else:
            print('Email sent Successfully!')
else:
        check = False
        
if not check:
    print('No one have birthday today')


