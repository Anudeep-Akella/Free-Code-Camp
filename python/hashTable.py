class HashTable:
    def __init__(self):
        self.collection = dict()

    def hash(self,key):
        sum = 0
        for i in key:
            sum += ord(i)
        return sum
        
    def add(self,key,value):
        key_hash = self.hash(key)
        if key_hash not in self.collection:
            self.collection[key_hash] = {}
        self.collection[key_hash][key] = value

    def remove(self,key):
        key_hash = self.hash(key)
        if key_hash in self.collection and key in self.collection[key_hash]:
            del self.collection[key_hash][key]        

    def lookup(self,key):
        key_hash = self.hash(key)
        if key_hash in self.collection:
            if key in self.collection[key_hash]:
                return self.collection[key_hash][key]
        return None
