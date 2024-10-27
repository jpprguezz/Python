# Condicionales

### Comentarios
Aunque esto no tenga nada que ver con los condicionales, es importante saber el como hacer comentarios en tu código. Se hacen de manera que el código ignore completamente el comentario y este solo sirva para dar información, y para ello se coloca un # delante de lo que queramos comentar para que así quede ignorado.

```python
# Formula del area de un círculo

area = PI * (radius ** 2)
```

### Ancho del código

Debido a que antiguamente las pantallas no eran tan grandes, las lineas de Python estaban limitadas con el fin de acumular 80 caracteres. Sin embargo, como hoy en día las pantallas son mas grandes, ya esta práctica no se efectua. Aunque igualmente, hayq gente que prefiere seguir esta métrica a día de hoy.

Por ello si queremos romper una línea, en mi caso usaré esta opcion (aunque existe también la "\" como opción para esto)

En mi caso, he decidido usar "( )" para ello:

```python
from_1_to_10 = 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10

from_1_to_10 = 1,
               2,
               3,
               4,
               5,
               6,
               7,
               8,
               9,
               10,
```

### El if

La sentencia en Python (al igual que en muchos otros lenguajes) para hacer condicionales, es el llamado if. Esta se construye colocando un comparador entre el pirmer y segundo valor a comparar y se termina con dos puntos.

```python
team_players = 11

if team_players < 11:
    print('No se puede jugar, no hay suficientes jugadores')
```

Pero, ¿que pasaría si realmente si hubieran suficientes jugadores para poder jugar al fútbol?, el código anterior no podría solucionar ese problema. Por ello le añadiremos el llamado else, el cual sirve para controlar los casos en los que si la primera opción no se cumple, se cumpla la segunda.

```python
team_players = 11

if team_players < 11:
    print('No se puede jugar, no hay suficientes jugadores')
else:
    print('Suficientes jugadores, podeis jugar')
```

Incluso podríamos tener las llamadas condiciones anidadas, que no son más que condiciones dentro de condiciones.

```python
team_players = 15

if team_players < 20:  # Máximo de jugadores en un equipo de fútbol
    if team players < 11:
        print('No se puede jugar, no hay suficientes jugadores')
    else:
        print('Suficientes jugadores, podeis jugar')
else:
    if team_players > 20:
        print('No se puede jugar, hay demasiados jugadores')
    else:
        print('Teneis justo el límite máximo de jugadores, podeis jugar')
```

En los condicionales de Python, podemos combinar las dos expresiones que hemos visto anteriormente (else e if) y usarlas en conjunto en una nueva expresión llamada elif. Se utiliza cuando aparecen estas dos expresiones seguidamente.

```python
if team_players < 20:  # Máximo de jugadores en un equipo de fútbol
    if team players < 11:
        print('No se puede jugar, no hay suficientes jugadores')
    else:
        print('Suficientes jugadores, podeis jugar')
elif team_players > 20:
    print('No se puede jugar, hay demasiados jugadores')
 else:
    print('Teneis justo el límite máximo de jugadores, podeis jugar')
```

### Asignaciones condicionales

Las asignaciones condicionales son un metodo por el cuál podemos escribir condiciones en una simple línea:

Imaginemos que tenemos este código con un condicional:

```python
caterpie_appearance_rate = 255

if caterpie_appearance_rate < 255:
    cartepies_in_zone = 'Low'
else:
    cartepies_in_zone = 'High'
```

Pues con la asignación condicional, este código se escribiría así de facil:

```python
cartepies_in_zone = 'Low' if caterpie_appearance_rate < 255 else 'High'
```

### Operadores de comparación en condicionales

En Python, las condiciones van seguidas, como hemos visto en los anteriores códigos, por operadores. Estos lo que hacen es expresar el motivo de un condicional. Vamos a verlos:

| Operador           | Símbolo |
|--------------------|---------|
| Igualdad           | ==      |
| Desigualdad        | !=      |
| Menor que          | <       |
| Menor o igual que  | <=      |
| Mayor que          | >       |
| Mayor o igual que  | >=      |

Ahora pongamos algún ejemplo práctico:

```python
bug_pokemon = 10
flying_pokemon = 14

bug_type > flying_type
True

fling_type <= bug_type
False
```

Una acción curiosa que podemos hacer con los operadores, es comprobar si un valor esta entre otros dos que seleccionemos, esto nos será muy útil en ciertas ocasiones.

```python
5 <= 3 <= 7
```

### Operadores lógicos en condicionales

Aparte de los operadores de comparación que vimos anteriormente, también existen los llamados operadores lógicos. Estos operadores sirven para aumentar la complicidad de nuestras condiciones. Estas se hacen con los operadores: `and`, `or` y `not`. Estos pues se traducen de forma literal en español como `y`, `o` y `no` respectivamente.

Estos operadores poseen un tipo de jerarquía para poder funcionar entre ellas, en las cuales los resultados se dan en True y False, veamoslas. Cabe destacar que estas expresiones, en el momento en el que usamos varias, es una buena práctica ponerlas entre parentesis para que se puedan leer mejor:


- Tabla de AND 

| A     | B     | A and B |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |


- Tabla de OR

| A     | B     | A or B  |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | True    |
| False | True  | True    |
| False | False | False   |


- Tabla de NOT

| A     | not A |
|-------|-------|
| True  | False |
| False | True  |


### Cortocircuito lógico

Debemos saber que las expresiones lógicas anteriormente vistas puede que no se ejecuten de forma completa si se dan ciertos factores. A eso lo llamamos cortocircuito. Pongamos el ejemplo de que para hacer pasta con tomate necesitamos, valga la redundancia, pasta y tomate. Pero para hacer un plato solo para una persona necesitamos al menos 100 gramos de pasta y al menos 50 gramos de tomate:

- And

```python
pasta = 20
tomatoes = 60

pasta > 100 and tomatoes > 50
False
```

Al estar en un and, y la pasta no superar los 100 gramos, se produce el cortocircuito, por lo cual no se evalua el resto de la condicion porque se sabe que dará como resultado False.


- Or

Ahora planteemos que para hacer pasta con tomate para dos personas, se necesitan al menos 200 gramos de pasta y al menos 100 de tomate:

```python
pasta = 210
tomatoes = 40

pasta > 200 or tomatoes > 100:
True
```

En este caso al estar en un or, y cumplirse la condicion de la pasta, el resto de la condición no se evalua porque ya se sabe que el resultado será True.


# Booleanos en condicionales

Para empezar a ver los boolenaos con los condicionales, comentaremos sobre como utilizar la veracidad. Habiendo visto las comparaciones anteriormente, podríamos pensar que la forma de indicar, por ejemplo, si algo es verdadero, sería así:

```python
pokemon_is_shiny = True

if pokemon_is_shiny == True:
    print('Atapar Pokémon')
else:
    print('Seguir buscando')

Atrapar Pokemon
```

Aunque esto funcione, así no se debe hacer. Deberíamos hacerlo de la siguiente manera:

```python
pokemon_is_shiny = True

if pokemon_is_shiny:
    print('Atapar Pokémon')
else:
   print('Seguir buscando')

Atrapar Pokémon
```

Ahora bien, ¿que pasaría si el valor de la variable fuera False?:

```python
pokemon_is_shiny = False

if not pokemon_is_shiny:
    print('Atapar Pokémon')
else:
   print('Seguir buscando')

Seguir  buscando
```

### Valor nulo

También existe el valor None, el cual como su nombre indica, es un valor totalmente nulo:

```python
pikachu_in_zone = None

if pikachu_in_zone:
    print('Puedes atrapar Pikachus en esta zona')
else:
    print('No se si hay en esta zona Pikachus')  # La frase de este print se debe a que el valor puede ser True, False, None o cualquier otro                                            
```

Si quisieramos preguntar si el valor no es nulo, lo podríamos escribirír asi:

```python
pikachu_rate = 2000
if pikachu_rate is not None:
    print(f'The Pikachu rate is {pikachu_rate}')
```

Ahora plantearemos la siguiente duda: si tenemos el operador ==, ¿por qué utilizar el is?. Para resumir, el is comprueba solo los ids de dos objetos iguales, pero el == puede tener muchas mas acciones diferentes. Esto hace que la ejecución sea más rapida y se eviten "falsos positivos" de forma erronea.

Al usar Python, None es uno de los muchos onbjetos que estan precargados, por ello tienen una id propia puesta ya. De hecho si guardamos None en una variable, la id sera la misma que el propio valor.

```python
id(None)
140710988010128
```
```python
value = None

id(value)
140710988010128
```

Por ello, podemos decir que ver si el id de un objeto es None, es simplemente comprobar que el id coincide con el de el valor None, basicamente lo mismo que hace el is:

```python
id(value) == id(None)
True

value is None
True 
```

### Veracidad 

Al trabajar con tipos de expresiones que usan booleanos, se hace una conversión implícita en la que los valores que pasemos por ello, se transforman en True o False. Para ello veremos primero, los datos que son True y los que son False.

Los datos que veremos ahora son los unicos que dan como resultado False al pasarlos a booleanos:

```python
bool(False)
bool(None)
bool(0)
bool(0.0)
bool('')
bool([])
bool(())
bool({})
bool(set())
```

Sin contar estos valores visto previamente, el resto de valores que podamos pensar, daran valor True al pasarlos a booleano:

```python
bool('Perro')
True

bool([0, 1, 2])
True

bool('👌')
True
```

### Asignación lógica

Es la posibilidad de usar operadores lógicos en setenciad de asignación, usando a su vez las tablas de la verdad que se pueden usar para estos casos:

```python
value_2 = 0
value_3 = 5

value_1 = value_2 or value_3

print(vaule_1)
5
```

Al definir la variable value_1, podemos ver que estamos aplicando expresión lógica, por ello se hace una conversión implicita, pasan a tratarse como booleanos. Por ello podemos ver que la variable value_2 al tener valor 0, en booleano sería False, mientras que la variable value_3 con valor 5, pasa a ser True. Además, al estar en un or, el resultado será verdadero, eligiendose este valor de value_3 para la variable value_1.

Si probamos el mismo ejemplo con and:

```python
value_2 = 0
value_3 = 5

value_1 = value_2 and value_3

print(value_1)
0
```

En esta ocasión al estar en un and, el resultado será False, por lo que se asigna a value_1 como su valor


### Match case

Es un tipo de sentencia muy importante y similar a los "switch" en otros lenguajes. En su forma más simple, esta permite comparar un valor de entrada con una serie de casos, algo similar a lo que hacemos con if. Veamoslo mñas a fondo:

```python
pokemon_name = 'Bulbasaur'

match pokemon_name:
    case 'Charmander':
        print('Pokemon#004')
    case 'Squirtle':
        print('Pokemon#007')
    case 'Pikachu':
        print('Pokemon#025')

Bulbasaur
```

¿Y si por casualidad quisieramos poner un caso en el cual si el usuario introduce un valor que no esta en el case, le devuelva un error? Pues sería tan sencillo como hace run caso extra llamado "_" por el cual pase cualqueir valor que no esté en el case.

```python
pokemon_name = 'Scyther'

match pokemon_name:
    case 'Charmander'
        print('Pokemon#004')
    case 'Squirtle'
        print('Pokemon#007')
    case 'Pikachu'
        print('Pokemon#025')
    case _:
        print('Pokemon not found in our list!')

Pokemon not found in our list!
``` 

### Operador morsa

Por último veremos el llamado operador morsa, una implementación de Python 3.8, la cual permite juntar sentencias de asignación dentro de expresiones. Se escribe así ":="

Supongamos que queremos introducir el perímetro de una circunferencia, diciendole al usuario que debe incrementarlo siempre que a un mínimo que hayamos establecido:

De forma corriente lo haríamos así:

```python
radius = 4.25
perimeter = 2 * 3.14 * radius
if perimeter < 100:
    print('Increase radius to reach minimum perimeter')
    print('Actual perimeter: ', perimeter)

Increase radius to reach minimum perimeter
Actual perimeter:  26.69
```

Con el operador morsa sería así:

```python
radius = 4.25
if (perimeter := 2 * 3.14 * radius) < 100:
    print('Increase radius to reach minimum perimeter')
    print('Actual perimeter: ', perimeter)

Increase radius to reach minimum perimeter
Actual perimeter:  26.69
```

Como podemos, el operador morsa permite que podamos hacer un código limpio y compacto.
