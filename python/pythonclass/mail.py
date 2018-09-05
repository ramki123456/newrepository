import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = 'karnati111@gmail.com'
toaddr   = 'karnati111@gmail.com'
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Mail using smtplib module"
body = "YOUR MESSAGE HERE"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login("karnati111@gmail.com","9440145562")
server.sendmail(fromaddr, toaddr, msg.as_string())
server.close()
# authontication failure  go to https://www.google.com/settings/security/lesssecureapps