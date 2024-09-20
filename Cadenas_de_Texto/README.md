# Cadenas de texto (Strings)

Los strings son secuencias de caracteres, que se pueden almacenar

Para creaar un string simplemente debemos encasillar los que queramos entre ' ', de esta manera:

```python
>>> 'Hola me "username" es Pepe222'

'Hola me "username" es Pepe222'
```

Como se ve en el ejemplo, se puede añadir de todo en medio de un string, incluyendo comillas y números

En el caso de que quisieramos colocar comillas simples dentro, deberiamos cambiar las comillas de fuera por unas dobles

```python
>>> "Hola 'Pepe222'"

"Hola 'Pepe222'"
```

Hay otra forma más de crear strings, y esta es con comillas triples. este tipo de strings normalmente se utiliza para cadenas multilineas, como por ejemplo, la documentación de código.

```python
>>> master_of_puppets = """Master of Puppets es una canción de la banda de trash metal Metallica de su album Master of Puppets de 1986""""
```

Y al igual que se pueden crear string con contenido, también se pueden hacer strings completamente vacios de esta sencilla manera:

```python
>>> ''

''
```

Gracias a la función str(), podemos convertir otros tipos de datos a strings:

```python
>>> str(True)
'True'

>>> str(100)
'100'
```

En el caso de que lo que quisieramos convertir es un string a cualqueir otro tipo, simplemente debemos usar las funciones ya vistas en anteriores temas:

```python
>>> bool('True')
True

>>> int('100')
100
```

También hay que destacar que la funcion int admite la base del numero correspondiente, por lo cual podemos pasarle un número cualquiera como string (en este caso, lo pasamos en hexadecimal) y podemos pasarlos a su valor entero:

```python
>>> int('FF', 16)

255
```

En Python se puede escapar el significado de algunos caracteres para conseguir resultados diferentes. Si escribimos \ en un string antes del caracter a escapar, podemos otorgar otro significado.

Porbablemente la secuencia de salto de linea (\n) es la mñas conocida de todas, aunque se pueden realizar muchas otras, que podremos ver más adelante, aunque vamos a ver unas pocas:

- Salto de línea

```python
>>> alphabet = 'a\nb\nc\n'
>>> print(alphabet)

a
b
c
```

- Tabulador

```python
>>> msg = 'Saludo = \tHola'
>>> print(msg)

Saludo =    Hola
```

- Comilla simple

```python
>>> msg = 'Este texto \'hola\' esta entre comillas simples'
>>> print(msg)

Este texto 'hola' esta entre comillas simples'
```

- Barra invertida

```python
>>> msg = 'Este texto \\ hola \\ esta barras invertidas'
>>> print(msg)

Este texto \ hola \ esta barras invertidas
```

Pero: ¿que pasaría si quisieramos que estos caracteres especiales pierdan el significado que poseen para poder usarlos de otra manera?. Para ello simplemente tendríamos que usar el raw data en el texto que queramos modificar. Este es representado con la letra r. Este metodo es muy usado para las llamadas expresiones regulares.

```python
>>> text = 'abc\nABC'

>>> print(text)
abc
ABC

>>> text = r'abc\nABC'

>>> print(text) # debería hacer el salto de linea pero al incluir el r antes del texto entre comillas simples, imprime el texto literal
abc\nABC
```

Ahora veremos algunas cosas más sobre la función print(), ya que admite muchos más parámetros:

```python
>> msg1 = 'Hola'
>> msg2 = 'Amigos'

>>> print(msg1, msg2) # separamos las dos variables entre ellas por comas, por lo cual se imprime el contenido de ambas
Hola Amigos

>>> print(msg1, msg2, sep = '|') # como vimos antes, el separador por defecto es un espacio, por lo cual aquí lo cambiamos por una barra vertical
Hola|Amigos

>>> print(msg1, end = '!!') # aqui cambiamos el valor final por defecto, por dos exclamaciones
Hola!!
```

Pyhton nos permite pasar el pasar datos a traves de teclado. Al escribir los que queramos, el programa leera dicha cosa escrita. Para ello usamos la función input(), la cual se usa así:

```python
>>> name = input('Introduce tu nombre: ')
Introduce tu nombre: José

>>> name
José

>>> type(name)
str
```

Debemos tener en cuenta que input() siempre nos devuelve un string. Por ello muchas veces deberemos hacer conversión explicita.

Aparte en Python, se pueden hacer operaciones con las propias strings:

- Se pueden combinar strings con +:

```python
>>> msg1 = 'Hola'
>>> msg2 = 'que tal'

>>> msg1 + msg2
'Holaque tal'

>>> msg1 + ',' + msg2 # incluimos una coma
'Hola, que tal'
```

- Se pueden repetir strings:

```python
>>> msg1 = 'Hola'

>>> msg1 * 4
'HolaHolaHolaHola'
```

- Una parte importante de las operaciones con string es el indice. Tenemos que tener en cuenta que los strings estan indexados, es decir que cada caracter dentro de la cadena de texto tiene su propio índice, el cual indicamos entre corchetes para acceder a el. Debemos tener en cuenta que el primer caracter siempre va a tener el indice 0 y el caracter final sera una unidad menos de la longituf del string

