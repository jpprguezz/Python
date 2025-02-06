def run(d1: dict, d2: dict) -> dict:
    merged = {}  # Creamos un diccionario vacío para guardar los nuevos elementos
    for unified_d in d1, d2:  # Unificamos los dos diccionarios con este for, que crea una tupla con ambos diccionarios. Estos van iterandose siendo la primera iteracion d1, y la segunda, d2
        for key, value in unified_d.items(): # Iteramos sobre clave y valor del diccionario unificado
            merged[key] = value # Añadimos los elementos uno a uno. En caso de que ya estuviera la clave de un elemento, el valor de dicho elemento se reemplaza por el valor del nuevo elemento


    return merged


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
