

items = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10}
offers = {
    'A': [{'count': 3, 'price': 130}, {'count': 5, 'price': 200}],
    'B': [{'count': 2, 'price': 45}],
    'E': [{'count': 2, 'free': 'B'}],
    'F': [{'count': 2, 'free': 'F'}],
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

    if 'E' in sku_counts and 'B' in sku_counts:
        free_count = sku_counts['E'] // 2
        sku_counts['B'] = max(sku_counts['B'] - free_count, 0)

    for sku, count in sku_counts.items():
        if sku in offers:
            sku_price = items[sku]
            offers[sku].sort(key=lambda x: x['count'], reverse=True)
            while count > 0:
                offer_applied = False
                for offer in offers[sku]:
                    offer_cost, remaining_count, free_sku = apply_offer(count, offer)
                    total_cost += offer_cost
                    if free_sku and free_sku in sku_counts:
                        free_count = min(remaining_count, sku_counts[free_sku])
                        remaining_count -= free_count
                        sku_counts[free_sku] -= free_count
                    count = remaining_count
                    offer_applied = offer_cost > 0
                    if offer_applied:
                        break
                if not offer_applied:
                    total_cost += count * sku_price
                    
        else:
            total_cost += count * items[sku]

 

    
    return total_cost


def apply_offer(count, offer):
    offer_count = offer.get('count', float('inf'))
    offer_price = offer.get('price', 0)
    free_sku = offer.get('free')
    if count >= offer_count:
        free_count = count // offer_count
        remaining_count = count % offer_count
        return (offer_price * free_count, remaining_count, free_sku)
    return (0, count, free_sku)


print(checkout('FFF'))

