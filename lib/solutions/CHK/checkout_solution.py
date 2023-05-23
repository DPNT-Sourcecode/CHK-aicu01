

items = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
offers = {'A': {'count': 3, 'price': 130},
          'B': {'count': 2, 'price': 45}}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus not in items.keys():
        return -1
    

    

