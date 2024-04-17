# resources
# https://www.youtube.com/watch?v=cNWsgbKwwoU
# https://srm.file.force.com/servlet/fileField?id=0BE3x000000LdNG
class HashTable:
    def __init__(self, initial_capacity=40):
        # Space Complexity: O(N), where N is the initial_capacity
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a key-value pair into the hash table.
    # Time Complexity: O(1) on average
    # Space Complexity: O(1) on average
    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Search for a key or value in the hash table.
    # Time Complexity: O(N), where N is the number of elements in the hash table
    # Space Complexity: O(1) on average
    def search(self, key_or_value):
        # First, check if the input is a key
        for bucket_list in self.table:
            for key_value in bucket_list:
                if key_value[0] == key_or_value:
                    return key_value[1]

        # If not found, check if the input is a value
        for bucket_list in self.table:
            for key_value in bucket_list:
                if key_value[1] == key_or_value:
                    return key_value[0]

        # If neither key nor value is found, return None
        return None

    # Removes a key-value pair from the hash table.
    # Time Complexity: O(N), where N is the number of elements in the hash table
    # Space Complexity: O(1) on average
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            bucket_list.remove([kv[0], kv[1]])

    # Lists all elements of the hash table.
    # Time Complexity: O(N), where N is the number of elements in the hash table
    # Space Complexity: O(N), where N is the number of elements in the hash table
    def list_all(self):
        print(self.table)
        return self.table