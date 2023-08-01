# OTP Verification Application

This is a simple OTP (One-Time Password) Verification application built using Python and Tkinter. The application allows users to request an OTP via email, enter the OTP, and verify it for authentication purposes.

## Features

- Generate a random 6-digit OTP.
- Send the OTP to the user's email using a Gmail SMTP server.
- Verify the entered OTP for authentication.

## Requirements

- Python 3.x
- Tkinter library (usually comes pre-installed with Python)
- smtplib library (for sending emails via SMTP)
- random library (for generating random OTPs)

## Usage

1. Run the `otp_verification.py` file to start the application.
2. Enter your email address in the provided input field.
3. Click the "Send OTP" button to request an OTP via email.
4. Check your email for the OTP sent from the Gmail SMTP server.
5. Enter the received OTP in the second input field.
6. Click the "Verify OTP" button to check if the entered OTP is valid.
7. A success message will be displayed if the OTP is verified.

## How It Works

The application uses the Tkinter library to create a graphical interface with input fields and buttons. The `generate_otp()` function generates a random 6-digit OTP. The `send_otp()` function sends the generated OTP to the user's email using the Gmail SMTP server. The `verify_otp()` function compares the entered OTP with the generated OTP to determine if it is valid.

When the "Send OTP" button is clicked, the application generates a new OTP, saves it globally, and attempts to send it to the user's email address using the `send_otp()` function. If the email is sent successfully, a success message is displayed. Otherwise, an error message is shown.

When the "Verify OTP" button is clicked, the application compares the entered OTP with the previously generated OTP. If they match, a success message is displayed, indicating successful OTP verification. Otherwise, an error message is shown.

## Future Improvements

- Allow users to select the email service provider for sending OTPs.
- Add email validation to ensure the user enters a valid email address.
- Implement better error handling for SMTP email sending failures.
