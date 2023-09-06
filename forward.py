import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

class Sending:
    
    def __init__(self,sender_email,sender_password):
         self.sender_email=sender_email
         self.sender_passwords=sender_password   
         

    def send_message(self,receiver_email, subject, message_text):

        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message_text, 'plain'))

        try:
            server = smtplib.SMTP('******', 587)
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, receiver_email, msg.as_string())
            server.quit()
            print("Message sent successfully!")
        except Exception as e:
            print("An error occurred:", str(e))



    def send_email(self,subject, body, to_email):
    
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = to_email
        msg['Subject'] = subject


        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('******', 587)  
            server.starttls() 
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, to_email, msg.as_string())
            server.quit()
            print("Email sent successfully!")
        except Exception as e:
            print("An error occurred:", str(e))
            
            
        
        
        
    def send_email_with_attachment(self,subject, body, to_email, attachment_path):

        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        
        with open(attachment_path, 'rb') as attachment:
            part = MIMEApplication(attachment.read())
            part.add_header('Content-Disposition', f'attachment; filename="{attachment_path}"')
            msg.attach(part)

        
        try:
            server = smtplib.SMTP('******', 587)
            server.starttls() 
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, to_email, msg.as_string())
            server.quit()
            print("Email with attachment sent successfully!")
        except Exception as e:
            print("An error occurred:", str(e))
        
class Forwading:       
   
    def email(ch, method, properties, body):
        message = json.loads(body)
        recipient_email = message['recipient_email']
        subject = message['subject']
        body_text = message['body']
        instance1=Sending()
        instance1.send_email(recipient_email, subject, body_text)
        


    def attachment(ch, method, properties, body):
        message = json.loads(body)
        recipient_email = message['recipient_email']
        subject = message['subject']
        body_text = message['body']
        attachment_path = message['attachment_path']
        instance2=Sending()
        instance2.send_email_with_attachment(recipient_email, subject, body_text, attachment_path)
        
           
    def message(ch, method, properties, body):
        message = json.loads(body)
        receiver_id = message['receiver_id']
        message_text = message['message_text']
        instance3=Sending()
        instance3.send_message(receiver_id, message_text)
 
 
 

