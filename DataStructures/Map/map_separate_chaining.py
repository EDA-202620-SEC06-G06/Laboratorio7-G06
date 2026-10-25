from DataStructures.Map  import map_functions as mf
from DataStructures.List  import array_list as ar
from DataStructures.List  import single_linked_list as sl   
from DataStructures.Map  import map_entry as me
import random as rd

def new_map(num_keys, load_factor, prime=109345121):
    capacity = mf.next_prime(num_keys//load_factor)
    scale = rd.randint(1, prime-1)
    shift = rd.randint(0, prime-1)
    hash_table = {'prime': prime,
    'capacity': capacity,
    'scale': scale,
    'shift': shift,
    'table': ar.new_list(),
    'size': 0,
    'limit_factor': load_factor,
    'current_factor': 0,
    'type': 'CHAINING_HASH_MAP'}
    for _ in range(capacity):
        bucket = sl.new_list()
        ar.add_last(hash_table['table'], bucket)
    return hash_table

def default_compare(key, element):

   if (key == me.get_key(element)):
      return 0
   elif (key > me.get_key(element)):
      return 1
   return -1

def rehash(my_map):
    old_capacity = my_map["capacity"]
    new_capacity = mf.next_prime(old_capacity * 2)
    
    new_hash_table = {'prime': my_map["prime"],
    'capacity': new_capacity,
    'scale': my_map["scale"],
    'shift': my_map["shift"],
    'table': ar.new_list(),
    'size': 0,
    'limit_factor': my_map["limit_factor"],
    'current_factor': 0,
    'type': 'CHAINING_HASH_MAP'}
    for _ in range(new_capacity):
        bucket = sl.new_list()
        ar.add_last(new_hash_table['table'], bucket)
        
    for i in range(old_capacity):
        bucket = ar.get_element(my_map["table"], i)
        n_elements = sl.size(bucket)
        for j in range(n_elements):
            entry = sl.get_element(bucket, j)
            key = me.get_key(entry)
            value = me.get_value(entry)
            new_hash_value = mf.hash_value(new_hash_table, key)
            new_bucket = ar.get_element(new_hash_table["table"], new_hash_value)
            new_entry = me.new_map_entry(key, value)
            sl.add_last(new_bucket, new_entry)
            new_hash_table["size"] += 1
            
    new_hash_table["current_factor"] = new_hash_table["size"] / new_hash_table["capacity"]
    
    my_map["capacity"] = new_hash_table["capacity"]
    my_map["table"] = new_hash_table["table"]
    my_map["current_factor"] = new_hash_table["current_factor"]
    my_map["size"] = new_hash_table["size"]

    return my_map

def put(my_map, key, value):
    
    hash_key = mf.hash_value(my_map, key)
    search = ar.get_element(my_map["table"],hash_key)
    entry_found = False
    n_elements = sl.size(search)
    j = 0
    while j < n_elements and not entry_found:
        current_entry = sl.get_element(search, j)
        if default_compare(key, current_entry) == 0:
            me.set_value(current_entry, value)
            entry_found = True
        j += 1
    if not entry_found:
        new_entry = me.new_map_entry(key, value)
        sl.add_last(search, new_entry)
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
        if my_map["current_factor"] >= my_map["limit_factor"]:
            rehash(my_map)
    return my_map

def contains(my_map, key):
    hash_key = mf.hash_value(my_map, key)
    search = ar.get_element(my_map["table"], hash_key)
    n_elements = sl.size(search)
    found = False
    j = 0
    while j < n_elements and not found:
        current_entry = sl.get_element(search, j)
        if default_compare(key, current_entry) == 0:
            found = True
        j += 1
    return found

def get(my_map, key):
    hash_key = mf.hash_value(my_map, key)
    search = ar.get_element(my_map["table"], hash_key)
    n_elements = sl.size(search)
    result = None
    found = False
    j = 0
    while j < n_elements and not found:
        current_entry = sl.get_element(search, j)
        if default_compare(key, current_entry) == 0:
            result = me.get_value(current_entry)
            found = True
        j += 1
    return result

def remove(my_map, key):
    hash_key = mf.hash_value(my_map, key)
    search = ar.get_element(my_map["table"], hash_key)
    n_elements = sl.size(search)
    found = False
    j = 0
    while j < n_elements and not found:
        current_entry = sl.get_element(search, j)
        if default_compare(key, current_entry) == 0:
            sl.delete_element(search, j)
            my_map["size"] -= 1
            my_map["current_factor"] = my_map["size"] / my_map["capacity"]
            found = True
        j += 1
    return my_map

def size(my_map):
    return my_map["size"]

def is_empty(my_map):
    
    if my_map["size"] == 0:
        return True
    else:
        return False

def key_set(my_map):
    
    keys_list = ar.new_list()
    for i in range(my_map["capacity"]):
        search = ar.get_element(my_map["table"], i)
        n_elements = sl.size(search)
        for j in range(n_elements):
            entry = sl.get_element(search, j)
            key = me.get_key(entry)
            ar.add_last(keys_list, key)
    return keys_list

def value_set(my_map):

    values_list = ar.new_list()
    for i in range(my_map["capacity"]):
        search = ar.get_element(my_map["table"], i)
        n_elements = sl.size(search)
        for j in range(n_elements):
            entry = sl.get_element(search, j)
            ar.add_last(values_list, me.get_value(entry))
    return values_list