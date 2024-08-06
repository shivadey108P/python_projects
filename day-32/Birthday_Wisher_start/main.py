import smtplib

my_email = 'shivadey108@gmail.com'
password = 'wpbxpxfzayxtwpym'

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection: # 587 is the port for TLS 
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='shivadey1089@gmail.com',
                            msg='Subject:Test Mail2\n\nSending mail for testing purpose')
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
