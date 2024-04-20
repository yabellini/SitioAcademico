---
title: "Sexto Encuentro. Aprendiendo a Programar en 30 lecciones"
weight: 6
subtitle: "Sexto encuentro"
excerpt: "Mi sobrino de 14 años quiere aprender a programar y yo voy a enseñarle. En esta clase Juan Cruz tuvo el desafio de generar el conjunto de datos necesario para hacer el grafico que le pedi.  La idea fue integrar en un ejercicio mas complejo diferentes conceptos que vimos en las clases 1 a 5."
date: 2024-04-18
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

En esta clase Juan Cruz tuvo el desafio de generar el conjunto de datos necesario para hacer el grafico que le pedi.  La idea fue integrar en un ejercicio mas complejo diferentes conceptos que vimos en las clases 1 a 5.

## El Desafio

Usando los conjunto de datos que venimos trabajando:

* Calcular la cantidad de goles por pais en cada copa del mundo.

* Quedarse con los cinco paises que mas goles hicieron teniendo en cuenta toda la historia de los mundiales.

* Hacer un grafico de lineas con esos cinco paises. 


## Solucion al primer punto

Vamos a usar la tabla `partidos`. Para poder tener la cantidad de goles por pais y por cada copa del mundo es necesario agrupar por estos dos valores. 

El año (columna `Year`) nos da la copa del mundo.  El pais lo podemos obtener por las columnas `Home Team Name` o `Away Team Name`.

Despues de agrupar, se deben sumar los goles del pais como local y como visitante (o sea sumar las columnas `Home Team Goals` y `Away Team Goals`) y guardarlos en una nueva variable.

Esta es la solucion de Juan Cruz:

``` r 
partidos %>%
  group_by(Year, `Home Team Name`) %>%
  summarise(golestotales = sum(`Home Team Goals` + `Away Team Goals`)) %>%
  arrange(desc(golestotales)) 
  
`summarise()` has grouped output by 'Year'. You can override using the `.groups` argument.
# A tibble: 367 × 3
# Groups:   Year [21]
   Year       `Home Team Name` golestotales
   <date>     <chr>                   <int>
 1 2014-01-01 Brazil                     36
 2 1954-01-01 Hungary                    32
 3 1954-01-01 Germany FR                 28
 4 1958-01-01 France                     26
 5 1970-01-01 Brazil                     26
 6 1950-01-01 Brazil                     25
 7 1998-01-01 Brazil                     24
 8 1938-01-01 Brazil                     22
 9 1954-01-01 Austria                    22
10 1966-01-01 Portugal                   22
# ℹ 357 more rows
# ℹ Use `print(n = ...)` to see more rows  
```


## Solucion al segundo punto

Ahora es necesario filtrar por los paises que mas goles hicieron.  Para eso primero deberiamos obtener cuales son esos paises. 

Se puede tener ese resultado si solo agrupamos por pais, lo que logramos usando el mismo codigo de la solucion uno, removiendo la columna `Year` del `group_by`. 

``` r 
partidos %>%
  group_by(`Home Team Name`) %>%
  summarise(golestotales = sum(`Home Team Goals` + `Away Team Goals`)) %>%
  arrange(desc(golestotales)) 
  
# A tibble: 79 × 2
   `Home Team Name` golestotales
   <chr>                   <int>
 1 Brazil                    258
 2 Argentina                 155
 3 Italy                     140
 4 Germany FR                135
 5 Germany                   101
 6 France                     99
 7 Hungary                    92
 8 Uruguay                    91
 9 Spain                      80
10 Sweden                     78
# ℹ 69 more rows
# ℹ Use cprint(n = ...)` to see more rows
```

Hay varias opciones para resolver este problema.  Juan Cruz decidio tomar los primeros cinco nombres y colocarlos en un `filter` con el operador `%in%`.  Por lo que al codigo de la solucion 1 le agrego el filtro: 

``` r
partidos %>%
  group_by(Year, `Home Team Name`) %>%
  summarise(golestotales = sum(`Home Team Goals`+ `Away Team Goals`)) %>%
  arrange(desc(golestotales)) %>% 
  filter(`Home Team Name` %in% c("Brazil", "Argentina", "Italy", "Germany FR", "Germany"))

