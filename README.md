# Email Client Application

This application is a simple email client that allows users to send and receive emails. It is built using Python and leverages the smtplib and imaplib libraries for sending and receiving emails, respectively. The application also uses the plyer library to send push notifications when a new email is received.

## Features

- **Send Email**: Send emails programmatically using SMTP.
- **Receive Email**: Receive and display emails from the inbox using IMAP.
- **Push Notifications**: Receive desktop notifications for new emails.
- **GUI**: built with Tkinter

## Dependencies

Make sure you have the following dependencies installed:

- `smtplib`
- `email.mime.multipart.MIMEMultipart`
- `email.mime.text.MIMEText`
- `imaplib`
- `email`
- `plyer.notification`
- `tkinter`
- `ttk`
- `ttkthemes`

You can install these dependencies using pip:

```bash
pip install smtplib email.mime.multipart.MIMEMultipart email.mime.text.MIMEText imaplib email plyer.notification tkinter ttk ttkthemes
```  

## Usage

1. Clone the repository: git clone https://github.com/Kirollos_Saad/Email-Client-Application 
2. Navigate to the project directory
3. Install the dependencies
4. Run the application: python -u GUI.py
5. Use the application to send and receive emails.













