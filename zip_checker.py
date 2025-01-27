def zip_checker(zipcode):
    #If `zipcode` has five characters, and the first two characters are NOT `'00'`, return `zipcode` as a string. Otherwise, return `'Invalid ZIP Code.'`. (ZIP Codes do not begin with 00 in the mainland U.S.)
    if len(zipcode) == 5 and zipcode[0:2] != '00':
        return zipcode
    #return 'Invalid ZIP Code'
    # If `zipcode` has four characters and the first character is NOT `'0'`, 
    # the function must add a zero to the beginning of the string and return the five-character `zipcode` as a string.
    if len(zipcode) == 4 and zipcode[0:1] !='0':
        zipcode =  '0' + zipcode 
        return str(zipcode)
    # If `zipcode` has four characters and the first character is `'0'`, 
    # the function must return `'Invalid ZIP Code.'`.
    if len(zipcode) == 4 and zipcode[0:1] == '0':
        return 'Invalid ZIP Code.'
    return 'Invalide ZIP Code.'




zip = "00280"
#print(len(zip))
#print(zip[0:1])
print(zip_checker(zip))

