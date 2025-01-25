def unpurchased_items(all_items, purchased_items):
    unpurchased_items = []
    for item in purchased_items:
        if item not in purchased_items:
            unpurchased_items.append(item)
    total_items = len(all_items)
    total_purchased_items = len(purchased_items)
    percantage_unpurchase = (unpurchased_items / total_items ) * 100
    print(f"{percantage_unpurchase} of {total_items} items unpurchased.")
    #print(f"{percentage_unverified:.2f}% unverified.")
purchased_items = ['apple', 'banana', 'orange']
all_items = ['apple', 'banana', 'orange', 'grape', 'watermelon']

unpurchased_items(all_items, purchased_items)

  