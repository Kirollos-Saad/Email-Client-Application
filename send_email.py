import smtplib
from email.mime.multipart import MIMEMultipart # Used to create the whole message
from email.mime.text import MIMEText # Used to add text to the email
#from email import encoders
#from email.mime.base import MIMEBase # Used to add attachments to the email

def send_email(sender_email, password, recipient_email, subject, body):
    try:
        # Define SMTP server and port
        server = smtplib.SMTP('smtp.office365.com', 587) 
        print('Connected to the server')

        # Start secure encrypted connection
        server.starttls() # Starts a TLS (Transport Layer Security) encrypted connection with the SMTP server
        server.ehlo() # EHLO is a command sent by an email server to identify itself when connecting to another email server
        
    except Exception as e:
        raise Exception(f'Failed to establish a connection with the server: {str(e)}')
        print(f'Failed to establish a connection with the server: {str(e)}')
        return

    try:
        # Login to your Outlook account
        server.login(sender_email, password)

    except smtplib.SMTPAuthenticationError:
        raise Exception('SMTP Authentication Error: The server didn\'t accept the username/password combination.')
        print('SMTP Authentication Error: The server didn\'t accept the username/password combination.')
        return
    except Exception as e:
        raise Exception(f'Failed to login: {str(e)}')
        print(f'Failed to login: {str(e)}')
        return

    try: 
        # Create a multipart message
        msg = MIMEMultipart()
        #Defining msg headers
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the message body as plain text
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

    except Exception as e:
        raise Exception(f'Failed to send email: {str(e)}')
        print(f'Failed to send email: {str(e)}')
        return
    
    finally:
        # Terminate the SMTP session and close the connection
        server.quit()
    print('Email sent successfully')

  

if __name__ == "__main__":
    sender_email = "lab3networks1@outlook.com"
    password = ".lab10net2020"
    recipient_email = "peachealasaid@awgarstone.com"
    subject = "Test Email"
    body = "Hello world this is my first try for sending email using python."
 #alternate email ="alih11221@outlook.com" pass=".m?ai7mo"
    send_email(sender_email, password, recipient_email, subject, body)