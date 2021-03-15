import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def Text_Me():
    stocks = []
    with open("/home/pi/Search/outfiles/Stock_data.csv", "r") as fs:
        for stock in fs:
            stock = stock.split(",")
            stock.remove('\n')
            try:
                try:
                    if float(str(stock[4]).replace("/n", "").replace("%", "")) >=5.00:
                        server = smtplib.SMTP( "smtp.gmail.com", 587 )
                        server.starttls()
                        server.login( 'Dylan.m.feuerman@gmail.com', 'Neekodog2299' )
                        server.sendmail( 'dylan.m.feuerman@gmail.com', '2034243302@messaging.sprintpcs.com', str(stock) )
                except IndexError:
                    continue
        
                    
            except ValueError:
                continue
      

def main():
    Text_Me()
    


main()
