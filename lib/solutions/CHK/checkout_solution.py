

items = {
    'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10,
    'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 70, 'L': 90,
    'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
    'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17,
    'Y': 20, 'Z': 21
} #cc xyzyz

offers = {
    'A': [{'count': 3, 'price': 130}, {'count': 5, 'price': 200}],
    'B': [{'count': 2, 'price': 45}],
    'E': [{'count': 2, 'price': 80, 'free': 'B'}],
    'F': [{'count': 2, 'price': 20, 'free': 'F'}],
    'H': [{'count': 5, 'price': 45}, {'count': 10, 'price': 80}],
    'K': [{'count': 2, 'price': 120}],
    'N': [{'count': 3, 'price': 120, 'free': 'M'}],
    'P': [{'count': 5, 'price': 200}],
    'Q': [{'count': 3, 'price': 80}],
    'R': [{'count': 3, 'price': 150, 'free': 'Q'}],
    'U': [{'count': 3, 'price': 120, 'free': 'U'}],
    'V': [{'count': 2, 'price': 90}, {'count': 3, 'price': 130}],
}

group_discounts = {
    'STXYZ': [{'count': 3, 'price': 45}]
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

    total_cost, sku_counts = group_discount_cost(sku_counts)

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

def group_discount_cost(sku_counts):
    total_cost = 0
    
    eligible_skus = []
    discounted_skus = []
    for group, discounts in group_discounts.items():
        group_counts = {sku: sku_counts.get(sku, 0) for sku in group}
        total_count = sum(group_counts.values())
        discounts.sort(key=lambda x: x['count'], reverse=True)

        for sku, count in group_counts.items():
            eligible_skus += [sku] * count
        
        for discount in discounts:
            while total_count >= discount['count']:
                total_cost += discount['price']
                total_count -= discount['count']

                for _ in range(discount['count']):
                    max_price_sku = max(group_counts, key=lambda sku: (items[sku] if group_counts[sku] > 0 else -1))
                    group_counts[max_price_sku] -= 1
                    discounted_skus.append(max_price_sku)
                
        if total_count > 0:
            remaining_skus = [sku for sku in eligible_skus if sku not in discounted_skus or discounted_skus.remove(sku)]
            for sku in remaining_skus:
                total_cost += items[sku]

    for sku in eligible_skus:
        sku_counts[sku] -= 1

    return total_cost, sku_counts




