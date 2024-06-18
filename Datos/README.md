# Datos

Si bien los programas que vemos son un simple conjunto de código y datos, pero a nivel de memoria la cosa esta hecha de secuencias de bits. Depende del lenguaje que usemos, la interpretacion de estos bits variará . Cada trozo de memoria contiene un objetoo y cada objeto posee

- Un tipo de dato que se almacena
- Un ID unico
- Un valor relacionado con su tipo

Los tipos de datos en Python son:

| Nombre    | Tipo     | Ejemplos                                 |
|-----------|----------|------------------------------------------|
| Booleano  | bool     | True, False                              |
| Entero    | int      | 21, 34500, 34_500                        |
| Flotante  | float    | 3.14, 1.5e3                              |
| Complejo  | complex  | 2j, 3 + 5j                               |
| Cadena    | str      | 'tfn', '''tenerife - islas canarias'''   |
| Tupla     | tuple    | (1, 3, 5)                                |
| Lista     | list     | ['Chrome', 'Firefox']                    |
| Conjunto  | set      | set([2, 4, 6])                           |
| Diccionario | dict   | {'Chrome': 'v79', 'Firefox': 'v71'}      |



En python existen las variables. Estas son importantes y ayudan a definir un nombre para cualquier valor en memoria que queramos usar en nuestro código:
```python
numero_uno = 1
```

Las variables solo pueden contener estos criterios:
- Letras minusculas y mayúsculas
- Digitos
- Guines bajos (_)

Además, deben empezar por una letra siempre y no pueden llamarse como cualqueir palabra reservada de python. Para este ultimo paso, podemos usar el comando `help(keywords)` para obtener todas las palabras reservadas. También es una buena practica escribirlas en inglés para hacer que nuestro código se vuelva algo internacional.

Entre las variables hay un caso especial el cual es el de las llamadas constantes. Es un tipo de varible que no cambia su valor a lo largo de todo nuestro codigo. En este caso, se escriben con mayusculas, de esta manera:
```python
LIGHT_SPEED = 300000
```

Dependiendo de lo que estemos usando, el nombre de nuestras variables puede cambiar, como podemos ver aqui abajo:

```python
- Nombres para variables --> Ej: article
- Verbos para funciones --> Ej: get_article()
- Adjetivos para booleano --> Ej: available
```

Como hemos visto antes, tanto en variables como en constantes, tenemos en común el uso de "=". Esta es la forma en la que le dices a Python que el nombre que aparece a la izquiera, se le asigna el valor de la derecha

```python
nombre_variable = 'variable'
numero_de_personas = 100
```
También tenemos la opcion de asginar de forma múltiple un valor a muchas variables. En el caso de abajo, hemos asignados a tres variables el valor 1:

```sql
one = uno = eins = 1
```

En Python tenemos la posibilidad de poder asignarle a una variable, otra variable como valor:

```python
hola = 'hola'
saludo_comun = hola
```

Pero, ¿que pasa si quiero ver el valor de una variable?. Para eso tenemos dos maneras:

```python
print(nombre_variable) --> Imprimre el valor de la variable


hola --> Llamas directamente a la variable (solo disponible en par a el interprete de Python)
```

También podemos conocer el tipo de la variable o de cualquier valor:

```python
type(19)
int

type(hola)
str
```

"Las variables son nombres, no lugares". Esta frase hace referencia a que cuando nostros definimos un valor para una variable, lo que hacemos es apuntar el nombre hacia algun lugar de memoria. He aqui un ejemplo:

```python
a = 6
b = a
id(a)
140736716028504
id(b)
140736716028504
```

En cambio, en el caso de que los valores de cada variable fueran diferentes, ahi si cambia el lugar de memoria:

```python
a = 5
b = 90
id(a)
140736716028472
id(b)
140736716031192
```

Por último, veremos brevemente las funciones built-in, las cuales son funciones incoporadas desde un inicio en Python:

| `abs()`        | `delattr()`     | `hash()`        | `memoryview()` | `set()`          |
|----------------|-----------------|-----------------|----------------|------------------|
| `all()`        | `dict()`        | `help()`        | `min()`        | `setattr()`      |
| `any()`        | `dir()`         | `hex()`         | `next()`       | `slice()`        |
| `ascii()`      | `divmod()`      | `id()`          | `object()`     | `sorted()`       |
| `bin()`        | `enumerate()`   | `input()`       | `oct()`        | `staticmethod()` |
| `bool()`       | `eval()`        | `int()`         | `open()`       | `str()`          |
| `breakpoint()` | `exec()`        | `isinstance()`  | `ord()`        | `sum()`          |
| `bytearray()`  | `filter()`      | `issubclass()`  | `pow()`        | `super()`        |
| `bytes()`      | `float()`       | `iter()`        | `print()`      | `tuple()`        |
| `callable()`   | `format()`      | `len()`         | `property()`   | `type()`         |
| `chr()`        | `frozenset()`   | `list()`        | `range()`      | `vars()`         |
| `classmethod()`| `getattr()`     | `locals()`      | `repr()`       | `zip()`          |
| `compile()`    | `globals()`     | `map()`         | `reversed()`   | `__import__()`   |
| `complex()`    | `hasattr()`     | `max()`         | `round()`      |                  |
