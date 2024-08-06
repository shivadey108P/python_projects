import random
import datetime as dt
import smtplib
with open('./day-32/Birthday_Wisher_start/quotes.txt') as file:
    quotes = file.readlines()
    motivational_quote = random.choice(quotes)
    
MY_EMAIL = 'shivadey108@gmail.com'
MY_PASSWORD = 'wpbxpxfzayxtwpym'

message = f"Subject: Motivational Quote of the day!\n\n{motivational_quote}"
date_now = dt.datetime.now()
week_day = date_now.weekday()

if week_day == 0:
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs='shivadey1089@gmail.com',
                                msg=message)
            print("Email sent successfully!")
    except Exception as e:
        print(f'Email not sent due to: {e}')
        
        
