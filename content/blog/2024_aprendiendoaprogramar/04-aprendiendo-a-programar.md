---
title: "Cuarto Encuentro. Aprendiendo a Programar en 30 lecciones"
weight: 4
subtitle: "Cuarto encuentro"
excerpt: "Mi sobrino de 14 años quiere aprender a programar y yo voy a enseñarle. En esta clase aprendimos como cambiar el tipo de dato cuando leemos los archivos, que son los verbos de dplyr y el pipe. Los usamos para filtrar columnas filas ya agrupar casos."
date: 2024-03-23
draft: false
categories:
  - Español
  - rstats
  - Education
  - 100DaysToOffload
tags: 
  - Education
  - rstats
  - Español
  - 100DaysToOffload
---

En esta clase aprendimos como cambiar el tipo de dato cuando leemos los archivos, que son los verbos de dplyr y el pipe. Los usamos para filtrar columnas filas ya agrupar casos.

## Nuestros datos

La ultima clase leimos los datos de las copas del mundo y revisamos su estructura.  Algunas de las cosas que vimos en los datos son:

* Hay datos de 20 copas.
* Hay 37748 datos de jugadores.
* Hay datos de 4572 partidos.

En el conjunto de datos de copas:

* La columna Year no se carga como fecha, si no como numero. 
* La columna GoalsScored QualifiedTeams, MatchesPlayed se leen como numeros decimales, cuando deberian ser enteros.
* La columna Attendance se lee como caracter aunque es un numero.

En el conjunto de datos de jugadores, los datos que son numericos se leen todos como decimales cuando en realidad son enteros.

En el conjunto de datos de partidos se repiten los problemas con Year y con las variables que son numericas.

### Indicando el tipo de dato

Las funciones para leer datos de R nos permiten indicar que tipo de datos tiene cada columna, en caso que la lectura por defecto asigne el tipo de forma incorrecta.  Este es un ejemplo para poder modificar el tipo de las columnas en el conjunto de datos de _jugadores_

``` r
jugadores <- read_csv("Data/WorldCupPlayers.csv", 
                      col_types = cols(RoundID = col_integer(), 
                                  MatchID = col_integer(), `Shirt Number` = col_integer()))

```

> #### Ejercicio 1
> 1. Modificar la lectura de los conjunto de datos de _copas_ y _partidos_ para que cada columna tenga el tipo correcto.
> 2. Encontraste inconvenientes con alguna columna? Que puede estar pasando?

## Empezando a trabajar con los datos.

En este curso vamos a centrarnos las cinco acciones o verbos más comunes:

-   `select()`: selecciona columnas de una tabla.
-   `filter()`: selecciona (o filtra) filas de una tabla a partir de una o más condiciones lógicas.
-   `group_by()`: agrupa una tabla en base al valor de una o más columnas.
-   `mutate()`: agrega nuevas columnas a una tabla.
-   `summarise()`: calcula estadísticas para cada grupo de una tabla.


### Select: para seleccionar con que columnas voy a trabajar

Quiero trabajar con el año, el pais y el ganador de cada copa del mundo realizada.  Para quedarme con unicamente con las columnas mencionadas uso `select()`  

``` r

select(copas, Year, Country, Winner)

```

El primer argumento de la funcion select es el conjunto de datos y luego las columnas con las que quiero quedarme.

¿Dónde quedó este resultado? Si te fijás en la tabla `copas`, su formato no cambió, sigue teniendo todas las columnas originales a pesar de nuestro select:

``` r
copas

> copas
# A tibble: 20 × 10
   Year       Country      Winner     `Runners-Up` Third Fourth GoalsScored QualifiedTeams MatchesPlayed
   <date>     <chr>        <chr>      <chr>        <chr> <chr>        <int>          <int>         <int>
 1 1930-01-01 Uruguay      Uruguay    Argentina    USA   Yugos…          70             13            18
 2 1934-01-01 Italy        Italy      Czechoslova… Germ… Austr…          70             16            17
 3 1938-01-01 France       Italy      Hungary      Braz… Sweden          84             15            18
 4 1950-01-01 Brazil       Uruguay    Brazil       Swed… Spain           88             13            22
 5 1954-01-01 Switzerland  Germany FR Hungary      Aust… Urugu…         140             16            26
 6 1958-01-01 Sweden       Brazil     Sweden       Fran… Germa…         126             16            35
 7 1962-01-01 Chile        Brazil     Czechoslova… Chile Yugos…          89             16            32
 8 1966-01-01 England      England    Germany FR   Port… Sovie…          89             16            32
 9 1970-01-01 Mexico       Brazil     Italy        Germ… Urugu…          95             16            32
10 1974-01-01 Germany      Germany FR Netherlands  Pola… Brazil          97             16            38
11 1978-01-01 Argentina    Argentina  Netherlands  Braz… Italy          102             16            38
12 1982-01-01 Spain        Italy      Germany FR   Pola… France         146             24            52
13 1986-01-01 Mexico       Argentina  Germany FR   Fran… Belgi…         132             24            52
14 1990-01-01 Italy        Germany FR Argentina    Italy Engla…         115             24            52
15 1994-01-01 USA          Brazil     Italy        Swed… Bulga…         141             24            52
16 1998-01-01 France       France     Brazil       Croa… Nethe…         171             32            64
17 2002-01-01 Korea/Japan  Brazil     Germany      Turk… Korea…         161             32            64
18 2006-01-01 Germany      Italy      France       Germ… Portu…         147             32            64
19 2010-01-01 South Africa Spain      Netherlands  Germ… Urugu…         145             32            64
20 2014-01-01 Brazil       Germany    Argentina    Neth… Brazil         171             32            64
# ℹ 1 more variable: Attendance <chr>

```

