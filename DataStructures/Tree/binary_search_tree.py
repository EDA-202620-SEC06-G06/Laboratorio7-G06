from DataStructures.Tree import bst_node as bn
from DataStructures.List import single_linked_list as sll

def new_map ():
    bst = {"root":None}
    return bst

def put(my_bst,key,value):
    my_bst = insert_node(my_bst["root"],key,value)

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
    lista = sll.new_list()
    set = key_set_tree(lista)
    return set
    
def key_set_tree(current_node,key_list):
    if current_node is not None:
        key_set_tree(current_node["left"],key_list)
        sll.add_last(key_list,current_node["key"])
        key_set_tree(current_node["right"], key_list)
    return current_node