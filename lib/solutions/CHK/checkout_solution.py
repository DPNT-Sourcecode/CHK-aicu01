

items = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
offers = {
    'A': [{'count': 3, 'price': 130}, {'count': 5, 'price': 200}],
    'B': [{'count': 2, 'price': 45}],
    'E': [{'count': 2, 'price': 80, 'free': 'B'}],    
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
        cost, skus = calculate_cost(item, count, skus)
        total_cost += cost

    return total_cost


    
    
def calculate_cost(item, count, skus):
    total_cost = 0

    if not any(offer.get('free') == item for offer in offers.values() for offer in offer):
        total_cost += count * items[item]
    else:
        while count > 0:
            for offer in offers[item]:
                if 'free' in offer and offer['free'] == item and count >= offer['count']:
                    count_free_item = skus.count(offer['free'])
                    if count_free_item > 0:
                        count -= offer['count']
                        skus = skus.replace(offer['free'], '', 1)
                        total_cost += offer['price']
                        break
            
            if count >= offer['count']:
                total_cost += offer['price']
                count -= offer['count']
            else: 
                break


    
    
    
    return total_cost, skus

print(checkout('ABCDE'))