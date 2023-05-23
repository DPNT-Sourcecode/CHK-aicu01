

items = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
offers = {
    'A': [{'count': 3, 'price': 130}, {'count': 5, 'price': 200}],
    'B': [{'count': 2, 'price': 45}],
    'E': [{'count': 2, 'free': 'B'}],    
}


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
        total_cost += calculate_cost(item, count, skus)

    return total_cost


    
    
def calculate_cost(item, count, skus):
    total_cost = 0

    if item in offers.keys():
        for offer in offers.keys():
            if 'free' in offer and count >= offer['count']:
                count_free_item = items.count(offer['free'])
                if count_free_item > 0:
                    skus = skus.replace(offer['free'], '', 1)
                    count -= offer['count']
            
            while count >= offer['count']:
                total_cost += offer['price']
                count -= offer['count']

        total_cost += count * items[item]
    
    return total_cost
    
