import smtplib 
from email import message
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication
from os.path import basename
from email import encoders

from_add = 'joules.dev.team@gmail.com'
from_pass = 'xairivszaemjctdn'

to_add = ['ben.turner@joules.com', 
          'harriet.watts@joules.com', 
          'deb.burton@joules.com', 
          'naomi.spencer@joules.com']
sub = 'Joules Empty Categories'
content = 'THIS IS AN AUTOMATED EMAIL DO NOT REPLY\nPlease find attached empty categories on site.\nJoules Dev Team.'

__attachments = ['UK-live.xlsx',
                 'UK-staging.xlsx', 
                 'US-live.xlsx', 
                 'US-staging.xlsx', 
                 'DE-live.xlsx', 
                 'DE-staging.xlsx', 
                 './impex-header-templates/DE-live.impex', 
                 './impex-header-templates/DE-staging.impex', 
                 './impex-header-templates/UK-live.impex', 
                 './impex-header-templates/UK-staging.impex', 
                 './impex-header-templates/US-live.impex', 
                 './impex-header-templates/US-staging.impex']

msg = MIMEMultipart()
msg['From'] = from_add
msg['To'] = ", ".join(to_add)
msg['Subject'] = sub
body = MIMEText(content, 'plain')
msg.attach(body)


for xl in __attachments:
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(xl, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(basename(xl)))
    msg.attach(part)

session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(from_add, from_pass) #login with mail_id and password

session.send_message(msg, from_add, to_add)
session.quit()

print("Email sent successfully.")