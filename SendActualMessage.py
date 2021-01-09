'''
https://www.google.com/settings/security/lesssecureapps
ALLOW FIRST
'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class ActualMessage:
    sender_address , sender_pass = '' , ''
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    def __init__(self,senderMail,senderPassword):
        self.sender_address = senderMail
        self.sender_pass = senderPassword
        self.session.starttls() #enable security
        self.session.login(self.sender_address, self.sender_pass) #login with mail_id and password
    def SendMessage (self,receiver_address,subject,messageContent):
        message = MIMEMultipart()
        message['From'] = self.sender_address
        message['To'] = receiver_address
        message['Subject'] = subject
        message.attach(MIMEText(messageContent, 'plain'))
        text = message.as_string()
        self.session.sendmail(self.sender_address, receiver_address, text)
        print('Mail Sent')

    def __del__(self): 
        print('Destructor called, session deleted.') 
        self.session.quit()
    