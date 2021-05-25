
bal variables to keep track of the hash table
count = 0
size = 1000

def hash_table(size):
    return [None] * size

def hash_item(key, value):
    return (key,value)

def hash_func(key):         #simple hash function
    index = hash(key) % 1000
    return index

def insert_hash(table,key,value):
    index = hash_func(key)
    item = hash_item(key,value)
    global count
    global size
    if count == size:
        raise Exception("Hash table limit reached")
    if table[index] == None:
        table[index] = item
    else:
        collision_handler(table, index, item)
    count = count + 1

def print_hash(table,key):
    index = hash_func(key)
"hashTable.py" 48L, 1065C
