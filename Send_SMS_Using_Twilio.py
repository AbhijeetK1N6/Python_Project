from twilio.rest import Client
# Your Account Sid and Auth Token from twilio.com/user/account
ACCOUNT_SID = "__YOUR_SID____" 
AUTH_TOKEN = "___YOUR_TOKEN___" 
client = Client(ACCOUNT_SID, AUTH_TOKEN) 
message = client.messages.create(to = "__RECEIVER_PH_NUMBER___", 
  from_ = "__TWILIO_PH_NUMBER___",
  body = "####--IMPORTANT--####\nSomeone is trying to enter in the XYZ Area, Time to be Alert!"
)
