from cache import LRUCache

cache = LRUCache(5)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')
cache.set('John', 'Depp')
cache.set('Robert', 'Downey Jr')
cache.set('Emma', 'Stone')

cache.set('Margot', 'Robbie')

print(cache.get('Jesse')) # вернёт 'James'
print(cache.get('Walter')) # вернёт ''

print(cache.get('Robert')) # вернёт 'Downey Jr'

cache.rem('Emma')

print(cache.get('Emma')) # вернёт ''