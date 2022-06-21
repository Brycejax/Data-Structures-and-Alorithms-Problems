
class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size

    def _hash(self, key):
        key = str(key)
        hash = 0
        i = 0
        for i, char in enumerate(key):
            hash = (hash + ord(char)*i) % self.size
        return hash
    
    def set(self, key, value):
        address = self._hash(key)
        if self.data[address] is None:
            self.data[address] = [(key,value)]
        else:
            self.data[address].append((key, value))
    
    def get(self, key):
        address = self._hash(key)
        currentBucket = self.data[address]
        if (currentBucket):
            for i in range(len(currentBucket)):
                if (currentBucket[i][0] == key):
                    return currentBucket[i][1]
        return None

    def keys(self):
        keys = []
        for i in self.data:
            if not i is None:
                for pair in i:
                    keys.append(pair[0])
        return keys


# Testing

hash = HashTable(50)
hash.set('grapes', 10000)
hash.set('oranges', 200)
hash.set('apples', 170)
hash.set('bananas', 260)

print(hash.keys())