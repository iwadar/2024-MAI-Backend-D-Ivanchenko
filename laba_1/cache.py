class LRUCache:
    def __init__(self, capacity: int=10) -> None:
        self.cache = dict()
        self.maxSizeCache = capacity

    def get(self, key: str) -> str:
        if value := self.cache.get(key, ''):
            del self.cache[key]
            self.cache[key] = value
        return value

    def set(self, key: str, value: str) -> None:
        if key in self.cache:
            del self.cache[key]
        
        self.cache[key] = value
        
        if len(self.cache) > self.maxSizeCache:
            del self.cache[next(iter(self.cache))]

    def rem(self, key: str) -> None:
        if key in self.cache:
            del self.cache[key]
