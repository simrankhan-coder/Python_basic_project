import pywhatkit
no=input("Enter the number(with country code eg +91) :")
msg=input("Enter the message you want to send: ")
hr = int(input("Enter the time in hours (24-hour format, eg. 17 for 5 PM): "))
min = int(input("Enter the time in minutes (eg. 30): "))

pywhatkit.sendwhatmsg(no, msg, hr, min)

print("Message scheduled successfully!")