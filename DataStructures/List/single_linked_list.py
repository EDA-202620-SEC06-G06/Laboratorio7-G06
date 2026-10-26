from DataStructures.List import list_node as nd


def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0
    }
    
    return newlist

def get_element(my_list, pos):
    searchpos = 0 
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos +=1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count =  0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp =  temp["next"]
            count += 1
    if not is_in_array:
        count = -1
    return count

def add_first(new_list: dict, element):
    
    node = nd.new_single_node(element)
    node["next"] = new_list["first"]
    new_list["first"] = node

    if new_list["last"] == None:
        new_list["last"] = node
    
    new_list["size"] += 1
    
    return new_list
    
    
def add_last(new_list: dict, element):
    
    node = nd.new_single_node(element)
    
    if new_list["last"] == None:
        new_list["last"] = node
        new_list["first"] = node
    
    else:
        new_list["last"]["next"] = node
        new_list["last"] = node 
    
    new_list["size"] += 1
    
    return new_list
    
def size(new_list:dict):
    
    tamanio = new_list["size"]
    
    return tamanio
    
def first_element(new_list:dict):
    
    if new_list["first"] == None:
        raise Exception('IndexError: list index out of range')
    else:
        primero = new_list["first"]["info"]
    return primero
    
def is_empty(new_list: dict):
    if new_list["size"] == 0:
        return True
    return False
    
def last_element(new_list: dict):
    
    if new_list["first"] == None:
            raise Exception('IndexError: list index out of range')
    else:
        ultimo = new_list["last"]["info"]
    return ultimo

def encontrar_posicion(new_list, pos):
    if pos < 0 or pos >= new_list["size"]:
        raise Exception("Posicion fuera de rango")
    elif is_empty(new_list):
        raise Exception("La lista esta vacia")
    else:
        i = 0
        d = new_list["first"]
        while i < pos:
            d = d["next"]
            i += 1
        return d
    
def delete_element(new_list, pos):
    if pos < 0 or pos >= new_list["size"]:
        raise Exception("Posicion fuera de rango")
    elif is_empty(new_list):
            raise Exception("Lista vacia")
    elif pos == 0:
        return remove_first(new_list)
    elif pos == new_list["size"]-1:
        return remove_last(new_list)
    else:
        nodo_anterior = encontrar_posicion(new_list, pos-1)
        nodo_eliminado = nodo_anterior["next"]
        info_eliminada = nodo_eliminado["info"]
        nodo_anterior["next"] = nodo_eliminado["next"]
        new_list["size"] -= 1
        return info_eliminada
    
def remove_first(new_list: dict):
    
    if is_empty(new_list):
        raise Exception("Lista vacia")
    elif new_list["size"] == 1:
        info_eliminada = new_list["first"]["info"]
        new_list["first"] = None
        new_list["last"] = None
        new_list["size"] -= 1
        return info_eliminada
    else:
        info_eliminada = new_list["first"]["info"]
        new_list["first"] = new_list["first"]["next"]
        new_list["size"] -=1 
        return info_eliminada
    
def remove_last(new_list: dict):
    if is_empty(new_list):
        raise Exception("Lista vacia")
    elif new_list["size"] == 1:
        info_eliminada = new_list["last"]["info"]
        new_list["first"] = None
        new_list["last"] = None
        new_list["size"] -= 1
        return info_eliminada
    else:
        penultimo = encontrar_posicion(new_list, size(new_list) - 2)
        info_eliminada = penultimo["next"]["info"]
        penultimo["next"] = None
        new_list["last"] = penultimo
        new_list["size"] -=1
        return info_eliminada
    
def insert_element(new_list: dict, pos: int, element):
    if is_empty(new_list) or pos == 0:
        return add_first(new_list, element)
    elif pos == size(new_list):
        return add_last(new_list, element)
    elif pos < 0 or pos >= size(new_list):
        raise Exception("Posicion fuera de rango")
    else:
        node = nd.new_single_node(element)
        posicion = encontrar_posicion(new_list, pos-1)
        hilo = posicion["next"]
        posicion["next"] = node
        node["next"] = hilo
        new_list["size"] += 1
        return new_list
    
def change_info(new_list: dict, pos: int, element):
    if is_empty(new_list):
        raise Exception("Lista vacia")
    elif pos < 0 or pos >= size(new_list):
            raise Exception("Posicion fuera de rango")
    elif pos == size(new_list)-1:
        new_list["last"]["info"] = element
        return new_list
    else:
        posicion = encontrar_posicion(new_list, pos)
        posicion["info"] = element
        return new_list
        
def exchange(new_list: dict, pos1: int, pos2: int):
    
    if is_empty(new_list):
        raise Exception("Lista vacia")
    elif pos1 < 0 or pos1 >= size(new_list) or pos2 < 0 or pos2 >= size(new_list):
        raise Exception("Posicion fuera de rango")
    else:
        posicion1 = encontrar_posicion(new_list, pos1)
        posicion2 = encontrar_posicion(new_list, pos2)
        info = posicion1["info"]
        posicion1["info"] = posicion2["info"]
        posicion2["info"] = info
        return new_list
    
def sub_list(source_list: dict, pos: int, num_elem: int):
    if num_elem < 0 or pos < 0 or pos > size(source_list) or (pos + num_elem) > size(source_list):
        raise Exception("Posicion fuera de rango")

    result = new_list()
    if num_elem == 0:
        return result

    actual = encontrar_posicion(source_list, pos)
    for _ in range(num_elem):
        add_last(result, actual["info"])
        actual = actual["next"]
    return result

