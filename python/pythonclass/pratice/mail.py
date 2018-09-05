
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def or_det(to,subject, data):
	print "Sending mail Please wait................"
	me = "karnati111@gmail.com"
	msg = MIMEMultipart('alternative')
	msg['Subject'] = subject
	msg['From'] = me
	#msg['To'] = to
	html = """\
	<html>
	<head></head>
	<body>
	  <p>Dear User,</p>
	  <p>Your order details</p>
	  <font color='red'> Item Name  -  {item_name}
	  					Quantity    -  {quantity}
	  					ppu         -  {ppu}
	  					Total       -  {total}</font>
	  <p>Here is the <a href="http://www.python.org">link</a> you wanted.  </p>
	</body>
	</html>""".format(item_name=data['item_name'], quantity=data['quantity'], ppu=data['ppu'], total=data['ppu']*data['quantity'])

	part2 = MIMEText(html, 'html')

	msg.attach(part2)
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(me, 9440145562)
	print "logged in successfully"
	#for mail in to:
		#print "Mail Sending to {mail}".format(mail=mail)
	[server.sendmail(me, mail, msg.as_string()) for mail in to]
	print "mail sent successfully.........;)"
	server.quit()

or_det(["h.sarma212@gmail.com", 'brahmarao1989@gmail.com'],"my sample text", {'item_name': 'Cipla', 'quantity': 20, 'ppu': 12.90})
