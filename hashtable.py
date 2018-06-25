# Hash Table class

class HashTable():
    def __init__(self):
        self.table_size = 10
        self.table = [None] * self.table_size

    def _calc_hash(self, key):
        # Takes in a key and calculates a Hash
        # translates key to string if int or something else
        key = str(key)
        if len(key) > 1:
            return (ord(key[0]) + ord(key[-1])) % self.table_size
        elif len(key) == 1:
            return ord(key[0]) % self.table_size
        else:
            return -1

    def insert(self, key):
        value = self._calc_hash(key)
        #value = hash(str(key)) % self.table_size
        if self.table[value] is None:
            self.table[value] = [key]
        else:
            if key not in self.table[value]:
                self.table[value].append(key)
            else:
                print("Key already in table, will not insert duplicates!\n")

    def delete(self, key):
        value = self._calc_hash(key)
        #value = hash(str(key)) % self.table_size
        if self.table[value] is None:
            print("Key not in table. Could not delete!\n")
        else:
            if key in self.table[value]:
                self.table[value].remove(key)
            else:
                print("Key not in table. Could not delete!\n")

    def lookup(self, key):
        value = self._calc_hash(key)
        #value = hash(str(key)) % self.table_size
        if key in self.table[value]:
            return True
        else:
            return False


table = HashTable()

# Create some keys and add to hash table
table.insert('Testing')
table.insert(134)
table.insert(3)
table.insert('Test')
table.insert(34)
table.insert('Partying')
table.insert(1337)
table.insert(37)
table.insert('Prank')
table.insert('No')
table.insert(1)

# Try adding a key that already exist
print("Testing to add key 'Test' to table that already exist. Should show message:")
table.insert('Test')

# Deleting some keys from hash table
table.delete('Testing')
table.delete(1337)

# Try to delete an item which doesn't exist
print("Testing to delete key 'Noble' which doesn't exist. Should show message:")
table.delete('Noble')

# Try the look up functionality
print("Testing to look up 'No' in Hash table. Should show 'True'")
print(table.lookup('No'))
print("Testing to look up 'Help' in Hash table. Should show 'False'")
print(table.lookup('Help'))

# Print the full hash table
print("\nPrinting the full hash table")
print(table.table)