`summarise()` has grouped output by 'Year'. You can override using the `.groups` argument.
# A tibble: 69 × 3
# Groups:   Year [20]
   Year       `Home Team Name` golestotales
   <date>     <chr>                   <int>
 1 2014-01-01 Brazil                     36
 2 1954-01-01 Germany FR                 28
 3 1970-01-01 Brazil                     26
 4 1950-01-01 Brazil                     25
 5 1998-01-01 Brazil                     24
 6 1938-01-01 Brazil                     22
 7 1930-01-01 Argentina                  21
 8 1958-01-01 Brazil                     20
 9 1970-01-01 Germany FR                 20
10 1990-01-01 Germany FR                 20
# ℹ 59 more rows
# ℹ Use `print(n = ...)` to see more rows
```

Ahora la cantidad de casos (o sea participaciones en mundiales de los cinco paises mas goleadores) se redujo a **59**, versus las **357** filas de la solucion 1 donde estaban todos los paises que alguna vez jugaron en las copas del mundo presentes en el conjunto de datos.


## Solucion al tercer punto

Ahora que tenemos los datos podemos realizar el grafico.  Como primer paso Juan Cruz almaceno el resultado de la solucion del punto 2 en un objeto llamado `masgoleadores`.

Este es el primer codigo de la solucion.  Previo a ejecutarlo y ver el resultado, Juan Cruz menciono que necesitaba una linea por pais, y que tenia que poder indicar de alguna manera esta caracteristica del grafico.  

``` r
masgoleadores %>%
  ggplot() +
  geom_line(aes(x=Year, y=golestotales))

```

<img src="linea_1.png" alt="Grafico con una linea negras que presenta la evolucion de la cantidad de goles realizadosa traves del tiempo en cada copa del mundo." />

Este grafico no nos sirve de mucho para distinguir los cinco paises y ver las diferencias entre ellos, ya que tiene una sola linea. 

### Mapear variables a elementos

Una solución sería utilizar otras variables de los datos, por ejemplo `Home Team Name` y mapear el color de las lineas de a cuerdo al pais (`Home Team Name`) al que pertenecen.


``` r
masgoleadores %>%
  ggplot() +
  geom_line(aes(x=Year, y=golestotales, color= `Home Team Name`))

```

<img src="linea_2.png" alt="Grafico con cinco lineas de diferente color que presentan la evolucion de la cantidad de goles realizadosa traves del tiempo en cada copa del mundo por cada pais en el conjunto de datos." />

Este grafico está un poco mejor. Se puede ver que Italia ha hecho menos goles que el resto de los paises y que Brasil tiene varios maximos en varias copas.  

Hay una linea que llama la atencion, la que corresponde a una de las Alemanias del conjunto de datos: la linea tiene el mismo valor durante varias copas.  Lo que nos lleva a preguntarnos que paso, realmente fueron tan consistente en la cantidad de goles en cada copa? o algo mas esta ocurriendo?  

###  Otras geometrías

Como ya vimos ggplot puede tener mas de una capa y un mismo grafico puede tener mas de una geometria. En este caso es recomendable agregar una capa con puntos, para ver en que copas participo cada pais. 

Por suerte las funciones `geom_*()` tienen más o menos nombres amigables, si queremos agregar una capa de puntos la funcion a usar es `geom_point()`

``` r
masgoleadores %>%
  ggplot() +
  geom_line(aes(x=Year, y=golestotales, color= `Home Team Name`))+
  geom_point(aes(x=Year, y=golestotales, color= `Home Team Name`))

```

<img src="linea_3.png" alt="Grafico con cinco lineas de diferente color que presentan la evolucion de la cantidad de goles realizadosa traves del tiempo en cada copa del mundo por cada pais en el conjunto de datos con una segunda capa con puntos del mismo color que la linea que muestra cuando un pais participo en una copa." />

Ahora si, conseguimos el gráfico que estamos buscando. Las líneas unen puntos consecutivos y permiten que el ojo siga la evolución de cada pais.

Tambien es mucho mas claro lo que pasa con las Alemanias:

* La linea de color verde tiene datos en el mundial de 1934 y luego no participo bajo ese nombre hasta el mundial 1994, por ende en el periodo comprendido entre esos años no hay datos y por eso la linea tiene esa forma recta horizontal. 

* Tambien podemos ver que la linea celeste de Alemania Occidental tiene datos desde 1954 a 1990.


Este ejemplo nos permite ver que a veces necesitamos mas de una geometria para poder analizar nuestros datos. 
