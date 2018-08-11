# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.mail.yahoo.com', 465)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("ram.kottapally@yahoo.com", "Benedict95$")
 
# message to be sent
message = "This message is sent via Python"
 
# sending the mail
s.sendmail("ram.kottapally@yahoo.com", "ramm.y2k@gmail.com", message)
 
# terminating the session
s.quit()
