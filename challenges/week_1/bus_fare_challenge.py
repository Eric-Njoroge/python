# WRITE YOUR CODE SOLUTION HERE
# WRITE YOUR CODE SOLUTION HERE

#imports
import time
import datetime

#tkaes the date today and stores in to variable date
date = datetime.date.today()

#takes the day from the date and stores the first three letters of the day
day = date.strftime("%A")[0:3]



#if statements

if date.strftime("%A")=="Monday"or"Tuesday"or"Wednesday"or"Thursday"or"Friday":
    fare = 100
    print("Date: ",date)
    print("Day: ",day)
    print("Fare: ",fare)

elif date.strftime("%A")=="Saturday":
    fare = 60
    print("Date: ",date)
    print("Day: ",day)
    print("Fare: ",fare)

elif date.strftime("%A")=="Sunday":
    fare = 80
    print("Date: ",date)
    print("Day: ",day)
    print("Fare: ",fare)


