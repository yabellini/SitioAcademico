---
title: "Quinto Encuentro. Aprendiendo a Programar en 30 lecciones"
weight: 5
subtitle: "Quinto encuentro"
excerpt: "Mi sobrino de 14 años quiere aprender a programar y yo voy a enseñarle. En esta clase resolvimos preguntas que Juan Cruz trajo sobre los datos, aprendimos algunos verbos nuevos de dplyr y hicimos nuestros primeros graficos"
date: 2024-03-24
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

## Preguntas sobre los datos

El ultimo ejercicio de la clase anterior era pensar en preguntas a contestar usando los datos de nuestros conjuntos de datos.  Juan Cruz trajo muchas preguntas, contestamos algunas y dejamos otras para mas adelante porque aun no habiamos visto los conceptos necesarios para poder resolverlas.

Veamos las preguntas que si pudimos contestar:

### Para copas

- *Todas las veces que Argentina quedo entre los 3 mejores*:podemos usar filter(), pero como indicamos que deje las filas en caso que Argentina haya sido campeon, subcampeon o tercero? 

`filter` puede tener mas de una condicion. 

> #### Ejercicio 1
> La clase pasada vimos que Brasil es el pais con mas campeonatos y que 161 es el maximo de goles en una de las copas en la que salieron campeones.  
> Como podriamos listar todas las copas en las que Brasil salio campeon pero que no tiene el maximo de goles anotados?


* Solucion propuesta durante la clase 

  ```{r}
  copas %>% 
    filter(Winner == "Brazil") %>% 
    filter(GoalsScored != 161)
  ```

* Podemos reescribir esa solucion de esta manera:

  ```{r}
  copas %>% 
    filter(Winner == "Brazil", GoalsScored != 161) 
  ```
Separar las condiciones con una coma es lo mismo que decir "y", en este caso seria: Que el ganador sea Brasil y que la cantidad de goles anotados no sea 161.

La expresion `!=` significa "distinto" o "no igual a". Ahora, como sabemos que otros simbolos existen para poder generar condiciones a usar con filter?

Las condiciones se generan con _operadores logicos_.  R tiene varios operadores logicos:


|operador |	definicion |		
|---------|------------|
| <	|menor que|
| x\|y |	x **o** y |
| <=	| menor o igual a |
| is.na(x)	| chequea si x es NA |
| !is.na(x)	| chequea si x **no** es NA |
| >	| mayor que |
| >= |	mayor o igual a	|
| x %in% y |	chequea si x esta en y |
| !(x %in% y)	| chequea si x **no esta** en y |
| == |	igual a |
| != | no igual a |
|!x	| no x |
| x & z	| x **y** z |

Entonces volviendo a la pregunta **Todas las veces que Argentina quedo entre los 3 mejores**, ahora podemos contestarla usando el operador **|** que significa **o**.

```{r}
copas %>% 
  filter(Winner == "Argentina" | `Runners-Up` == "Argentina" | Third == "Argentina")
  
# A tibble: 5 × 10
  Year       Country   Winner     `Runners-Up` Third     Fourth GoalsScored QualifiedTeams MatchesPlayed
  <date>     <chr>     <chr>      <chr>        <chr>     <chr>        <int>          <int>         <int>
1 1930-01-01 Uruguay   Uruguay    Argentina    USA       Yugos…          70             13            18
2 1978-01-01 Argentina Argentina  Netherlands  Brazil    Italy          102             16            38
3 1986-01-01 Mexico    Argentina  Germany FR   France    Belgi…         132             24            52
4 1990-01-01 Italy     Germany FR Argentina    Italy     Engla…         115             24            52
5 2014-01-01 Brazil    Germany    Argentina    Netherla… Brazil         171             32            64
# ℹ 1 more variable: Attendance <chr>
```

Al ver los resultados, nos dimos cuenta que si Argentina llego a la semifinal, siempre paso a la final, o sea *nunca perdimos una semifinal*!. Armamos esta consulta para chequear ese dato:

```{r}
copas %>% 
  filter(Third == "Argentina" | Fourth == "Argentina")
  
# A tibble: 0 × 10
# ℹ 10 variables: Year <date>, Country <chr>, Winner <chr>, Runners-Up <chr>, Third <chr>,
#   Fourth <chr>, GoalsScored <int>, QualifiedTeams <int>, MatchesPlayed <int>, Attendance <chr> 
```

### Consultas para jugadores.

* Listar todos los jugadores que tuvieron la 10.
 
```{r}
diez <- jugadores %>% 
  filter(`Shirt Number` == 10) 
```

La solucion propuesta es correcta, pero nos devuelve el mismo jugador varias veces, ya que ese jugador pudo haber jugado mas de un mundial con el mismo numero, por ejemplo Maradona con el numero 10.  Para obtener valores unicos, usamos la funcion `distinct()`.


```{r}
diez <- jugadores %>% 
  filter(`Shirt Number` == 10) %>% 
  distinct(`Player Name`)
```

### Consultas para partidos:

* Todos los cuartos de final de Argentina
  
```{r}
partidos %>% 
  filter(Stage == "Quarter-finals", 
        `Away Team Name` == "Argentina" | `Home Team Name` == "Argentina")
```
  
* Todos los partidos que en el primer tiempo se metieron 2 goles o mas

