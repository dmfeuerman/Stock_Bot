import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime, time
def Send_Sorted_Data():
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
	msg['Subject'] = "Newest Data"

	# string to store the body of the mail
	body = "Total Files"

	# attach the body with the msg instance
	msg.attach(MIMEText(body, 'plain'))

	# open the file to be sent
	files = "/home/dylan/Documents/StockBot/outfiles/Sorted_data"

	filenames = [os.path.join(files, f) for f in os.listdir(files)]

	for file in filenames:
		part = MIMEBase('application', 'octet-stream')
		part.set_payload(open(file, 'rb').read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', 'attachment; filename="%s"' % file)
		msg.attach(part)

	# creates SMTP session
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

def Send_out_files():
	fromaddr = "automationtestdmf@gmail.com"
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
	files = "/home/dylan/Documents/StockBot/Data_collection"
	filenames = [os.path.join(files, f) for f in os.listdir(files)]

	for file in filenames:
		part = MIMEBase('application', 'octet-stream')
		part.set_payload(open(file, 'rb').read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', 'attachment; filename="%s"' % file)
		msg.attach(part)

	# creates SMTP session
	s = smtplib.SMTP('smtp.gmail.com', 587)

	# start TLS for security
	s.starttls()

	# Authentication
	s.login(fromaddr, "Neekodog2299!")

	# Converts the Multipart msg into a string
	text = msg.as_string()

	# sending the mail
	s.sendmail(fromaddr, toaddr, text)

	# terminating the session
	s.quit()
def Upload_Single_File():
	fromaddr = "automationtestdmf@gmail.com"
	toaddr = "automationtestdmf@gmail.com"
	#toaddr2 = "joshfeuerman@gmail.com"
	#toaddr3 = "pftrading17@gmail.com"

	# instance of MIMEMultipart
	msg = MIMEMultipart()

	# storing the senders email address
	msg['From'] = fromaddr

	# storing the receivers email address
	msg['To'] = toaddr

	# storing the subject
	msg['Subject'] = "Newest Data"

	# string to store the body of the mail
	body = "Total Files"

	# attach the body with the msg instance
	msg.attach(MIMEText(body, 'plain'))

	filename = "/home/dylan/Documents/StockBot/outfiles/Stock_data.csv"
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
	#s.sendmail(fromaddr, toaddr2, text)
	#s.sendmail(fromaddr, toaddr3, text)

	# terminating the session
	s.quit()

def main():
	Send_Sorted_Data()
	Send_out_files()
	Upload_Single_File()


main()
