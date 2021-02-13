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

# Test 1
bc = Blockchain()
print(bc.get_head()) 
# None
print(bc.get_tail())
# None

# Test 2
bc.append(9)
bc.append(5)
print(bc.get_head()) 
# Data: 9
# Timestamp: 2021-02-13 11:55:51.918102
# Hash: 7ed6f59eb0290bc014f07d7cb8962e41b034b2af1ca30c187248a14520d1570a
# PrevHash: 0
print(bc.get_tail())
# Data: 5
# Timestamp: 2021-02-13 11:55:51.918429
# Hash: 5c311961fb2db40f0c1bf4e1606c4e7ae1f84ff2c0594b0bb6a3eeef3b67f38e
# PrevHash: 7ed6f59eb0290bc014f07d7cb8962e41b034b2af1ca30c187248a14520d1570a

# Test 3
bc.append("A")   
print(bc.get_head())  
# Data: 9
# Timestamp: 2021-02-13 11:55:51.918102
# Hash: 7ed6f59eb0290bc014f07d7cb8962e41b034b2af1ca30c187248a14520d1570a
# PrevHash: 0
print(bc.get_tail())   
# Data: A
# Timestamp: 2021-02-13 11:55:51.918501
# Hash: e8a4b810d812f786626374bdb3dd69d6c08012af24a6126ae1614fb58b1f135a
# PrevHash: 5c311961fb2db40f0c1bf4e1606c4e7ae1f84ff2c0594b0bb6a3eeef3b67f38e 



