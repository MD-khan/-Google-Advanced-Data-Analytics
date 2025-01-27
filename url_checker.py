
### YOUR CODE HERE ###
def url_checker(url):
    store_id = url.split('/')[-1]
    protocol = url.split('://')[0]
    #If both the protocol and the store ID are invalid
    if protocol != 'https' and len(store_id) != 7:
        print(f"{protocol} is an invalid protocol.'")
        print(f"'{store_id} is an invalid store ID.'")
    #If only the protocol is invalid
    elif protocol != 'https':
        print(f"{protocol} is an invalid protocol.'")
    # If only the store ID is invalid:
    elif len(store_id) != 7:
        print(f"'{store_id} is an invalid store ID.'")
    else:
        return store_id
    
#url = 'https://exampleURL1.com/r626c36'
#url_checker('https://exampleURL1.com/r626c3')
url_checker('http://exampleURL1.com/r626c3')    # 'http: is an invalid protocol.'
print()                                         # 'r626c3 is an invalid store ID.'

url_checker('ftps://exampleURL1.com/r626c36')   # 'ftps: is an invalid protocol.
print()
url_checker('https://exampleURL1.com/r626c3')   # 'r626c3 is an invalid store ID.'
print()
url_checker('https://exampleURL1.com/r626c36')  # 'r626c36'