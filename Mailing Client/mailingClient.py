import smtplib  # using to send mails
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

### server and mailing details ###

SERVER = 'smtp.gmail.com'  # our SMTP server
PORT = 587  # our port number
FROM = 'doarzevel12345678@gmail.com'  # our from-email ID
PASS = '*********'  # FROM email id's password
TO = 'doarzevel12345678@gmail.com'  # our email ids to send to


### starting the server ###

with open("password.txt", 'r') as f:  # reading the password from an external file for safer code
    PASS = f.read()

server = smtplib.SMTP(SERVER, PORT)  # opening a server
server.set_debuglevel(0)  # showing debug comments so we can debug if there are any errors (0 for not showing, 1 for showing)
server.ehlo()
server.starttls()
server.login(FROM, PASS)



### building the message ###

msg = MIMEMultipart()  # initializes the message
msg['From'] = FROM
msg['To'] = TO
msg['Subject'] = "test"

with open("message.txt", 'r') as f:
    message = f.read();

msg.attach(MIMEText(message, 'plain'))

fileName = 'image.jpg'
attachment = open(fileName, 'rb')

payload = MIMEBase('application', 'octet-stream')
payload.set_payload(attachment.read())

encoders.encode_base64(payload)
payload.add_header('Content-Disposition', 'attachment; filename="image.png"')
msg.attach(payload)

text = msg.as_string()  # all of our data casted into text to be sent by mail

print("Sending Mail")

server.sendmail(FROM, TO, text)

print("Mail sent")
