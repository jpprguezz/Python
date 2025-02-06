def run(text: str) -> dict:
    counter = {}  # Se crea el diccionario vacio
    for letter in text:  # Se recorre la palabra
        if letter in counter:  # Si se ha entrado por este if, significa que la letra ya estaba en el diccionario, por lo que se le agrega una ocurrencia más a dicha letra
            counter[letter] += 1
        else: # Si no, se crea un apartado en el diccionario para la nueva letra, a la que se le agrega una ocurrencia
            counter[letter] = 1


    return counter  


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