`select()` y el resto de las funciones de dplyr siempre generan una nueva tabla y nunca modifican la tabla original. Para guardar la tabla con las tres columnas `Year`, `Country` y `Winner` tenés que asignar el resultado a una nueva variable.


### Filter: filtra filas o casos. 

Ahora podés usar `filter()` para quedarte con sólo unas filas. Por ejemplo, para quedarse con las copas donde se hayan anotado mas de 100 goles. 

``` r
filter(copas, GoalsScored > 100)

# A tibble: 12 × 10
   Year       Country      Winner     `Runners-Up` Third Fourth GoalsScored QualifiedTeams MatchesPlayed
   <date>     <chr>        <chr>      <chr>        <chr> <chr>        <int>          <int>         <int>
 1 1954-01-01 Switzerland  Germany FR Hungary      Aust… Urugu…         140             16            26
 2 1958-01-01 Sweden       Brazil     Sweden       Fran… Germa…         126             16            35
 3 1978-01-01 Argentina    Argentina  Netherlands  Braz… Italy          102             16            38
 4 1982-01-01 Spain        Italy      Germany FR   Pola… France         146             24            52
 5 1986-01-01 Mexico       Argentina  Germany FR   Fran… Belgi…         132             24            52
 6 1990-01-01 Italy        Germany FR Argentina    Italy Engla…         115             24            52
 7 1994-01-01 USA          Brazil     Italy        Swed… Bulga…         141             24            52
 8 1998-01-01 France       France     Brazil       Croa… Nethe…         171             32            64
 9 2002-01-01 Korea/Japan  Brazil     Germany      Turk… Korea…         161             32            64
10 2006-01-01 Germany      Italy      France       Germ… Portu…         147             32            64
11 2010-01-01 South Africa Spain      Netherlands  Germ… Urugu…         145             32            64
12 2014-01-01 Brazil       Germany    Argentina    Neth… Brazil         171             32            64
# ℹ 1 more variable: Attendance <chr>
```

> #### Ejercicio 2: usemos los dos verbos que aprendimos
> 
>  1. Filtren el anio 1986
>
>  2. Filtren cuando el ganador es Brasil
>
>  3. Filtren cuando la cantidad de equipos es mayor a 30
>
>  4. Filtren cuando el anio es 1930
> 
>  5. Selecciones las columnas de cantidad de goles. 


#### Soluciones al ejercicio 2

``` r
filter(copas, GoalsScored > 100)

filter(copas, Year == 1986)

filter(copas, Winner == "Brazil")

filter(copas, QualifiedTeams < 30)

filter(copas, Year == 1930)

select(copas, GoalsScored)

```

La mayoría de los análisis consisten en varios pasos que van generando tablas intermedias. La única tabla que te interesa es la última, por lo que ir asignando variables nuevas en cada paso intermedio es tedioso y poco práctico. Para eso se usa el operador ‘pipe’ (`%>%`).

Este operador ‘pipe’ (`%>%`) agarra el resultado de una función y se lo pasa a la siguiente. Esto permite escribir el código como una cadena de funciones que van operando sobre el resultado de la anterior.

Dos de las operaciones anteriores (seleccionar tres columnas y luego filtrar las filas correspondientes a las copas donde el ganador fue Brasil) se pueden escribir uno después del otro y sin asignar los resultados intermedios a nuevas variables de esta forma:

``` r
copas %>% 
  select(Year, Country, Winner) %>% 
  filter(Winner == "Brazil") %>% 
```

La forma de “leer” esto es “Tomá el conjunto de datos de `copas`, **despues** aplicale `select(Year, Country, Winner)` y **después** aplicale `filter(Winner == "Brazil")`”.

Cómo vimos, el primer argumento de todas las funciones de dplyr es el data frame sobre el cual van a operar, pero notá que en las líneas con `select()` y `filter()` no escribís la tabla explícitamente.
Esto es porque la pipe implícitamente pasa el resultado de las líneas anteriores como el primer argumento de la función siguiente.

