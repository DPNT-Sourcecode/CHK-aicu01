

items = {
    'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10,
    'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 80, 'L': 90,
    'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
    'S': 30, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 90,
    'Y': 10, 'Z': 50
}
offers = {
    'A': [{'count': 3, 'price': 130}, {'count': 5, 'price': 200}],
    'B': [{'count': 2, 'price': 45}],
    'E': [{'count': 2, 'price': 80, 'free': 'B'}],
    'F': [{'count': 2, 'price': 20, 'free': 'F'}],
    'H': [{'count': 5, 'price': 45}, {'count': 10, 'price': 80}],
    'K': [{'count': 2, 'price': 150}],
    'N': [{'count': 3, 'price': 120, 'free': 'M'}],
    'P': [{'count': 5, 'price': 200}],
    'Q': [{'count': 3, 'price': 80}],
    'R': [{'count': 3, 'price': 150, 'free': 'Q'}],
    'U': [{'count': 3, 'price': 120, 'free': 'U'}],
    'V': [{'count': 2, 'price': 90}, {'count': 3, 'price': 130}],
}

free_items_offer = ['E', 'F', 'N', 'R', 'U']

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

    sku_counts = handle_free_items(sku_counts)

    for sku, count in sku_counts.items():
        if sku in offers:
            sku_price = items[sku]
            offers[sku].sort(key=lambda x: x['count'], reverse=True)
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

    return total_cost

def handle_free_items(sku_counts):
    for free_offer in free_items_offer:
        if free_offer in sku_counts and free_offer in offers:
            for offer in offers[free_offer]:
                if 'free' in offer:
                    free_item = offer['free']
                    if free_item in sku_counts:
                        offer_count = offer['count'] + 1 if free_item == free_offer else offer['count']
                        free_count = sku_counts[free_offer] // offer_count 
                        sku_counts[free_item] = max(sku_counts[free_item] - free_count, 0)

    return sku_counts