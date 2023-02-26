from email.message import EmailMessage
import os.path
import mimetypes
import smtplib
import getpass
# Sending Email with Attachment

message = EmailMessage()

recipient = "dev.shahfahad.com"
sender = 'you@example.com'
message['From'] = sender
message['To'] = recipient
message['Subject'] = "Greeting from {} to {}".format(sender, recipient)

body = "This is the fake email body which will be send to dummy mail clinet"
message.set_content(body)

# Adding attachment
attachment_path = './Week-3.PNG'
attachment_filename = os.path.basename(attachment_path)
mime_type,_ = mimetypes.guess_type(attachment_path)
# seperate mimetype and subtype 
mime_type, mime_subtype = mime_type.split('/', 1)
# Add 
with open(attachment_path, 'rb') as ap:
     message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, 
                            filename=os.path.basename(attachment_path))
print(message)

# Sending mail
mail_server = smtplib.SMTP('localhost')
mail_server = smtplib.SMTP_SSL('smtp.example.com')
mail_server.set_debuglevel(1)
mail_pass = getpass.getpass('Password? ')
print(mail_server)
print(mail_pass)
# authenticate 
mail_server.login(sender, mail_pass)

# send
mail_server.send_message(message)

# close server
mail_server.quit()


print("END")