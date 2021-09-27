import requests  # http requests
from bs4 import BeautifulSoup  # web scraping
import smtplib  # send the email
from email.mime.multipart import MIMEMultipart  # email body
from email.mime.text import MIMEText  # email body
import datetime  # system date and time

now = datetime.datetime.now()  # current system time

content = ''  # email content placeholder


def extract_news(url):
    print('Extracting HackerNews Stories...')
    cnt = ''
    cnt += ('<b>HN Top Stories:</b>\n' + '<br>' + '-' * 50 + '<br>')  # title for our male
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt += ((str(i + 1) + ' :: ' + tag.text + "\n" + '<br>') if tag.text != 'More' else '')
    return cnt


cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------<br>')
content += ('<br><br>End of message')

######## send the mail ########

print('Composing Email....')

SERVER = 'smtp.gmail.com'  # our SMTP server
PORT = 587  # our port number
FROM = 'doarzevel12345678@gmail.com'  # our from-email ID
PASS = 'm1826424'  # FROM email id's password
TO = 'kfirbilu@gmail.com'  # our email ids to send to

msg = MIMEMultipart()

msg['Subject'] = 'Top Nes Stories HN [Automated Email]'+' '+ str(now.day)+'-'+str(now.month)+'-'+str(now.year)
msg['From'] = FROM
msg['To'] = TO
msg.attach(MIMEText(content,'html'))



######## Mail server ########

print('Initiating Server...')

server = smtplib.SMTP(SERVER,PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM,PASS)
server.sendmail(FROM,TO,msg.as_string())

print('Email Sent...')

server.quit()



