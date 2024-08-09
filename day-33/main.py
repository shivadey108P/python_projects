import requests
import datetime as dt
import smtplib
import time

MY_LAT = 17.38
MY_LONG = 78.48

time_now = dt.datetime.now()

my_parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}

my_email = 'shivadey108@gmail.com'
password = 'wpbxpxfzayxtwpym'

def is_iss_satellite_present():
    iss_reponse = requests.get('http://api.open-notify.org/iss-now.json')
    iss_reponse.raise_for_status()

    data = iss_reponse.json()

    longitude_iss = data['iss_position']['longitude']
    latitude_iss = data['iss_position']['latitude']

    iss_position = (longitude_iss, latitude_iss)
    if MY_LAT -5 <= latitude_iss <= MY_LAT + 5 and MY_LONG-5 <= longitude_iss <= MY_LONG:
        return True
    

def is_night():
    response =  requests.get('https://api.sunrise-sunset.org/json', params=my_parameters)
    response.raise_for_status

    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    current_hour = time_now.hour
    if current_hour > sunset and current_hour < sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_satellite_present and is_night:
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection: # 587 is the port for TLS 
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs='shivadey1089@gmail.com',
                                    msg='Subject:ISS Satellite Above You\n\nCheck out the satellite now')
                print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")