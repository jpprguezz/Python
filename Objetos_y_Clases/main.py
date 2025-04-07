from __future__ import annotations


# ♣ ◆ ❤ ♠

class Card:
    # Palos disponibles en la baraja
    SUITS = ['♣', '◆', '❤', '♠']

    # Valores de cartas válidos como strings
    STR_VALUES = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    # Mapeo de strings a valores numéricos
    STR_KEYS = {
        "A": 1, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
        "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13
    }

    def __init__(self, value: int | str, suit: str):
        """
        Constructor de la clase Card. Valida y guarda el valor y el palo de la carta.
        - value: puede ser un entero (1 a 13) o string ('A', 'J', 'Q', etc.).
        - suit: debe ser uno de los palos definidos en SUITS.
        """
        if isinstance(value, int): 
            if not 1 <= value <= 13:
                raise InvalidCardError(f'{repr(value)} is not a supported value')
            else:
                self.value = value
        else:
            if value not in Card.STR_VALUES:
                raise InvalidCardError(f'{repr(value)} is not a supported symbol')
            else:
                self.value = Card.STR_KEYS[value]

        if suit not in Card.SUITS:
            raise InvalidCardError(f'{repr(suit)} is not a supported suit')

        self.suit = suit

    @property
    def get_numeric_value(self) -> int:
        """
        Devuelve el valor numérico de la carta.
        El As (1) se considera como 14 para comparaciones.
        """
        return self.value if self.value != 1 else 14

    def __repr__(self):
        """
        Devuelve una representación visual de la carta usando los glifos del archivo externo.
        """
        glyphs = Card.get_glyphs(self.suit)
        return glyphs[self.value - 1]

    def __eq__(self, other: Card | object) -> bool:
        """
        Compara si dos cartas son iguales (mismo valor y mismo palo).
        """
        return self.value == other.value and self.suit == other.suit

    def __lt__(self, other: Card) -> bool:
        """
        Compara si esta carta es menor que otra (según el valor numérico).
        """
        return self.get_numeric_value < other.get_numeric_value

    def __gt__(self, other: Card) -> bool:
        """
        Compara si esta carta es mayor que otra (según el valor numérico).
        """
        return self.get_numeric_value > other.get_numeric_value

    def __add__(self, other: Card) -> Card:
        """
        Suma dos cartas.
        - Si la suma de valores excede 13, se reinicia a 1.
        - El palo resultante es el mismo si son iguales, o el de la carta de mayor valor.
        """
        max_card = max(self, other)
        min_card = min(self, other)

        if max_card.value + min_card.value > 13:
            new_card_value = 1
        else:
            new_card_value = max_card.value + min_card.value

        if self.suit == other.suit:
            new_card_suit = self.suit
        else:
            new_card_suit = max_card.suit

        return Card(new_card_value, new_card_suit)

    @classmethod
    def get_available_suits(cls) -> str:
        """
        Devuelve todos los palos disponibles como una sola cadena.
        """
        return ''.join(Card.SUITS)

    @classmethod    
    def get_cards_by_suit(cls, suit: str):
        """
        Generador que devuelve los símbolos de las cartas disponibles para un palo.
        """
        for i in cls.get_glyphs(suit):
            yield i

    @classmethod
    def get_glyphs(cls, suit):
        """
        Lee el archivo de glifos y devuelve los símbolos visuales para el palo indicado.
        El archivo debe tener una línea por palo en el formato: ♠:🂡,🂢,🂣,...
        """
        with open('data/glyphs.dat', 'r', encoding='utf-8') as f:
            for line in f:
                if line[0] == suit:
                    splitted_glyphs = line.strip().replace(':', ',').split(',')
                    splitted_glyphs.pop(0)  # quitar el símbolo del palo
                    return splitted_glyphs


class InvalidCardError(Exception):
    """
    Excepción personalizada para errores en la creación de cartas.
    """
    def __init__(self, message: str = 'Invalid card'):
        if message != 'Invalid card':
            self.message = f'Invalid card: {message}'
        else:
            self.message = message
        super().__init__(self.message)