La cantidad de goles totales no esta en ninguna columna de nuestro conjunto de datos. 
Tenemos disponibles las variables `Half-time Home Goals` que son los goles del local
al llegar el medio tiempo y `Half-time Away Goals`, que son los goles del equipo
visitante al terminar el primer tiempo. 

Para agregar una columna con el total de goles, vamos a usar la función `mutate()`. 
  
```{r}
partidos %>% 
  mutate(goles = `Half-time Home Goals` + `Half-time Away Goals`) 
```

Esta operacion genera una nueva columna llamada `goles` que almacena el resultado de sumar los goles del visitante y del local, o sea, de sumar los valores que tienen las columnas
`Half-time Home Goals` y `Half-time Away Goals`.

Recordá que las funciones de dplyr nunca modifican la tabla original. `mutate()` devolvió una nueva tabla que es igual a la tabla `partidos` pero con la columna “goles” agregada. La tabla `partidos` sigue intacta.

Ahora podemos usar esa variable `goles` con la funcion `filter()`
  
```{r}
partidos %>% 
  mutate(goles = `Half-time Home Goals` + `Half-time Away Goals`) %>% 
  filter(goles >= 2)
```

* Todos los partidos que se jugaron en _Wembley_.

```{r}
partidos %>% 
  filter(Stadium == "Wembley Stadium")
```
  
* Todos los partidos que Argentina fue local

```{r}
partidos %>% 
  filter(`Home Team Name` == "Argentina")
```
  
* Ordenar los partidos por audiencia de mayor a menor. Cual fue el partido menos visto?
  
```{r}
partidos %>% 
  arrange(desc(Attendance))
```

* ya ahora ordenarlo de menor a mayor.  Cual fue el partido mas visto?
  
```{r}
partidos %>% 
  arrange(desc(Attendance))
```


## Preguntas para mas adelante:

Juan Cruz genero muchas preguntas mas, pero para poder responderlas tenemos que
aprender otros conceptos.  Asi que las dejamos para proximas clases.

Este es el listado propuesto y un breve detalle de que tenemos que aprender para
poder resolverlo.

* Jugadores:
  - _todos los jugadores que metieron 1 o mas  goles en el segundo tiempo._ Hay que ver manejo de cadenas porque los datos estan en la columna "Event" y con anotaciones al estilo "G20" o "Y56" que significan: "Gol a los 20 minutos" y "Tarjeta amarilla a los 56 minutos", respectivamente. 
  
  - _todos los jugadores que tuvieron de técnico a un sudamericano._  Hay que aprender manejo de cadenas y unir mas de un conjunto de datos, ya que la informacion no se encuentra en la tabla de jugadores solamente.  Tambien es necesario poder generar una nueva columna y asignar el valor usando case.
  - _ordenar los jugadores por cantidad de goles_. Al igual que la primera necesitamos aprender como manejar cadenas.

* Partidos y Jugadores:
  - _todos los partidos de Di Maria._
  - _todos los goles de Neymar._
  - _todos los partidos donde un Europeo fue visitante._
  
  Para todas estas consultas necesitamos aprender sobre cadenas, joins y case. 
  

* Copas:
  - _ordenar de mayor a menor o al revez la audiencia de los mundiales._ Cambiar al tipo correcto. Hay que entender locale y la configuracion regional de la computadora.  


## Graficos

Antes de terminar la clase, vamos a ver como podemos visualizar nuestros datos en otra forma que no sea una tabla de resultados.

Visualizar datos es útil para identificar a relación entre distintas variables pero también para comunicar el análisis de los datos y resultados. El paquete `ggplot2` permite generar gráficos de gran calidad en pocos pasos. Cualquier gráfico de ggplot tendrá como mínimo 3 componentes: los **datos**, un **sistema de coordenadas** y una **geometría** (la representación visual de los datos) y se irá construyendo por capas.

### Primera capa: el área del gráfico

Cómo siempre, primero hay que cargar los paquetes y los datos. Vamos a usar los datos de partidos para este primer grafico, asi que ya lo tenemos cargado. Para cargar el paquete usamos `library(ggplot2)`.

Nuestro objetivo es graficar la cantidad de goles en cada copa del mundo. Queremos poder graficar tambien la cantidad de goles que hacen los equipos locales y los equipos visitantes en cada copa del mundo.  

Para poder realizar ese grafico, primero tenemos que calcular la cantidad de goles por cada copa.  Podemos hacer ese agrupando por año y sumando la cantidad de goles del equipo visitante (variable `Away Team Goals`) y del equipo local (variable `Home Team Goals`) en cada partido y el total.  

Vamos a guardar esos calculos en un nuevo conjunto de datos llamado `goles`

```{r}
goles <- partidos %>% 
  group_by(Year) %>% 
  summarise(goles_v = sum(`Away Team Goals`),
            goles_l = sum(`Home Team Goals`),
            goles_t = goles_v + goles_l)
```

El paquete para hacer graficos se llama `ggplot2` y la funcion principal es `ggplot()`. El primer argumento de ggplot es el conjunto de datos (igual que las otras funciones del tidyverse), en nuestro caso sera `goles`.



```{r}
goles %>% 
  ggplot(mapping = aes(x= Year, y = goles_t)) +
  geom_line()


```

```{r}
goles %>% 
  ggplot() +
  geom_line(aes(x=Year, y = goles_v), color = "blue") +
  geom_line(aes(x=Year, y = goles_l), color = "green")
```






