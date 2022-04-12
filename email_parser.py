import random
import smtplib
import math

from email.mime.text import MIMEText

from datetime import date

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

file_path = ""
senders_email_address = ""
senders_email_password = ""
send_to_email = ""

#Divide line count by 5 to reach the number of quotes, rounded up. 
lineCount = file_len(file_path)
lineCount = lineCount / 5

titleArr = []
quoteArr = []

#Open the file again for reading, not counting
clipFile = open(file_path, 'r')

#Digest the clippings file and append to the array
for x in range(math.ceil(lineCount)):
    #Title will be returned, clipFile.readline() should return the line until EOL.
    getTitle = clipFile.readline()
    getLoc = clipFile.readline()
    getEmptySpace = clipFile.readline()
    getContent = clipFile.readline()
    getBarrier = clipFile.readline()

    titleArr.append(getTitle)
    quoteArr.append(getContent)

clipFile.close()

#Random generator that chooses which quote to send
quoteSelctor1 = random.randrange(len(titleArr))
quoteSelctor2 = random.randrange(len(titleArr))
quoteSelctor3 = random.randrange(len(titleArr))
quoteSelctor4 = random.randrange(len(titleArr))
quoteSelctor5 = random.randrange(len(titleArr))

#print('From the book ' + titleArr[quoteSelctor] + ' a highlighted quote was ' + quoteArr[quoteSelctor])

#Email code

#Start connection and setup login.
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
type(smtpObj)
smtpObj.starttls()
smtpObj.login(senders_email_address, senders_email_password)

#MIME sending of the HTML email

# Create message container - the correct MIME type is multipart/alternative.

with open('email_template.html', "rt") as html:#Template file
    with open('{date}.html'.format(date = date.today()), "wt") as todaysEmail:#Generated file
        for line in html:
            todaysEmail.write(line.replace('$TITLE-ONE', titleArr[quoteSelctor1]).replace('$QUOTE-ONE', quoteArr[quoteSelctor1]).replace('$TITLE-TWO', titleArr[quoteSelctor2]).replace('$QUOTE-TWO', quoteArr[quoteSelctor2]).replace('$TITLE-THREE', titleArr[quoteSelctor3]).replace('$QUOTE-THREE', quoteArr[quoteSelctor3]).replace('$TITLE-FOUR', titleArr[quoteSelctor4]).replace('$QUOTE-FOUR', quoteArr[quoteSelctor4]).replace('$TITLE-FIVE', titleArr[quoteSelctor5]).replace('$QUOTE-FIVE', quoteArr[quoteSelctor5]))


todaysEmail = open('/Users/Harvey/Desktop/programming/Kindle clippings/Program/emails/{date}.html'.format(date = date.today()))

msg = MIMEText(todaysEmail.read(), 'html')
msg['Subject'] = "Your daily kindle highlight " + date.today().strftime("%b %d %Y")
msg['From'] = senders_email_address
msg['To'] = send_to_email

text = msg.as_string()
smtpObj.sendmail(senders_email_address, send_to_email, text)

smtpObj.quit()
todaysEmail.close()
