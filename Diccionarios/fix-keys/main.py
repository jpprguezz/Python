def run(items: dict) -> dict:
    fitems = {}  # Creamos el diccionario desde cero
    for key, value in items.items():  # Hacemos un for para sacar tanto las claves como los valores
        key_without_spaces = ''  # Creamos un string vacío para guardar las letras del string original
        for char in key:  # Hacemos un for para recorrer las claves, para poder añadir las letras al string vacío
            if char != ' ':  # Si el caracter no es un espacio, es una letra
                key_without_spaces += char # Por lo que se añade al string vacío
        fitems[key_without_spaces] = value  # Añadimos dichas entradas al diccionario
        
    return fitems


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
