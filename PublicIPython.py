try:
    from bs4 import BeautifulSoup
except:
    print("You need BeautifulSoup module, please install it!")
    print("pip install bs4")
    exit(1)
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

"""
This script servers the purpose of sending by email your current public IP, I'm using GMAIL SMTP server to send it
and IPchicken or whatismypublicip to retrieve the IP, using bs4 to parse it from the request.

Note that the script only sends the IP if it has changed it (when the script executes creates a file and saves the current public IP
then compares if the public IP obtained is the same, if it's the same, the script exits, if it's not the same the script sends the email)

Lastly: this script is intended for sysadmins that need to make remote administration no dynamic IP servers, I am not responsible for
any missuse of this script!
"""

#VARS
filename = 'ip.txt'
public_ip_web = 'https://ipchicken.com/' #main website to check
fallback_web = 'https://www.whatismypublicip.com/' #fallback website, in case ipchicken is down

def get_ip():
    """
    This function retrieves the public IP. Note that the headers are needed otherwise, we got a 403 status.
    """
    try:
        req = Request(public_ip_web, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage,features="html.parser")
        find_b = (soup.find_all('b')[0].get_text())
        fields = find_b.strip().split('\n')
        return fields[0]
    except HTTPError:
        req = Request(fallback_web, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage,features="html.parser")
        fields = (soup.find('div', id="up_finished").get_text())
        return fields


def send_mail():
    """
    This function handles the entire mail setup.
    """
    #BASIC VARS
    sender = '' #the sender address
    to = '' #the recipient address
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_server_login = '' # the address to login on the SMTP server, usually the same as the sender
    smtp_server_pass = '' # password used to auth
    message = MIMEMultipart()
    message['From'] = sender #SENDER
    message['To'] = to #SEND TO
    message['Subject'] = "Your public IP has changed" # SUBJECT
    body = IP #Body of the message
    message.attach(MIMEText(body, 'plain')) #the IP
    #LOGIN AND AUTH
    smtpserver = smtplib.SMTP(smtp_server,smtp_port )
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(smtp_server_login, smtp_server_pass)
    #SEND MAIL
    email_text = message.as_string()
    smtpserver.sendmail(sender, to, email_text)
    smtpserver.close()

# CHECK IF THE FILE EXIST, IF NOT, CREATE IT
if os.path.isfile("filename):
    pass
else:
    with open(filename, 'w+') as ipfile:
        ipfile.write("")

#CHECK IF THE FILE HAS THE ACTUAL PUBLIC IP, IF NOT DELETE THE OLD ONE, WRITE THE NEW ONE AND SEND THE MAIL
IP = get_ip()
with open(filename, 'r+') as output:
    if IP in output.read():
        pass
    elif IP not in output.read():
        output.truncate(0)
        output.write(IP)
        send_mail()
    else:
        print("If you see this, you fucked up the script")
#os.remove(filename) if you do not want the file to be left behind, note that if this is active, the script will not be able to see compare if the IP has changed or not, so it will send the email everytime is executed.
