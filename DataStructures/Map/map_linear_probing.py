from DataStructures.Map  import map_functions as mf
from DataStructures.List  import array_list as ar
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
    'current_factor': 0,
    'limit_factor': load_factor,
    'size': 0,
    'type': 'PROBE_HASH_MAP'}
    for i in range(capacity):
        entry = me.new_map_entry(None, None)
        ar.add_last(hash_table['table'], entry)
    return hash_table

def is_available(table, pos):

   entry = ar.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):

   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   visited = 0
   # visited evita un ciclo infinito si la tabla no tiene ninguna casilla None
   while not found and visited < my_map["capacity"]:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = ar.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, ar.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
      visited += 1
   return ocupied, first_avail


def rehash(my_map) -> dict:
    current_capacity = my_map["capacity"]
    new_capacity_target = current_capacity * 2
    
    limit_factor = my_map["limit_factor"]
    prime = my_map["prime"]
    new_capacity = mf.next_prime(new_capacity_target)
    
    new_map_obj = {
        'prime': prime,
        'capacity': new_capacity,
        'scale': my_map['scale'],
        'shift': my_map['shift'],
        'table': ar.new_list(),
        'current_factor': 0,
        'limit_factor': limit_factor,
        'size': 0,
        'type': 'PROBE_HASH_MAP'
    }
    
    for _ in range(new_capacity):
        entry = me.new_map_entry(None, None)
        ar.add_last(new_map_obj['table'], entry)

    old_table = my_map["table"]
    old_capacity = my_map["capacity"]
    
    for indice_tabla_antigua in range(old_capacity):
        entry = ar.get_element(old_table, indice_tabla_antigua)
        llave = me.get_key(entry)
        valor = me.get_value(entry)
        
        if llave is not None and llave != "__EMPTY__":
            new_map_obj = put(new_map_obj, llave, valor)
            
    my_map.update(new_map_obj)
    
    return my_map
 
def put(my_map, key, value) -> dict:
    hash_position = mf.hash_value(my_map, key)
    occupied, position = find_slot(my_map, key, hash_position)
    
    entry = ar.get_element(my_map["table"], position)
    
    if occupied:
        me.set_value(entry, value)
    else:
        me.set_key(entry, key)
        me.set_value(entry, value)
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
        
        if my_map["current_factor"] > my_map["limit_factor"]:
            my_map = rehash(my_map)
            
    return my_map
 
def contains(my_map, key) -> bool:
    hash_value = mf.hash_value(my_map, key)
    occupied, position = find_slot(my_map, key, hash_value)
    return occupied


def remove(my_map, key) -> dict:
    hash_value = mf.hash_value(my_map, key)
    occupied, position = find_slot(my_map, key, hash_value)
    
    if occupied:
        entry = ar.get_element(my_map["table"], position)
        me.set_key(entry, "__EMPTY__")
        me.set_value(entry, "__EMPTY__")
        my_map["size"] -= 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
        
    return my_map
 
def get(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    occupied, position = find_slot(my_map, key, hash_value)
    
    if occupied:
        entry = ar.get_element(my_map["table"], position)
        return me.get_value(entry)
        
    return None


def size(my_map) -> int:
    return my_map["size"]


def is_empty(my_map) -> bool:
    return my_map["size"] == 0


def key_set(my_map):
    keys_list = ar.new_list()
    for i in range(my_map["capacity"]):
        entry = ar.get_element(my_map["table"], i)
        key = me.get_key(entry)
        if key is not None and key != "__EMPTY__":
            ar.add_last(keys_list, key)
    return keys_list


def value_set(my_map):
    values_list = ar.new_list()
    for i in range(my_map["capacity"]):
        entry = ar.get_element(my_map["table"], i)
        key = me.get_key(entry)
        if key is not None and key != "__EMPTY__":
            ar.add_last(values_list, me.get_value(entry))
    return values_list