# Números

Para empezar este tema, veremos los booleanos. Llamados asi por su creador, establecen la logica binaria, la cual esta determinada por dos valores:

- True: es decir, el valor verdadero, que corresponde a 1 en su representacion númerica

- False: el valor falso, correspondiende a 0 en valor numérico

```python
 is_false = False
 is_true = True

 is_false
 False
 is_true
 True
```

Ahora veremos los enteros, los cuales son aquellos números que no tienen decimales y pueden contener cualquier signo:

```python
>>> 9
9
>>> 18
18
>>> -7
-7
>>> 500000
500000
```
En números con muchos ceros, Python permite el poder poner _ para la mejor lectura del número.

Como es lógico, con los números se pueden hacer operaciones. He aqui los simbolos de las distintas operaciones:

| Operador | Descripción       | Ejemplo   | Resultado |
|----------|-------------------|-----------|-----------|
| +        | Suma              | 3 + 9     | 12        |
| -        | Resta             | 6 - 2     | 4         |
| *        | Multiplicación    | 5 * 5     | 25        |
| /        | División flotante | 9 / 2     | 4.5       |
| //       | División entera   | 9 // 2    | 4         |
| %        | Módulo            | 9 % 4     | 1         |
| **       | Exponenciación    | 2 ** 4    | 16        |

Con estos simbolos, podemos realizar cualquier operacion matemática. Como buenos programadores, se deben hacer espacios entre operadores y números para una mejor lectura del código:

```python
>>> 2+7
9
>>> 5-8
-3
>>> 5 // 2
2
>>> 5 / 2
2.5
>>> 5 ** 2
25
```

En Python existe la asignación aumentada. Esta nos permite mezclar signo "=" con cualquier otro signo, en vez de estar haciendo la operacion directamente. Veamos un ejemplo: 

Asi se haría de forma normal:

```python
>>> people_in_supermarket = 90
>>> people_in_street = 80
>>> more_people_supermarket = people_in_supermarket + people_in_street
>>> more_people_supermarket
170
```

Y asi con asignacion aumentada:

```python
>>> people_in_supermarket = 90
>>> people_in_street = 80
>>> people_in_supermarket += people_in_street
>>> people_in_supermarket
170
>>>
```

El módulo es simplemente el averiguar el resto de cualquier division usando el simbolo %.

```python
>>> 9 % 4
1
>>> 6 % 3
0
>>>
```

La exponenciación es la elevacion de un número usando ** 

```python
>>> 2 ** 2
4
>>> 4 ** 2
16
>>>
```

También podemos elevar un numero entero a uno decimal. En este caso es como si utilizaramos la raiz cuadrada. Para ello elevariamos el número deseado a 0.5:

```python
>>> 4 ** 0.5
2.0
```

En Python podemos encontrar la funcion abs() que nos da el valor absoluto de cualquier número:

```python
>>> abs(-1)
1
```

Una parte importante de los nuúmero en Python, son los llamados flotantes. Son aquellos numeros con parte decimal, como por ejemplo:

```python
>>> 4.0
4.0
```

Gracias a los diferentes tipos de datos en Python, muchas cosas del mundo real pueden ser representadas a través de la programación. Sin embargo, muchas veces hay que descubrir rebuscadas maneras para poder representar ciertas cosas. Aqui entra la conversión de tipos, entre las cuales existen las dos siguientes:

- Conversión implícita: Se mezclan enteros, booleanos y flotantes, haciendo una conversion de los valores al tipo de mayor rango:

```python
>>> True + 25 # Como True es equivalente a 1, se le suma a 25
26

>>> 7 * False # Debido a que False es equivalente a 0, al mutiplicarlo por cualquier numero, da igulamente 0
0

>>> 10 + 11.3
21.3
```

La conversión implicita se resume en:

| Tipo 1 | Tipo 2 | Resultado |
|--------|--------|-----------|
| bool   | int    | int       |
| bool   | float  | float     |
| int    | float  | float     |


- Conversion explícita: Existen ciertas funciones que pueden cambiar el tipo de un número a otro, las cuales son:

`bool()`: pasa un valor a booleano

`int()`: pasa un valor a entero

`float()`: pasa un valor a flotante

```python
>>> bool(0)
False

>>> int(True)
1

>>> float(8)
8.0
```

Cabe destacar la existencia de `isinstance()` la cual comprueba el tipo que tiene una variable de la siguiente manera:

```python
is_true = True

isinstance(is_raining, bool)
True
```
En Python existe la posibilidad de rendondear un valor, con la función `round()`. Incluso puedes indicarle la cantidad de decimales a los que quieres que te redondee:

```python
>>> pi = 3.14159265359
>>> round(pi)
3

>>> round(pi, 1)
3.1

>>> round(pi, 2)
3.14
```

Si bien los numeros que manejamos normalmente estan en base decimal (o base 10), hay otras bases (con prefijos y funciones propias), con las que podemos nombrar a los numeros:

- Base binaria: Con dos símbolos para representar valores, el 0 y el 1

    - Prefijo: 0b

    ```python
    0b1010
    10
    ```

    - Función: bin()

    ```python
    bin(10)
    '0b1010' 

    # Hay que tener en cuenta que bin() nos devuelve una cadena de texto (las cuales veremos más adelante en el temario)
    ```

- Base octal: Con ocho simbolos para representar valores, del 1 al 7
