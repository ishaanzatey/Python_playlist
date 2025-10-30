import smtplib
from tkinter import N

sender= "sender@gmail.com"
receiver= "receiver@gmail.com"
password= "password123"
subject= "Python email test"
body= "I wrote an email"


# header
message = f"""from{sender}
To: {receiver}
subject: {subject}\n
{body}
"""


server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in")
    server.sendmail(sender,receiver,message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("Unable to login successfully")