```python
>>> msg1 = 'Hola, Familia'

>>> msg1[0]
'H'

>>> msg1[6]
'F'

>>> msg1[2]
'l'

>>> msg1[4]
','
```

Debemos destacar la existencia de indices positivos, pero también de indices negativos. A ellos se acceden teniendo en cuenta que el ultimo carácter del string es -1 y a partir de ese, hacia atrás. Aquí una imagen para mayor claridad:

![alt text](src/image.png)

Los strings pueden ser troceados para extraer ciertos trozos del mismo. Para ello se utiilizan estas aproximaciones:

- [:]
  Extrae todo el string (es similar a una copia).

```python
>>> msg1 = 'Hola que tal amigos'

>>> proverb[:]
'Hola que tal amigos'
```

- [start:]
  Extrae desde el principio (start) al final de la cadena.

```python
>>> msg1[4:]
' que tal amigos'
```

- [:end]
  Extrae desde el comienzo hasta el final (end) menos 1.

```python
>>> msg1[:6]
'Hola q'
```

- [start:end]
  Extrae desde el inicio al final menos 1.

```python
>>> msg1[7:15]
'e tal am'
```

- [start:end:step]
  Extrae desde el inicio al final, menos 1, indicandole los saltos de tamaño en el string (step).

```python
>>> msg1[5:11:2]
'qet'
```

Debemos tener en cuenta que el troceado siempre llega a un unidad menos del indice final real del string. En cambio, el comienzo siempre coincide con lo que colocamos

La longitud de un string puede ser comprobada, gracuas a la funcion len(), la cual da la posibilidad de medir practicamente todos los tipos y estructuras en Python.

```python
>>> msg1 = 'Mediremos este string'

>>> len(msg1)
21

>>> empty_msg = ''

>>> len(empty_msg)
0
```

Una importante parte de los string en Python, es el poder comprobar la existencia de subcadenas dentro de la cadena principal que queramos analizar. Para ellos tenemos el operador in. Este operador nos devuelve un booleano como resultado al ejecutarlo.

```python
>>> msg1 = 'Este es un texto de ejemplo'

>>> 'Este' in msg1
True

>>> 'texto' in msg1
True

>>> 'hola' in msg1
False
```

Hay que tener en cuenta que si quisieramos descubrir si una subcadena no esta en una cadena de texto, deberiamos hacer la siguiente pregunta pitónica:

```python
first_three_abecedary_letters = 'ABC'

>>> 'D' not in first_three_abecedary_letters
True
```

Debemos tener en cuenta que a la hora de leer cualquier informacion, lo más probable es que esta posea caracteres de relleno tanto al comienzo como al final de la cadena de texto. Para poder suprimir estos caracteres, podemos utilizar la función strip(), la cual elimina los caracteres iniciales y finales del string.

Existen variantes de esta funcion, la cual puede ser aplicada solo al comienzo o solo al final del string.

```python
>>> serial_number = '\n\t   \n 48374983274832    \n\n\t   \t   \n'

>>> serial_number.strip()
'48374983274832'
```

Hay que tener en cuenta que si no inidicamos a la función strip(), elimina por defecto cualquier combinación de espacios en blanco, \n y \t. Para ello se utilizan las siguientes dios funciones:

- lstrip() para limpiar por el comienzo (es decir, por la izquierda)

```python
>>> serial_number.lstrip()
'48374983274832    \n\n\t   \t   \n'
```

- rstip() para limpiar por el final (es decir, por la derecha)

```python
>>> serial_number.rstrip()
'\n\t   \n 48374983274832'
```

Y como dijimos antes, se puede especificar lo que quieres que se quiera borrar:

```python
>>> serial_number.strip('\n')
'\t   \n 48374983274832    \n\n\t   \t   '
```

En Python se puede hacer, entre muchas cosas, busquedas en los strings.

Pongames de ejemplo, el estribillo de la primera intro de la pirmera temporada de Pokémon:

```python
lyrics = """Pokémon (gotta catch 'em all), it's you and me
I know it's my destiny (Pokémon)
Oh, you're my best friend
In a world we must defend
Pokémon (gotta catch 'em all), a heart so true
Our courage will pull us through
You teach me and I'll teach you
Pokémon (gotta catch 'em all)
Gotta catch 'em all, yeah"""
```

A partir de este string, podemos:

- Comprobar si un string comienza o termina por alguna subcadena:

```python
>>> lyrics.startwith('Pokémon')
True

>>> lyrics.endwith('oh')
False
```

- Encontrar la primera ocurrencia de alguna subcadena:

```python
>>> lyrics.find('gotta')
9

>>> lyrics.index('friend')
99
```

Debemos destacar que las funciones index() y find() devuelven el índice de la primera ocurrencia de la subcadena que le pasemos a función, pero cada una de estas funciones tiene un comportamiento diferente cuando el elemento pasado no existe en el string:

```python
>>> lyrics.find('hola')
-1

>>> lyrics.index('hola')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
```

