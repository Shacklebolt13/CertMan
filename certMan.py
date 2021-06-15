from email import encoders, message
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import smtplib,ssl,sys
import locMan 


eventSm="xyz"   #for files
event="xyz Competion"   #for mail
filedir="certs/" 
makePdf=True

msg=f"Thank You For Participating in {event}. Please find your certificate attatched to this mail."


if("-d" not in sys.argv):
    context = ssl.create_default_context()
    sender=sys.argv[1]
    password=sys.argv[2]
    server=smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) 
    server.login(sender, password)
else:
    sender="Test"
    server=smtplib.SMTP("localhost",port=1025)
#syntax: python3 ownAuto.py <gmail> <pass> [options]
# -v verbose
# -d debug smtp server
#-c custom input
#-n no attatch file
    

def main():
    if("-d" not in sys.argv ):
        df=pd.read_csv('participants.csv')
        name_list=list(df['name'])
        email_list=list(df['email'])
    else:
        name_list=['p1','p2','p3']#  list(df['name'])
        email_list=['a@emai1.com','b@email.com','c@email.com']

    for name,email in zip(name_list,email_list):
        filename=createPdf(name)
        maillto(email,filename,name)



def maillto(address,filename,name):
    
    message=attachMsg(name,address)

    if("-n" not in sys.argv):
        message.attach(attachFile(filename))
    
    text=message.as_string()

    if("-v" in sys.argv):
        print(text)
    
    
    server.sendmail(sender, address, text)



def createPdf(name):
    debugMode=True if("-v" in sys.argv ) else False
    
    return locMan.saveCert(name,debug=debugMode,pdf=makePdf)

def attachMsg(name,address):

    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = address
    message["Subject"] = f"Certificate For {event}"

    finalmsg=f"Hi {name},\n"+msg
    
    message.attach(MIMEText(finalmsg, "plain"))    

    return message


def attachFile(filename):
    attchdFile = MIMEBase("application", "octet-stream")
    
    with open(filename, "rb") as attachment:
        attchdFile.set_payload(attachment.read())
    
    encoders.encode_base64(attchdFile)
    attchdFile.add_header("Content-Disposition",f"attachment; filename= {filename}",)

    return attchdFile

main()