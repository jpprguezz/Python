def run(data_path: str, target_word: str) -> list:
    with open(data_path) as f:
        SPECIAL_SYMBOLS = ".,:;()’¡!"
        matches = []
        for line_no, line in enumerate(f, start=1):
            words = line.split()
            pos = 0  # Posición actual en la línea

            for word in words:
                cleaned_word = word.strip(SPECIAL_SYMBOLS).lower()
                if cleaned_word == target_word:
                    column = pos + 1  # La posición real en la línea
                    matches.append((line_no, column))
                
                pos += len(word) + 1  # Mueve la posición para la siguiente palabra
        
 



                
    return matches


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
