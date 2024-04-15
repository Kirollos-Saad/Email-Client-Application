import imaplib
import email
#from email.header import decode_header
from plyer import notification

def receive_email(user_email, password):
    try:
        # Establish a connection with the mail server
        mail = imaplib.IMAP4_SSL('outlook.office365.com') #port usually =993
        
        # Authenticate
        mail.login(user_email, password)
        print('Connected to the server')

        # Select the mailbox you want 
        mail.select("Inbox") # Select the mailbox you want to access (e.g. "Inbox", "Sent Items", "Drafts", etc.)

        # Search for all emails
        status , msgnums = mail.search(None, "ALL") # Returns a list of email IDs
        if status != "OK":
            raise Exception("No messages found")
            print("No messages found")
            return

        # msgnums[0].split() splits the string of email IDs into a list of individual IDs. The [-1] then selects the last item from this list, which is the ID of the latest (most recent) email.
        latest_email_id = msgnums[0].split()[-1] 

        # Fetch the email message by ID
        status, data = mail.fetch(latest_email_id, "(RFC822)") #RFC822 to fetch the whole msg
        if status != "OK":
            raise Exception("Error fetching the email")
            print("Error fetching the email")
            return
        message = email.message_from_bytes(data[0][1]) #data[0][1] is the email content
        print(f"From: {message.get('From')}")
        print(f"To: {message.get('To')}")
        print(f"Subject: {message.get('Subject')}")
        print(f"Date: {message.get('Date')}")
        print("Content")

        email_content = {} # Create a dictionary to store the email content to be used in the GUI
        for part in message.walk(): #walk() is used to iterate over the parts of the email
            if part.get_content_type() == "text/plain":
                print(part.get_payload(decode=True).decode())
                email_content = {
                    'From': message.get('From'),
                    'To': message.get('To'),
                    'Subject': message.get('Subject'),
                    'Body': part.get_payload(decode=True).decode()
                }
        
        # Send a push notification
        notification.notify(
            title=f"New Email from {message.get('From')}",
            message=f"Subject: {message.get('Subject')}\n{message.get('Date')}",
            timeout=10, # The notification will disappear after 10 seconds
        )        

        # Close the connection to the mail server
        mail.logout()

        return email_content

    except Exception as e:
        raise Exception(f'Failed to receive email: {str(e)}')
        print(f'Failed to receive email: {str(e)}')

if __name__ == "__main__":
    user_email = "lab3networks1@outlook.com"
    password = ".lab10net2020"
    receive_email(user_email, password)