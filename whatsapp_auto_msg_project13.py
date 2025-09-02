import pywhatkit

# Get the 10-digit phone number
no = input("Enter the 10-digit phone number: ")

# Add the +91 country code automatically
phone_number_with_code = f"+91{no}"

# Get the message
msg = input("Enter the message you want to send: ")

# Get hours and minutes as separate integers
hr = int(input("Enter the time in hours (24-hour format, e.g. 17 for 5 PM): "))
min = int(input("Enter the time in minutes (e.g. 30): "))

# Call the function with the correctly formatted phone number
pywhatkit.sendwhatmsg(phone_number_with_code, msg, hr, min)

print("Message scheduled successfully!")