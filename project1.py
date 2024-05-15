#The program
#1.URL shortener:

import pyshorteners  
long_url = input("Enter the URL to shorten: ")
 

tiny = pyshorteners.Shortener()
short_url = tiny.tinyurl.short(long_url)
 
print("The Shortened URL is: " + short_url)


# Documentation
#The above python program imports the pyshorteners module which is an bulit -in libray which provides functionality for shortening URLs using various URL shortening services. 
#First the program accepts the URL in a default string fomat which is stored in an object named long_url 
#Then the object tiny is an instance of the Shortener class that allows access to the methods in Shortener class.
#Then this line calls the short() method of the Shortener instance tiny and passes the long URL (long_url) as an argument. The short method specifically uses the TinyURL service to shorten the URL. The shortened URL is then stored in the variable short_url. 
#Finally the print method is used to print out the shortened url to the console.

