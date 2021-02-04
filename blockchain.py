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


