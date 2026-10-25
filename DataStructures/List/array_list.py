def new_list():
    newlist = {
        "elements": [],
        "size": 0,
    }
    return newlist

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    return my_list["elements"][0]

def add_first(my_list, element):
    my_list["elements"].insert(0,element)
    my_list["size"] += 1
    return my_list
      
def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list
        
def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else:
        return False

def last_element(my_list):
    if is_empty(my_list):
        raise Exception("La lista está vacía")
    else:
        return my_list["elements"][-1]
    
def remove_first(my_list):
    if is_empty(my_list):
        raise Exception("La lista está vacía")
    else:
        element = my_list["elements"].pop(0)
        my_list["size"] -= 1
        return element
    
def remove_last(my_list):
    if is_empty(my_list):
        raise Exception("La lista está vacía")
    element = my_list["elements"].pop()
    my_list["size"] -= 1
    return element

def insert_element(my_list, element, position):
    if position < 0 or position > size(my_list):
        raise Exception("Posición fuera de rango")
    elif is_empty(my_list) or position == 0:
            return add_first(my_list, element)
    elif position == size(my_list):
        return add_last(my_list, element)
    else:
        my_list["elements"].insert(position, element)
        my_list["size"] += 1
        return my_list

def delete_element(my_list, position):
    if position < 0 or position >= size(my_list):
        raise Exception("Posición fuera de rango")
    elif is_empty(my_list):
            raise Exception("Lista vacia")
    else:
        element = my_list["elements"].pop(position)
        my_list["size"] -= 1
        return element

def change_info(my_list, position, new_info):
    if position < 0 or position >= size(my_list):
        raise Exception("Posición fuera de rango")
    elif is_empty(my_list):
        raise Exception("Lista vacia")
    else:
        my_list["elements"][position] = new_info
        return my_list
    
def exchange(my_list, position1, position2):
    if position1 < 0 or position1 >= size(my_list) or position2 < 0 or position2 >= size(my_list):
        raise Exception("Posición fuera de rango")
    elif is_empty(my_list):
            raise Exception("Lista vacia")
    else:
        temp = my_list["elements"][position1]
        my_list["elements"][position1] = my_list["elements"][position2]
        my_list["elements"][position2] = temp
        return my_list
    
def sub_list(my_list, position, num_elem):
    if position < 0 or position >= size(my_list) or (position + num_elem) > size(my_list):
        raise Exception("Rango de sub lista invalido")
    elif is_empty(my_list):
            raise Exception("Lista vacia")
    else:
        new_sub = new_list()
        new_sub["elements"] = my_list["elements"][position : (position + num_elem)]
        new_sub["size"] = num_elem
        return new_sub

def default_sort_criteria(element_1, element_2):

   is_sorted = False
   if float(element_1) < float(element_2):
      is_sorted = True
   return is_sorted

def selection_sort(my_list,sort_crit):
    if is_empty(my_list) or size(my_list) <= 1:
            return my_list
    n = size(my_list)
    for i in range(n):
        min_pos = i
        for j in range(i + 1, n):
            if sort_crit(get_element(my_list, j), get_element(my_list, min_pos)):
                min_pos = j

        if min_pos != i:
            exchange(my_list, i, min_pos)

    return my_list


def insertion_sort(my_list, sort_crit):
    if is_empty(my_list) or size(my_list) <= 1:
            return my_list
    else:
        for i in range(size(my_list)):
            j = i
            while j > 0 and sort_crit(get_element(my_list,j),get_element(my_list,j-1)):
                exchange(my_list,j,j-1)
                j-=1
    return my_list


def shell_sort(my_list, sort_crit):
    if is_empty(my_list) or size(my_list) <= 1:
            return my_list
    n = size(my_list)
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