def default_sort_criteria(element_1, element_2):

   is_sorted = False
   if float(element_1) < float(element_2):
      is_sorted = True
   return is_sorted

def selection_sort(my_list, sort_crit=default_sort_criteria):
    if is_empty(my_list) or size(my_list) <= 1:
        return my_list

    nodo_i = my_list["first"]

    while nodo_i is not None:
        nodo_min = nodo_i
        nodo_j = nodo_i["next"]

        while nodo_j is not None:
            if sort_crit(nodo_j["info"], nodo_min["info"]):
                nodo_min = nodo_j
            nodo_j = nodo_j["next"]

        if nodo_min != nodo_i:
            temp = nodo_i["info"]
            nodo_i["info"] = nodo_min["info"]
            nodo_min["info"] = temp

        nodo_i = nodo_i["next"]

    return my_list

def insertion_sort(my_list, sort_crit=default_sort_criteria):
    
    if is_empty(my_list) or size(my_list) <= 1:
        return my_list

    lista_ordenada = new_list()
    actual = my_list["first"]

    while actual is not None:
        siguiente = actual["next"]
        elem = actual["info"]

        if is_empty(lista_ordenada):
            add_first(lista_ordenada, elem)

        elif sort_crit(elem, lista_ordenada["first"]["info"]):
            add_first(lista_ordenada, elem)

        elif not sort_crit(elem, lista_ordenada["last"]["info"]):
            add_last(lista_ordenada, elem)

        else:
            nod_actual = lista_ordenada["first"]
            pos = 0

            while nod_actual["next"] is not None and not sort_crit(elem, nod_actual["next"]["info"]):
                nod_actual = nod_actual["next"]
                pos += 1

            insert_element(lista_ordenada, pos + 1, elem)

        actual = siguiente

    my_list["first"] = lista_ordenada["first"]
    my_list["last"] = lista_ordenada["last"]
    my_list["size"] = size(lista_ordenada)

    return my_list

def shell_sort(my_list, sort_crit=default_sort_criteria):
    
    n = size(my_list)
    if n <= 1:
        return my_list

    h = 1
    while h < n // 3:
        h = 3 * h + 1

    while h >= 1:
        for i in range(h, n):
            j = i
            while j >= h and sort_crit(get_element(my_list, j), get_element(my_list, j - h)):
                exchange(my_list, j, j - h)
                j -= h

        h = h // 3

    return my_list

def merge(lst, aux_lst, sort_criteria, lo, mid, hi):
    i = lo
    j = mid + 1

    for k in range(lo, hi + 1):
        if i > mid:
            elem_j = get_element(lst, j)
            change_info(aux_lst, k, elem_j)
            j += 1
        elif j > hi:
            elem_i = get_element(lst, i)
            change_info(aux_lst, k, elem_i)
            i += 1
        else:
            elem_i = get_element(lst, i)
            elem_j = get_element(lst, j)

            if sort_criteria(elem_j, elem_i):
                change_info(aux_lst, k, elem_j)
                j += 1
            else:
                change_info(aux_lst, k, elem_i)
                i += 1

    for k in range(lo, hi + 1):
        elem_aux = get_element(aux_lst, k)
        change_info(lst, k, elem_aux)


def merge_sort_recursive(lst, aux_lst, sort_criteria, lo, hi):
    if lo >= hi:
        return

    mid = lo + (hi - lo) // 2

    merge_sort_recursive(lst, aux_lst, sort_criteria, lo, mid)
    merge_sort_recursive(lst, aux_lst, sort_criteria, mid + 1, hi)
    merge(lst, aux_lst, sort_criteria, lo, mid, hi)


def merge_sort(lst, sort_criteria=default_sort_criteria):
    lst_size = size(lst)
    if lst_size > 1:
        aux_lst = sub_list(lst, 0, lst_size)
        merge_sort_recursive(lst, aux_lst, sort_criteria, 0, lst_size - 1)

    return lst

def dividir(lista, criterio_orden, limite_inferior, limite_superior):
    pivote = get_element(lista, limite_inferior)
    i = limite_inferior
    j = limite_superior + 1
    detener = False

    while not detener:
        i += 1
        while i <= limite_superior and criterio_orden(get_element(lista, i), pivote):
            i += 1

        j -= 1
        while criterio_orden(pivote, get_element(lista, j)):
            j -= 1

        if i >= j:
            detener = True
        else:
            exchange(lista, i, j)

    exchange(lista, limite_inferior, j)
    return j


def quick_sort_recursivo(lista, criterio_orden, limite_inferior, limite_superior):
    if limite_inferior >= limite_superior:
        return

    posicion_pivote = dividir(lista, criterio_orden, limite_inferior, limite_superior)
    quick_sort_recursivo(lista, criterio_orden, limite_inferior, posicion_pivote - 1)
    quick_sort_recursivo(lista, criterio_orden, posicion_pivote + 1, limite_superior)


def quick_sort(lista, criterio_orden=default_sort_criteria):
    if is_empty(lista) or size(lista) <= 1:
        return lista

    quick_sort_recursivo(lista, criterio_orden, 0, size(lista) - 1)
    return lista