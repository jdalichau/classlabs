def conversion(): #define conversion
    H = 'Hello' #Hello with H
    h = 'hello' #hello with h
    c = 'HeLlO' #hello wi H and L and I

    if h.upper() == H.upper() and h.upper() == c.upper() and H.upper() == c.upper(): #compaare the above assignments
        return(True) #return true if the match or not
    else:
        return(False) #else statement


print(str(conversion())) #print true/false statement
