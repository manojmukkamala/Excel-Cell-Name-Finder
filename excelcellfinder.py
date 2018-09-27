def getCellName(n):
    
    if (n <= 0 or n > 17179869184):
        return('Cell Out Of Range')
    else:
        q, r = divmod(n, 16384)
        string = ''

        if (r == 0):
            return ('XFD' + str(q))

        else: 
            while (r > 0):
                r, rem = divmod(r - 1, 26)
                string = chr(65 + rem) + string
            return (string + str(q + 1))
            
            
##### Test Cases #######

getCellName(1)            # Returns A1
getCellName(17179869184)  # Returns A1
getCellName(17179869185)  # Returns XFD1048576
getCellName(0)            # Returns 'Cell Out Of Range'
getCellName(-1)           # Returns 'Cell Out Of Range'
getCellName('Hello')      # Returns 'Cell Out Of Range'
