import smtplib
import random
import tkinter as tk
from tkinter import messagebox

# Function to generate a random 6-digit OTP
def generate_otp():
    return ''.join(str(random.randint(0, 9)) for _ in range(6))

# Function to send the OTP to the given email
def send_otp(receiver_email, otp):
    sender_email = 'santanutalukdar1512@gmail.com'
    sender_password = 'nklgtxwyvsritrme'
    
    message = f'Subject: OTP Verification\n\nYour OTP is: {otp}'
    
    try:
        # Connect to the Gmail SMTP server and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# Function to verify the entered OTP
def verify_otp():
    user_email = email_entry.get()
    user_otp = otp_entry.get()

    if not user_email or not user_otp:
        messagebox.showwarning("Warning", "Please enter your email and OTP.")
        return

    if user_otp == generated_otp:
        messagebox.showinfo("Success", "OTP Verified!")
    else:
        messagebox.showerror("Error", "Invalid OTP. Please try again.")

# Function to handle the "Send OTP" button click event
def send_otp_button_click():
    global generated_otp
    user_email = email_entry.get()

    if not user_email:
        messagebox.showwarning("Warning", "Please enter your email.")
        return

    # Generate a new OTP and attempt to send it to the user's email
    generated_otp = generate_otp()
    if send_otp(user_email, generated_otp):
        messagebox.showinfo("Success", "OTP has been sent to your email.")
    else:
        messagebox.showerror("Error", "Failed to send OTP. Please try again.")

# Create the main application window
app = tk.Tk()
app.title("OTP Verification")
app.geometry("450x300")

# Define fonts and background color
title_font = ("Comic Sans MS", 20)
label_font = ("Comic Sans MS", 12)
button_font = ("Comic Sans MS", 12)
app.configure(bg="#f0f0f0")  # Set background color for the window

# Create and pack widgets for the application

# Title label
title_label = tk.Label(app, text="OTP Verification", font=title_font, bg="#f0f0f0")
title_label.pack(pady=10)

# Email entry
email_label = tk.Label(app, text="Enter your email:", font=label_font, bg="#f0f0f0")
email_label.pack()

email_entry = tk.Entry(app, font=label_font)
email_entry.pack()

# "Send OTP" button
otp_button = tk.Button(app, text="Send OTP", font=button_font, command=send_otp_button_click, bg="#ffd700", fg="black")
otp_button.pack(pady=10)

# OTP entry
otp_entry_label = tk.Label(app, text="Enter OTP:", font=label_font, bg="#f0f0f0")
otp_entry_label.pack()

otp_entry = tk.Entry(app, font=label_font)
otp_entry.pack()

# "Verify OTP" button
verify_button = tk.Button(app, text="Verify OTP", font=button_font, command=verify_otp, bg="#00bfff", fg="black")
verify_button.pack(pady=10)

# Start the main event loop
app.mainloop()
