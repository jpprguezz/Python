def run(cinfo: str) -> dict:
    cities = {}  # Creamos el diccionario desde cero
    cinfo_without_semicolons = cinfo.split(';')  # Eliminamos los ; de en medio del texto
    for data in cinfo_without_semicolons:  # Creamos un bucle que recorra el texto formateado, y con el cual añadiremos info al diccionario
        data_splitted = data.split(':')  # Volvemos a splitear el dato que se recorre para separar ciudad y población
        city = data_splitted[0] # La ciudad, resultante del split anterior
        population_without_bars = int(data_splitted[1].replace('_', ''))  # Hacemos un replace de las _ por no espacios, para tener un string todo junto, y lo convertimos a entero
        cities[city] = population_without_bars  # Añadimos la entrada al diccionario

    return cities


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
