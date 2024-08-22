# ******************
# LA PALABRA PERDIDA
# ******************


def run(text: str, target_word: str, replace_word: str) -> str:
    # TU CÓDIGO AQUÍ
    replacing_slicing = text.find(target_word)
    start = text[:replacing_slicing]
    end = text[replacing_slicing + len(target_word):]  # Sumamos la longitud de la target_word para saltar exactamente sobre la palabra que estamos reemplazando, de modo que podamos capturar correctamente el resto del texto a partir de donde termina la palabra original.
    mtext = start + replace_word + end
    return mtext


if __name__ == "__main__":
    run("This is a beautiful night on the Atlantic", "beautiful", "terrible")
