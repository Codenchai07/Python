#Greet the message to your senior on basis of system time not by entering you 
#like good mornign sir, good evening sir, good night sir

import time
timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))

# hour = int(input("Enter hour: "))

if hour >= 0 and hour < 12 :
    print("Good morning sir")
elif hour >= 12 and hour < 17:
    print("Good afternoon sir")
elif hour >= 17 and hour < 21:
    print("Good evening sir")
else :
    print("Good night sir")