import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("pemmasani.ramakrishna@gmail.com", "mypass@9043")
 
msg = "YOUR MESSAGE!"
server.sendmail("pemmasani.ramakrishna@gmail.com", "ramki0653@gmail.com", msg)
server.quit()