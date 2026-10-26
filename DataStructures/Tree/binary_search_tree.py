from DataStructures.Tree import bst_node as bn
from DataStructures.List import single_linked_list as sll

def new_map ():
    bst = {"root":None}
    return bst

def put(my_bst,key,value):
    my_bst["root"] = insert_node(my_bst["root"],key,value)
    return my_bst

def insert_node(current_node,key,value):
    
    if current_node is None:
        return bn.new_node(key,value)
    key_node = current_node["key"]
    if key < key_node:
        current_node["left"] = insert_node(current_node["left"],key,value)
    elif key > key_node:
        current_node["right"] = insert_node(current_node["right"],key,value)
    else:
        current_node["value"] = value
    current_node["size"] = 1 + size_tree(current_node["left"]) + size_tree(current_node["right"])
    return current_node

def get(my_bst,key):
    nodo_encontrado = get_node(my_bst["root"],key)
    return bn.get_value(nodo_encontrado)

def get_node(current_node, key):
    
    if current_node is None:
        return None
    key_node = current_node["key"]
    if  key_node == key:
        return current_node
    elif key < key_node:
        return get_node(current_node["left"], key)
    elif key_node < key:
        return get_node(current_node["right"], key)

def size(my_bst):
    size = size_tree(my_bst["root"])
    return size

def size_tree(current_node):
    if current_node is None:
        return 0
    else:
        size = current_node["size"]
        return size
def contains(my_bst,key):
    valor = get(my_bst,key)
    if valor is None:
        return False
    else:
        return True
def is_empty(my_bst):
    return size(my_bst) == 0

def key_set(my_bst):
    key_list = sll.new_list()
    key_set_tree(my_bst["root"], key_list)
    return key_list

def key_set_tree(current_node, key_list):
    if current_node is not None:
        key_set_tree(current_node["left"], key_list)
        sll.add_last(key_list, bn.get_key(current_node))
        key_set_tree(current_node["right"], key_list)
        
    return key_list

def value_set(my_bst):
    value_list = sll.new_list()
    value_set_tree(my_bst["root"], value_list)
    return value_list

def value_set_tree(current_node, value_list):
    if current_node is not None:
        value_set_tree(current_node["left"], value_list)
        sll.add_last(value_list, bn.get_value(current_node))
        value_set_tree(current_node["right"], value_list)
        
    return value_list

def get_min(my_bst):
    min_node = get_min_node(my_bst["root"])
    if min_node is None:
        return None
    return bn.get_key(min_node)

def get_min_node(current_node):
    if current_node is None:
        return None
    if current_node["left"] is None:
        return current_node
    return get_min_node(current_node["left"])

def get_max(my_bst):
    max_node = get_max_node(my_bst["root"])
    if max_node is None:
        return None
    return bn.get_key(max_node)

def get_max_node(current_node):
    if current_node is None:
        return None
    if current_node["right"] is None:
        return current_node
    return get_max_node(current_node["right"])

def delete_min(my_bst):
    my_bst["root"] = delete_min_tree(my_bst["root"])
    return my_bst

def delete_min_tree(current_node):
    if current_node is None:
        return None
    if current_node["left"] is None:
        return current_node["right"]
    current_node["left"] = delete_min_tree(current_node["left"])
    current_node["size"] = 1 + size_tree(current_node["left"]) + size_tree(current_node["right"])
    
    return current_node

def delete_max(my_bst):
    my_bst["root"] = delete_max_tree(my_bst["root"])
    return my_bst

def delete_max_tree(current_node):
    if current_node is None:
        return None
    if current_node["right"] is None:
        return current_node["left"]
    current_node["right"] = delete_max_tree(current_node["right"])
    current_node["size"] = 1 + size_tree(current_node["right"]) + size_tree(current_node["left"])
    
    return current_node

def height(my_bst):
    return height_tree(my_bst["root"])

def height_tree(root):
    if root is None:
        return 0
    left_h = height_tree(root["left"])
    right_h = height_tree(root["right"])
    return 1 + max(left_h, right_h)


def keys(my_bst, key_initial, key_final):
    key_list = sll.new_list()
    keys_range(my_bst["root"], key_initial, key_final, key_list)
    return key_list

def keys_range(root, key_initial, key_final, list_key):
    if root is not None:
        key_node = root["key"]
        if key_initial < key_node:
            keys_range(root["left"], key_initial, key_final, list_key)
        if key_initial <= key_node <= key_final:
            sll.add_last(list_key, key_node)
        if key_node < key_final:
            keys_range(root["right"], key_initial, key_final, list_key)
    return list_key


def values(my_bst, key_initial, key_final):
    value_list = sll.new_list()
    values_range(my_bst["root"], key_initial, key_final, value_list)
    return value_list

def values_range(root, key_initial, key_final, list_values):
    if root is not None:
        key_node = root["key"]
        if key_initial < key_node:
            values_range(root["left"], key_initial, key_final, list_values)
        if key_initial <= key_node <= key_final:
            sll.add_last(list_values, bn.get_value(root))
        if key_node < key_final:
            values_range(root["right"], key_initial, key_final, list_values)
    return list_values