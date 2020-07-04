


# age = input("Enter variable ")
# age = int(age)

# if (age<18):
#     print("less than 18")
# elif(age==18):
#     print("equal to 18")
# else :
#     print("greater than 18")

# comment - it will be there but its not part of code 
# list / array 

# name_list = ["Vinayak", "Akul", "Rahul"]
# length = len(name_list)
# print(length)

# loops repetation of code block 

# for i in range(1, 11):
#     print(i)

# i = 0 

# while(i < 10):
#     i = i + 1
#     print("Hello")



import smtplib


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail():

    mail_content = "Hello, This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library. You"
    #The mail addresses and password
    sender_address = ''
    sender_pass = ''
    receiver_address = ''
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')