- Y por último contabilizar el número de veces que aparece uan subcadena:

```python
>>> lyrics.count('Pokémon')
4
```

Una parte importa de las cadenas de texto, es la llamada función replace(). Indicandole a esta función la subcadena que queremos reemplazar, el reemplazo, y las instancias en las que se debe reemplazar, podemos hacer que esta función sea efectiva. En el caso de que no indiquemos las instancias, el replace se realizará en todos los casos que se encuentren

```python
>>> proverb = 'Quien mal anda mal acaba'

>>> proverb.replace('mal', 'bien')
'Quien bien anda bien acaba'

proverb.replace('mal', 'bien', 1)  # sólo 1 reemplazo
'Quien bien anda mal acaba'
```

A su vez, Python nos permite realizar cambios en los caracteres de una cadena de texto, pudiendolos cambiar a mayusculas y minúsculas:

```python
>>> text = 'hombre precavido, vale por dos'

>>> text.capitalize()
'Hombre precavido, vale por dos'

>>> text.title()
'Hombre Precavido, Vale Por Dos'

>>> text.upper()
'HOMBRE PRECAVIDO, VALE POR DOS'

>>> text.lower()
'hombre precavido, vale por dos'

>>> text.swapcase()
'HOMBRE PRECAVIDO, VALE POR DOS'
```

Debemos destacar una serie de funciones importantes, las cuales nos permite identificar el tipo de caracteres que poseemos en una cadena de texto:

```python
# Identificar si todos los caracteres son alfanuméricos, es decir, letras (a-z) y números (0-9)
>>> 'Kangashkan'.isalnum()
True

>>> 'Porygon-2'.isalnum()
False

# Identificar si todos son números
>>> '555'.isnumeric()
True

>>> '5-5-5'.isnumeric()
False

# Identificar si son todos letras
>>> 'abc'.isalpha()
True

>>> 'a-b-c'.isalpha()
False

# Identificar si hay mayúsculas/minúsculas

>>> 'HELLO'.isupper()
True

>>> 'hello'.islower()
True

>>> 'Hello World'.istitle()
True
```

Ahora veremos el como hacer interpolación de strings. En este contexto, esto significa que vamos a ver el como sustituir una variable por una cadena de texto.

Primero veremos el f-string, que es la forma más común para poder hacer intrerpolación de strings. Para hacerlo en Python, simplemente debemos antes de la primera comilla del string, una "f" e incluir "{ }" cada vez que deseemos interpiolar alguna expresión. Veamoslo mejor con un ejemplo.

```python
>>> name = 'Fumito Ueda'
>>> date = '2005'
>>> game = 'Shadow of the Colosus'
>>> console = 'PS2'

>>> f'Mi nombre es {name} y soy el principal creador de {game} que salió en {console}'
'Mi nombre es Fumito Ueda y soy el principal creador de Shadow of the Colosus que salió en PS2'
```

Pero, ¿y si queremos colocar llaves dentro de la interpolación?. Pues es tan sencillo como duplicar las llaves. Por ejemplo:

```python
>>> x = 10

>>> f'{{x = {x}}}'
```

También el f-string nos permite el poder cambiar diversas opciones de formateado (ancho de texto, numero de decimales, etc.) como se ve en estos ejemplos:

```python
# Dando formato a valores enteros
>>> pokemon_1st_gen = 151

>>> f'{pokemon_1st_gen:10d}'
'       151'

>>> f'{pokemon_1st_gen:010d}'
'0000000151'


# Dando formato a valores flotantes
>>> PI = 3.14159265

>>> f'{PI:f}'  # Se colocan 6 decimales por defecto
'3.141593'

>>> f'{PI:12f}'
'    3.141593'

>>> f'{PI:07.2f}'
'0003.14'
```

En estos dos primeros la f se utiliza haciendo referencia a flotante

```python
# Dando formato a cadenas de texto
>>> text1 = 'hello'
>>> text2 = 'my'
>>> text3 = 'friend'

>>> f'({text1:<9s})({text2:^13})({text3:>9s})'
'(hello    )(     my      )(   friend)'

>>> f'({text1:.<9s})({text2:^13})({text3:.>9s})'
'(hello....)(     my      )(...friend)'
```

En este ultimo se coloca la s haciendo referencia a string

```python
# Pasar valores enteros a otras bases
>>> value = 987

>>> f'{value:b}' # Binario
'1111011011'

>>> f'{value:o}' # Octal
'1733'

>>> f'{value:x}' # Hexadecimal
'3db'
```

Aqui simplemente se colocan los prefijos de las bases a las que se quiere pasar el valor que tenemos

Ahora vamos a pasar a hablar sobre algunos de los modos que podemos encontrar en Python:

- Modo "debug"

A partir de la version 3.8, Python permite que el nombre de la variable, pueda mostrarse/imprimirse, con simplemente añadir un "=" al lado del nombre de la variable.

```python
>>> serie = 'Hunter X Hunter (2011)'
>>> imdb_rating = 9.0
>>> num_seasons = 6

>>> f'{serie=}'
"serie='Hunter X Hunter (2011)'"
```
