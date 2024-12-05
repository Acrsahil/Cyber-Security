import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Enable debugging for SMTP communication
DEBUG_LEVEL = 1

# Initialize connection to Gmail SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
# server.set_debuglevel(DEBUG_LEVEL)  # Enable detailed debug output
server.ehlo()  # Say hello to the server
server.starttls()  # Start encrypted connection

# Login to the server with App Password
app_password = "qrkxgdngarezcvvnss"  # App Password 
server.login("sender@gmail.com", app_password)

# Prepare the email
msg = MIMEMultipart()
msg["From"] = "Sahil acrsahil18@gmail.com"
msg["To"] = "acharyalekhnath07@gmail.com"
msg["Subject"] = "Just a Test"

# Read email body from file
with open("message.txt", "r") as f:
    message = f.read()
msg.attach(MIMEText(message, "plain"))


msg1 = msg.as_string()

print(msg1)

    
i = 10
while(i):
    server.sendmail("sender@.com", "receiver.com", msg.as_string())
    print("Email sent successfully!")
    i-=1

server.quit()  # Close the connection
