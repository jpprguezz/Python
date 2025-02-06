def run(imoves: str) -> dict:
    inventory = {}
    imoves_splitted = imoves.split(',')
    for move in imoves_splitted:
        move_position = imoves_splitted.index(move)
        article = imoves_splitted[move_position][0]
        inventory_modification = imoves_splitted[move_position][1:]
        for modification in inventory_modification:
            modifications = 0


    return inventory


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
