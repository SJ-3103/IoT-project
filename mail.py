import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# Setting the mail client
sender = "shbhm89300@gmail.com"
reciever = "jshubham579@gmail.com"
msg = MIMEMultipart() 
msg['From'] = sender 
msg['To'] = reciever 


def sendmail(subject, file_name1, path_name, body_message):
    msg['Subject'] = subject
    body = body_message
    msg.attach(MIMEText(body, 'plain')) 
    filename = file_name1
    attachment = open( path_name, "rb") 
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read())  # To change the payload into encoded form 
    encoders.encode_base64(p)     # encode into base64 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p)     # attach the instance 'p' to instance 'msg'
    s = smtplib.SMTP('smtp.gmail.com', 587)     # creates SMTP session 
    s.starttls()     # start TLS for security 
    s.login(sender, "password")   # Authentication 
    text = msg.as_string()  # Converts the Multipart msg into a string
    s.sendmail(sender, reciever, text)   # sending the mail 
    print("[INFO] Mail Sent\n[MSG] Mailed to {}\n[MSG] Subject: {}" .format(reciever,subject))
    s.quit()
