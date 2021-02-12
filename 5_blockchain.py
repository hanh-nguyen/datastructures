import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data):
      self.timestamp = timestamp
      self.data = data
      self.hash = self.calc_hash()
      self.previous_hash = None
      self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.data) + str(self.timestamp)
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()

    def get_hash(self):
        return self.hash

    def __str__(self):
        return f"Data: {self.data}\nTimestamp: {self.timestamp}\nHash: {self.get_hash()}\nPrevHash: {self.previous_hash}"

class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        block = Block(datetime.datetime.utcnow(), data)
        if self.head is None:
            block.previous_hash = 0
            self.head = block
            self.tail = self.head
            return
        self.tail.next = block
        block.previous_hash = self.tail.get_hash()
        self.tail = self.tail.next

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

# Test
bc = Blockchain()
bc.append(9)
bc.append(5)
print(bc.get_head()) 
# Data: 9
# Timestamp: 2021-02-06 23:58:40.291380
# Hash: 1503044ebfa693cfa7d763c38f4ecedeb14e8c97284c5be825085073c5f98c94
# PrevHash: 0
print(bc.get_tail())
# Data: 5
# Timestamp: 2021-02-06 23:58:40.291409
# Hash: 1bccb31fd4c7e166b21ac6a5a9d0e5496aeb260eadcacbecf073471bf3614b28
# PrevHash: 1503044ebfa693cfa7d763c38f4ecedeb14e8c97284c5be825085073c5f98c94



