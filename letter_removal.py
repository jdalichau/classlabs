#CNT 336 Spring 2018
#Jaosn Dalichau
#jdalichau@gmail.com

#help with .replace syntax found it the book 'how to think like a computer scientist' interactive edition

#This code is designed to take an input name and remove vowels of any case
n = input('Enter your full name: ') #input statement for a persons full name


if n == ('a') or ('e') or ('i') or ('o') or ('u'): #If statement declaring lower case values
    n = n.replace('a','')#remove a
    n = n.replace('e', '')#remove e
    n = n.replace('i','')#remove i
    n = n.replace('o','')#remove o
    n = n.replace('u','')#remove u

    if n == ('A') or ('E') or ('I') or ('O') or ('U'):#second if statement declaring upper case values
        n = n.replace('A','')#remove A
        n = n.replace('E', '')#remove E
        n = n.replace('I','')#remove I
        n = n.replace('O','')#remove O
        n = n.replace('U','')#remove U
        print(n)#print the input with or without replaced values












