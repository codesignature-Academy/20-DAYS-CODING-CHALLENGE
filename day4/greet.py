# check the time and greet the user according to their time
import datetime

# user's current date and time
date = datetime.datetime.now()

# get hour from time
h = int(date.strftime('%H'))

message = "Good "

if h < 12:
    message += "Morning"
elif h < 16:
    message += "Afternoon"
elif h < 21:
    message += "Evening"
else:
    message += "Night"

print(message)