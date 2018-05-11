#CNA336
#Jason Dalichau	
#Contact jdalichau@gmail.com

pi = 3.14 #value of pie
r = (float(input("What is the radius of your circle?"))) #input statement for radius of users circle 


if r >= 1:   #input validation for numbers below 1
	
	r = pi*r**2 #calculation for radius 
	print("Your circumfrence is", r) #print of the radius for the users 
	
else:
	
	input("Please choose a postive whole number") #input validation for a positive number 


	
print("Congradulations!!")


