import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import Encoders
import os
def main():
	
	fromaddr = "dylan.m.feuerman@gmail.com"
	toaddr = "automationtestdmf@gmail.com"

	# instance of MIMEMultipart
	msg = MIMEMultipart()

	# storing the senders email address
	msg['From'] = fromaddr

	# storing the receivers email address
	msg['To'] = toaddr

	# storing the subject
	msg['Subject'] = "Newest Data Output Files"

	# string to store the body of the mail
	body = "Cron worked. Attached is the file to verify if it worked"

	# attach the body with the msg instance
	msg.attach(MIMEText(body, 'plain'))

	# open the file to be sent
	files = "/home/pi/Search/Data_collection"
	filenames = [os.path.join(files, f) for f in os.listdir(files)]
	
	for file in filenames:
		part = MIMEBase('application', 'octet-stream')
		part.set_payload(open(file, 'rb').read())
		Encoders.encode_base64(part)
		part.add_header('Content-Disposition', 'attachment; filename="%s"' % file)
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

	# terminating the session
	s.quit()

main()
