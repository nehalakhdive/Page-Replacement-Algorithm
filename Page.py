# Initialize global variables
cache = {}
capacity = 0
order = []

def initialize(cap: int):
    global capacity
    capacity = cap
    global cache
    cache = {}
    global order
    order = []

def refer(page: int):
    global cache, order
    if page not in cache:
        if len(order) == capacity:
            least_recently_used = order.pop(0)
            cache.pop(least_recently_used)
        cache[page] = True
    else:
        order.remove(page)
    order.append(page)

def display():
    global order
    print("Pages in cache:", order)

# Example usage
capacity = 3
pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]

initialize(capacity)
for page in pages:
    refer(page)
    display()
