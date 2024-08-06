##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import pandas as pd
import datetime as dt
from random import randint
import smtplib

MY_EMAIL = 'shivadey108@gmail.com'
MY_PASSWORD = 'wpbxpxfzayxtwpym'

PLACEHOLDER = '[NAME]'
birthday_person = None

data = pd.read_csv('./day-32/birthday-wisher-extrahard-start/birthdays.csv')
birthday_records = data.to_dict(orient='records')
# print(type(birthday_records[0]['month']), birthday_records[0]['day'])

birthday_records_size = len(birthday_records)
now = dt.datetime.now()
today_date = now.day
today_month = now.month

random_number = randint(1,3)

check = True

for i in range(birthday_records_size):
    if birthday_records[i]['day'] == today_date and birthday_records[i]['month'] == today_month:
        birthday_person = birthday_records[i]['name']
        with open(f'./day-32/birthday-wisher-extrahard-start/letter_templates/letter_{random_number}.txt', mode= 'r') as letter:
            letter_selected = letter.read()
            letter_birthday = letter_selected.replace(PLACEHOLDER,birthday_person)
            print(letter_birthday)
        to_address_email = birthday_records[i]['email']
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





