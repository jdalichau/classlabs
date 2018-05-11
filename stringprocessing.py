f = input('Please enter your first name: ') #input for first name
l = input('Please enter your last name: ') #input for last name

f = f.lower() #turn first name to lower case
l = l.lower() #turn last name to lower case
print(f[:1] + l[:7]) #print first letter of first name and seven characters of last name
