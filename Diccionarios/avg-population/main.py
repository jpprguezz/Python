def run(pdata: dict) -> dict:
    avg_data = {}  # Creamos el diccionario  vacío para guardar los valores
    total_population = sum(pdata.values())  # Sumamos todas las poblaciones
    for city, population in pdata.items():  # Creamos un for para recorrer los elementos del diccionarios
        avg_calc = (population / total_population) * 100  # Hacemos el calculo del zip
        avg_data[city] = round(avg_calc, 3)  # Añadimos los datos al diccionario, redondeando la población a tres digitos


    return avg_data


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
