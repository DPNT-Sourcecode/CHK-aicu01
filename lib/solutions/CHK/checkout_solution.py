

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

    if item in offers:
        for offer in sorted(offers[item], key=lambda x: x['count'], reverse=True):
            while count >= offer['count']:
                total_cost += offer['price']
                count -= offer['count']

                if 'free' in offer and offer['free'] in items:
                    free_item = offer['free']
                    free_item_count = skus.count(free_item)
                    eligible_offers = min(count // offer['count'], free_item_count)
                    total_cost -= eligible_offers * items[free_item]
    return total_cost, skus

print(checkout('EEEEB'))