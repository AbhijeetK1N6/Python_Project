import os
import math
import random
import smtplib
from twilio.rest import Client


def TryingEntry():
        # Your Account Sid and Auth Token from twilio.com/user/account
    ACCOUNT_SID = "####__MY_SID___####" 
    AUTH_TOKEN = "####___MY_TOKEN___####" 
    client = Client(ACCOUNT_SID, AUTH_TOKEN) 
    #    to = "+15556667777",    # Replace with the number you want to text
    #    from_ ="+15558675309")  # Replace with your Twilio number
    #    Note that the parameter is named `from_`, not `from`
    message = client.messages.create(to = "+91TargetPhoneNuber", 
        from_ = "+17472987031",
        body = "####--IMPORTANT--####\nSomeone is trying to enter in the XYZ Area, Time to be Alert!")

aadhar_data={"5675":"abc@gmail.com","0930":"xyz@gmail.com"}     #Target Emails(linked with aadhar) to get the OTP
ip_aadhar=input("Enter Last Four Digits of your Aadhar Number:-")
if ip_aadhar in aadhar_data:
    ip_email=input("Enter the Email Linked with your Aadhar:-")
    if aadhar_data[ip_aadhar]==ip_email:
        digits="0123456789"
        OTP=""
        for i in range(6):
            OTP+=digits[math.floor(random.random()*10)]
        otp = OTP + " is your OTP to get in"
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("pqrs@gmail.com", "uitkkqpgmyhwglau")   #Source email to send the OTP
        #emailid = input("Enter your email: ")
        s.sendmail('&&&&&&&&&&&',ip_email,msg)
        a = input("Enter Your OTP >>: ")
        if a == OTP:
            print("Verified!!,Let's Move to next security check.")
        else:
            print("ACCESS DENIED!!,OTP Mismatch.")
            TryingEntry()
    else:
        print("ACCESS DENIED, Email Not Found!!")
        TryingEntry()

else:
    print("ACCESS DENIED!!,Aadhar Not Found.")
    TryingEntry()
