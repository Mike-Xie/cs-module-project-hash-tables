class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implemented as an empty list that will hold entries
    """

    def __init__(self, capacity: int):
        if capacity < MIN_CAPACITY:
            print("Input capacity under minimum (8), setting to minimum.")
            self.capacity = 8
        else:
            self.capacity = capacity
        self.table = [None] * capacity
        self.load = 0 

    def get_num_slots(self) -> int:
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implemented as just returning length of table.
        """
        return len(self.table)


    def get_load_factor(self) -> float:
        """
        Return the load factor for this hash table.
        Number of keys divided by capacity
        Implement this.
        """
        # counts number of keys
        # refactor later to return a number that increases
        # when put is called 
        number_of_keys = sum(1 for _ in filter(None.__ne__, self.table))
        return (number_of_keys/capacity)


    def fnv1(self, key: str, seed: int = 0) -> int:
        """
        FNV-1 Hash, 64-bit for strings, breaks for ints
        ^ is bitwise XOR and breaks on strings 
        """
        # constants, prime and offset are on wikipedia page
        # https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function#FNV-1_hash
        FNV_PRIME = 1099511628211
        offset_basis = 14695981039346656037

        hashed = offset_basis + seed 
        for char in key:
            hashed = hashed * FNV_PRIME
            hashed = hashed ^ ord(char)
        return hashed 

    def djb2(self, key: str, seed: int = 0) -> int:
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        pass 

    def hash_index(self, key: str) -> int:
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.fnv1(key) % self.capacity

    def put(self, key: str, value: str) -> None:
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        self.load += 1
        insert_index = self.hash_index(key)
        self.table[insert_index] = HashTableEntry(key = key, value=value)


    def delete(self, key: str) -> None:
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        delete_index = self.hash_index(key)

        if self.table[delete_index].key is None:
            print("Warning, key not found")
        else:
            self.load -= 1 
            self.table[delete_index] = HashTableEntry(key, None)

  
    def get(self, key: str) -> str:
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        hash_entry = self.table[index]
        if hash_entry is not None:
            return hash_entry.value 
        else:
            return None 


    def resize(self, new_capacity: int) -> None:
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        """
        self.capacity *= 2

        old_table = self.table.copy()

        self.table = [None] * self.capacity

        for i in range(len(old_table)):
            old_hash = old_table[i]
            while old_hash:
                self.put(old_hash.key, old_hash.value)

        



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    # ht.delete("line_1")
    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