Toma el data frame `copas` y se lo pasa al primer argumento de `select()`. Luego el data frame resultante de esa operación pasa como el primer argumento de la función `filter()` gracias al `%>%`.

> Tip: En RStudio podés escribir %>% usando el atajo de teclado Ctr + Shift + M. ¡Probalo!

> #### Ejercicio 3
>
> Escribir una combinacion de verbos usando el pipe que nos liste todas las copas en la que Brasil fue el campeon e Italia el subcampeon.

**Una posible solucion ejercicio 3**

``` r
copas %>% 
  filter(Winner == "Brazil") %>% 
  select(Year, Winner, Country, `Runners-Up`) %>% 
  filter(`Runners-Up` == "Italy") 

```

## Agrupar casos, generar nuevas columnas y calcular resumenes.

El pipe o _tuberia_ nos va a permitir realizar operaciones interesantes como agrupar casos, generar nuevas columnas y calcular resumenes. 

### Saber cuantas veces salio campeon cada pais.

Para poder contestar esa pregunta, primero hay que agrupar por pais para luego poder contar cuantas veces salio campeon.  Hay que usar el combo `group_by() %>% summarise()`.

``` r
copas %>% 
  group_by(Winner) 
  
# A tibble: 20 × 10
# Groups:   Winner [9]
   Year       Country      Winner     `Runners-Up` Third Fourth GoalsScored QualifiedTeams MatchesPlayed
   <date>     <chr>        <chr>      <chr>        <chr> <chr>        <int>          <int>         <int>
 1 1930-01-01 Uruguay      Uruguay    Argentina    USA   Yugos…          70             13            18
 2 1934-01-01 Italy        Italy      Czechoslova… Germ… Austr…          70             16            17
 3 1938-01-01 France       Italy      Hungary      Braz… Sweden          84             15            18
 4 1950-01-01 Brazil       Uruguay    Brazil       Swed… Spain           88             13            22
 5 1954-01-01 Switzerland  Germany FR Hungary      Aust… Urugu…         140             16            26
 6 1958-01-01 Sweden       Brazil     Sweden       Fran… Germa…         126             16            35
 7 1962-01-01 Chile        Brazil     Czechoslova… Chile Yugos…          89             16            32  
```


A primera vista parecería que la función no hizo nada, pero fijate que el resultado ahora dice que tiene grupos (“Groups:”), y nos dice qué columna es la que agrupa los datos (“Winner”) y cuántos grupos hay (“9”). Las operaciones subsiguientes que le hagamos a esta tabla van a hacerse para cada uno de esos nueve grupos.

Para ver esto en acción, usá `summarise()` para computar la cantidad de veces que aparece cada pais.

``` r
copas %>% 
  group_by(Winner) %>% 
  summarise(cantidad = n()) 

# A tibble: 9 × 2
  Winner     cantidad
  <chr>         <int>
1 Argentina         2
2 Brazil            5
3 England           1
4 France            1
5 Germany           1
6 Germany FR        3
7 Italy             4
8 Spain             1
9 Uruguay           2
```

El resultado se veria mejor si pudieramos ordenar el listado por el pais que mas veces gano la copa del mundo, para eso usamos la funcion `arrange()` y para indicarle que ordene de mayor a menor usamos la funcion `desc()` por dencendente.

``` r
copas %>% 
  group_by(Winner) %>% 
  summarise(cantidad = n()) %>% 
  arrange(desc(cantidad))

# A tibble: 9 × 2
  Winner     cantidad
  <chr>         <int>
1 Brazil            5
2 Italy             4
3 Germany FR        3
4 Argentina         2
5 Uruguay           2
6 England           1
7 France            1
8 Germany           1
9 Spain             1
```

> #### Ejercicio 4 
> 
> Usa la ayuda para ver que hace la funcion `n()` 


`group_by()` permite agrupar en base a múltiples columnas y `summarise()` permite generar múltiples columnas de resumen. Por ejemplo podriamos querer saber cual fue el maximo de goles anotados cuando cada pais salio campeon.

``` r
copas %>% 
  group_by(Winner) %>% 
  summarise(cantidad = n(),
            max_goles = max(GoalsScored)) %>% 
  arrange(desc(cantidad))

# A tibble: 9 × 3
  Winner     cantidad max_goles
  <chr>         <int>     <int>
1 Brazil            5       161
2 Italy             4       147
3 Germany FR        3       140
4 Argentina         2       132
5 Uruguay           2        88
6 England           1        89
7 France            1       171
8 Germany           1       171
9 Spain             1       145

```

El resultado va a siempre ser una tabla con la misma cantidad de filas que grupos y una cantidad de columnas igual a la cantidad de columnas usadas para agrupar y los estadísticos calculados.


> #### Ejercicio 5: Pensar preguntas para cada uno de los conjuntos de datos usando los verbos que aprendimos hoy.  Las vamos a resolver la clase que viene.

