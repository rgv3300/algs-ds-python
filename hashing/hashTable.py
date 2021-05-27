#global variables to keep track of the hash table
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
    while table[index][0] != key:      #in case there is a collision:
        index = index + 1
    print(table[index])
    
def delete_hash(table,key):
    index = hash_func(key)
    while table[index][0] != key:
        index = index + 1
    table[index] = None
    
    
def collision_handler(table,index,item):         #handling collisions using open addressing
        while table[index] != None:
            index = index + 1
        table[index] = item
        



a = hash_table(size)

insert_hash(a,1000,'john')
insert_hash(a,1000,'edward')
print_hash(a,1000)
