#CNT 336 Python for networking
#Jason Dalichau
#jdalichau@gmail.com

try:
    f = int(input("Enter a temperature in Fahrenheit to convert to Celsius")) #User input for a temp in fahrenheit to convert to celsius
    c = (f - 32) * 5 / 9 #algorithm for the conversion. Found on https://www.almanac.com/content/temperature-conversion

except ValueError: #Value exception for entering a str
    print("Error! Can only convert numbers") #User friendly error
print(f, "degrees in Fahrenheit is", c, "in Celsius") #Printed conversion for the user


