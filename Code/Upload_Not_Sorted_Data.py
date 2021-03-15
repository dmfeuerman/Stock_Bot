import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def Upload_Single_File(filename):
	fromaddr = "automationtestdmf@gmail.com"
	toaddr = "automationtestdmf@gmail.com"
	toaddr2 = "joshfeuerman@gmail.com"
	toaddr3 = "pftrading17@gmail.com"

	# instance of MIMEMultipart
	msg = MIMEMultipart()

	# storing the senders email address
	msg['From'] = fromaddr

	# storing the receivers email address
	msg['To'] = toaddr

	# storing the subject
	msg['Subject'] = "Unsorted data"

	# string to store the body of the mail
	body = "Total Files"

	# attach the body with the msg instance
	msg.attach(MIMEText(body, 'plain'))


	attachment = open(filename, "rb")

	# instance of MIMEBase and named as p
	p = MIMEBase('application', 'octet-stream')

	# To change the payload into encoded form
	p.set_payload((attachment).read())

	# encode into base64
	encoders.encode_base64(p)

	p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

	# attach the instance 'p' to instance 'msg'
	msg.attach(p)
	s = smtplib.SMTP('smtp.gmail.com', 587)

	# start TLS for security
	s.starttls()

	# Authentication
	s.login(fromaddr, "Neekodog2299!")

	# Converts the Multipart msg into a string
	text = msg.as_string()

	# sending the mail
	s.sendmail(fromaddr, toaddr, text)
	s.sendmail(fromaddr, toaddr2, text)
	s.sendmail(fromaddr, toaddr3, text)

	# terminating the session
	s.quit()

def Upload_Main_Unsorted():
	Upload_Single_File("/home/dylan/Documents/StockBot/outfiles/Stock_data.csv")
