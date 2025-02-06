def run(items: list) -> dict:
    unpack_items = {}  # Creamos el diccionario desde cero
    for item in items: # Recorremos el grupo de listas
        key = item[0] # Asignamos como key, el primer elemento de la sublista que recorremos
        value = item[1:]  # Asignamos como value, el resto de elementos
        unpack_items[key] = value  # Agregamos los valores al diccionario
    return unpack_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
