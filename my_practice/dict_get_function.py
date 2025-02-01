inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8
    }

def check_stock(item):
    return inventory.get(item,'Out of stock')

print(check_stock("orange"))