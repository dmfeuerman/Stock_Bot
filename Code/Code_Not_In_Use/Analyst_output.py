import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import Encoders
import os
from datetime import datetime, time

        
def main():
	
	fromaddr = "dylan.m.feuerman@gmail.com"
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
	msg['Subject'] = "Newest Data Compilation"

	# string to store the body of the mail
	body = "Attached is the daily print out from all sites. This also includes stock data"

	# attach the body with the msg instance
	msg.attach(MIMEText(body, 'plain'))

	# open the file to be sent
	file_out = "/home/pi/Search/outfiles/Stock_data.csv"
	part = MIMEBase('application', 'octet-stream')
	part.set_payload(open(file_out, 'rb').read())
	Encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename="%s"' % file_out)
	msg.attach(part)
      
	# creates SMTP session
	s = smtplib.SMTP('smtp.gmail.com', 587)

	# start TLS for security
	s.starttls()

	# Authentication
	s.login(fromaddr, "Neekodog2299")

	# Converts the Multipart msg into a string
	text = msg.as_string()

	# sending the mail
	s.sendmail(fromaddr, toaddr, text)
	s.sendmail(fromaddr, toaddr2, text)
	s.sendmail(fromaddr, toaddr3, text)

	# terminating the session
	s.quit()

main()
