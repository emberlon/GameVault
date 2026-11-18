class HashTable:
    def __init__(self, capacity=16):
        if capacity < 1:
            raise ValueError("Capacity must be at least 1.")
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        self._size = 0

    def _index(self, key):
        return hash(key.casefold()) % self.capacity

    def insert(self, key, value):
        index = self._index(key)
        bucket = self.buckets[index]

        for position, (existing_key, _) in enumerate(bucket):
            if existing_key.casefold() == key.casefold():
                bucket[position] = (key, value)
                return

        bucket.append((key, value))
        self._size += 1

    def get(self, key):
        bucket = self.buckets[self._index(key)]
        for existing_key, value in bucket:
            if existing_key.casefold() == key.casefold():
                return value
        return None

    def remove(self, key):
        bucket = self.buckets[self._index(key)]
        for position, (existing_key, _) in enumerate(bucket):
            if existing_key.casefold() == key.casefold():
                del bucket[position]
                self._size -= 1
                return True
        return False

    def __len__(self):
        return self._size
