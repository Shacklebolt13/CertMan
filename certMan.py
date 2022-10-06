from email import encoders, message
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import smtplib
import ssl
import sys
import locMan
import argparse

# ----------------- TO CUSTOMIZE-------------------
eventSm = " "  # for files
event = "the 2 Day Training in Android App Development"  # for mail
filedir = "certs/"
makePdf = True
msg = f"Thank You For Participating in {event}. Please find your certificate attatched to this mail."
debugServerPort = 1025
mailSub = f"Badhiyaan Ji"
# Instantiate the parser
parser = argparse.ArgumentParser(
    description="Post certificate and send mail using gmail smtp")
parser.add_argument('sender', metavar='',
                    help='Sender mail ID is required')
parser.add_argument('password', metavar='',
                    help='Sender password is required')
group = parser.add_mutually_exclusive_group()
group.add_argument('-d', '--debug', action='store_true', help='Enable debug')
group.add_argument('-v', '--verbose', action='store_true',
                   help='Enable verbose')
group.add_argument('-c', '--custom', action='store_true',
                   help='Enable custom input')
group.add_argument('-n', '--nofile', action='store_true',
                   help='Enable no file')
args = parser.parse_args()
# --------------------------------------------------

if args.debug:
    context = ssl.create_default_context()
    sender = args.sender
    password = args.password
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
    print(sender, password)
    server.login(sender, password)
else:
    sender = "Test"
    server = smtplib.SMTP("localhost", port=debugServerPort)
# syntax: python3 ownAuto.py <gmail> <pass> [options]
# -v verbose
# -d debug smtp server
# -c custom input
# -n no attatch file


def capUp(name):
    chunks = name.split(" ")
    return " ".join(list(map(lambda x: x.capitalize(), chunks)))


def main():
    if args.verbose:
        df = pd.read_excel("participants.xlsx")
        name_list = list(df["name"])
        email_list = list(df["mail"])
        for *i, coun in zip(name_list, email_list, range(1, 100000)):
            print(i, coun)
    else:
        name_list = ["p1", "p2", "p3"]  # list(df['name'])
        email_list = ["a@emai1.com", "b@email.com", "c@email.com"]

    for name, email in zip(name_list, email_list):
        name = capUp(name)
        filename = createPdf(name)
        maillto(email, filename, name)


def maillto(address, filename, name):

    message = attachMsg(name, address)

    if args.nofile:
        message.attach(attachFile(filename))

    text = message.as_string()

    if args.verbose:
        print(text)

    server.sendmail(sender, address, text)


def createPdf(name):
    debugMode = args.verbose

    return locMan.saveCert(name, debug=debugMode, pdf=makePdf)


def attachMsg(name, address):

    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = address
    message["Subject"] = mailSub

    # finalmsg = open("team_selection.html", "r").read()
    finalmsg = f"Hi {name},\n" + msg

    message.attach(MIMEText(finalmsg, "html"))

    return message


def attachFile(filename):
    attchdFile = MIMEBase("application", "octet-stream")

    with open(filename, "rb") as attachment:
        attchdFile.set_payload(attachment.read())

    encoders.encode_base64(attchdFile)
    attchdFile.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    return attchdFile


main()
