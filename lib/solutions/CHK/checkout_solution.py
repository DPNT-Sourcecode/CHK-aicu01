

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

    sku_counts = {sku: skus.count(sku) for sku in set(skus)}

    return calculate_cost(sku_counts)


    
    
def calculate_cost(sku_counts):
    total_cost = 0

    for sku, count in sku_counts.items():
        if sku in offers:
            sku_price = items[sku]
            while count > 0:
                offer_applied = False
                for offer in offers[sku]:
                    offer_count = offer['count']
                    offer_price = offer['price']
                    if count >= offer_count:
                        total_cost += offer_price
                        count -= offer_count
                        offer_applied = True
                        break
                if not offer_applied:
                    total_cost += count * sku_price
                    count = 0
        else:
            total_cost += count * items[sku]

    if 'E' in sku_counts and 'B' in sku_counts:
        free_count = min(sku_counts['E'], sku_counts['B'])
        total_cost -= free_count * items['B']

    
    return total_cost

print(checkout('ABCD'))