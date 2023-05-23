

items = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
offers = {'A': {'count': 3, 'price': 130},
          'B': {'count': 2, 'price': 45}}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not set(skus).issubset(items.keys()):
        return -1
    
    if not skus:
        return 0

    total_cost = 0

    for item in items.keys():
        count = skus.count(item)
        if item in offers.keys() and count >= offers[item]['count']:
            offer = offers[item]
            total_cost += (count // offer['count']) * offer['price']
            count %= offer['count']
        total_cost += count * items[item]
    
    return total_cost
    

    
