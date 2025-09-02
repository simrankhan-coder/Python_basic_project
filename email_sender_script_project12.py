import smtplib
from email.message import EmailMessage
def send_email(to,subject,body):
    email=EmailMessage()
    email['From']='your_email@example.com'
    email['To']=to
    email['Subject']=subject
    email.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login('Your email@example.com','your_app_password')
        smtp.send_message(email)

email=input("Enter the email ID :")
subj=input("Enter the Subject: ")
body=input("Enter the Body of Email")
send_email(email,subj,body)