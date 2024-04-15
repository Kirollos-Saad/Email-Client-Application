import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
import send_email
import receive_email
import re

def is_valid_email(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def send(user_email, password, recipient_email, subject, body):
    if not user_email or not password or not recipient_email or not subject or not body:
        messagebox.showerror("Error", "All fields must be filled out")
        return

    if not is_valid_email(user_email) or not is_valid_email(recipient_email):
        messagebox.showerror("Error", "Invalid email address")
        return

    if len(body) > 500:
        messagebox.showerror("Error", "Body of the email is too long")
        return

    try:
        send_email.send_email(user_email, password, recipient_email, subject, body)
        messagebox.showinfo("Success", "Email sent successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def receive(user_email, password):
    if not user_email or not password:
        messagebox.showerror("Error", "User email and password must be filled out")
        return

    if not is_valid_email(user_email):
        messagebox.showerror("Error", "Invalid email address")
        return

    try:
        email=receive_email.receive_email(user_email, password)
        messagebox.showinfo("Success", "Email received successfully")

        # Create a new window to display the email content
        email_content_window = tk.Toplevel(root)
        email_content_window.title("Received Email Content")
        email_content_window.grab_set()  # Make the window modal

        # Add labels and text fields to display the email content
        ttk.Label(email_content_window, text="From:").pack(padx=10, pady=10)
        ttk.Label(email_content_window, text=email['From']).pack(padx=10, pady=10)

        ttk.Label(email_content_window, text="To:").pack(padx=10, pady=10)
        ttk.Label(email_content_window, text=email['To']).pack(padx=10, pady=10)

        ttk.Label(email_content_window, text="Subject:").pack(padx=10, pady=10)
        ttk.Label(email_content_window, text=email['Subject']).pack(padx=10, pady=10)

        ttk.Label(email_content_window, text="Body:").pack(padx=10, pady=10)
        ttk.Label(email_content_window, text=email['Body']).pack(padx=10, pady=10)

    except Exception as e:
        messagebox.showerror("Error", str(e))

def open_send_email_screen():
    send_email_screen = tk.Toplevel(root)
    send_email_screen.title("Send Email")
    send_email_screen.grab_set()  # Make the window modal

    user_email = tk.StringVar()
    password = tk.StringVar()
    recipient_email = tk.StringVar()
    subject = tk.StringVar()
    body = tk.StringVar()

    ttk.Label(send_email_screen, text="User Email").pack(padx=10, pady=10)
    ttk.Entry(send_email_screen, textvariable=user_email).pack(padx=10, pady=10)

    ttk.Label(send_email_screen, text="Password").pack(padx=10, pady=10)
    ttk.Entry(send_email_screen, textvariable=password, show='*').pack(padx=10, pady=10)

    ttk.Label(send_email_screen, text="Recipient Email").pack(padx=10, pady=10)
    ttk.Entry(send_email_screen, textvariable=recipient_email).pack(padx=10, pady=10)

    ttk.Label(send_email_screen, text="Subject").pack(padx=10, pady=10)
    ttk.Entry(send_email_screen, textvariable=subject).pack(padx=10, pady=10)

    ttk.Label(send_email_screen, text="Body").pack(padx=10, pady=10)
    ttk.Entry(send_email_screen, textvariable=body).pack(padx=10, pady=10)

    ttk.Button(send_email_screen, text='Send Email', command=lambda: send(user_email.get(), password.get(), recipient_email.get(), subject.get(), body.get())).pack(padx=10, pady=10)

def open_receive_email_screen():
    receive_email_screen = tk.Toplevel(root)
    receive_email_screen.title("Receive Email")
    receive_email_screen.grab_set()  # Make the window modal

    user_email = tk.StringVar()
    password = tk.StringVar()

    ttk.Label(receive_email_screen, text="User Email").pack(padx=10, pady=10)
    ttk.Entry(receive_email_screen, textvariable=user_email).pack(padx=10, pady=10)

    ttk.Label(receive_email_screen, text="Password").pack(padx=10, pady=10)
    ttk.Entry(receive_email_screen, textvariable=password, show='*').pack(padx=10, pady=10)

    ttk.Button(receive_email_screen, text='Receive Email', command=lambda: receive(user_email.get(), password.get())).pack(padx=10, pady=10)

root = ThemedTk(theme="arc")  # Use the "arc" theme
root.title("Email Client")
root.geometry("800x600") #To set the size of the window

style = ttk.Style()
style.configure("BW.TButton", foreground="black", font=('Helvetica', '20', 'bold'))

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, expand=True)

ttk.Button(frame, text='Send Email', command=open_send_email_screen, style="BW.TButton").grid(row=0, column=0, padx=10, pady=10)
ttk.Button(frame, text='Receive Email', command=open_receive_email_screen, style="BW.TButton").grid(row=0, column=1, padx=10, pady=10)

frame.place(relx=0.5, rely=0.5, anchor='center')


root.mainloop()