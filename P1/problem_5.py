import hashlib
import datetime

def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.prev = None

    def calc_hash(self):
      sha = hashlib.sha256()
      hash_str = self.data.encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

class Blockchain:

    # Function to initialize the Linked
    # List object
    def __init__(self, head):
        self.head = head

    def printList(self):
            temp = self.head
            while (temp):
                print (temp.data, temp.hash, temp.previous_hash)
                temp = temp.prev

# Sample chain

blockA = Block(datetime.datetime.now().timestamp(), "blockA", None)

blockB = Block(datetime.datetime.now().timestamp(), "blockB", blockA.hash)
blockB.prev = blockA

bc = Blockchain(blockB)

# Test Case 1 - Normal case
bc.printList() # returns two entries
print()

blockC = Block(datetime.datetime.now().timestamp(), "blockC", blockB.hash)
blockC.prev = bc.head

bcC = Blockchain(blockC)

bcC.printList() # returns an extra entry than the above output
print()

# Test Case 2 - Edge case with incorrect hash
blockD = Block(datetime.datetime.now().timestamp(), "bad hash", "BAD HASH")
blockD.prev = blockB

bcD = Blockchain(blockD)

bcD.printList() # print out the chain but notice blockD's previous_hash is not pointed to the blockB's hash
print()

# Test Case 2 - Edge case with incorrect hash
blockE = Block(datetime.datetime.now().timestamp(), "blockE", None)
blockE.prev = blockB

bcE = Blockchain(blockE)

bcE.printList() # print out the chain but notice blockE's previous_hash is set to None and not pointed to the blockB's hash
print()