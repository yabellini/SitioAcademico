---
title: "Noveno Encuentro. Aprendiendo a Programar en 30 lecciones"
weight: 9
subtitle: "Noveno encuentro"
excerpt: "Mi sobrino de 14 años quiere aprender a programar y yo voy a enseñarle. En esta clase resolvemos otra de las preguntas que nos hicimos sobre los datos y aprendemos la diferencia entre geom_col y geom_bar para hacer graficos de barra.  Tambien aprendemos como hacer graficos de area y repasamos graficos de lineas y de puntos."
date: 2024-05-15
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

La clase pasada nos quedo de tarea contestar la pregunta de cuantos goles metieron los jugadores en el segundo tiempo.  Vamos a resolver esa pregunta paso a paso. 

> ## Ejercicio 2: Jugadores que metieron goles en el segundo tiempo.

La clase pasada generamos un conjunto de datos con todos los goles que se metieron en el mundial.  Vamos a usar esos datos para resolver la pregunta.  Primero vamos a cargar los datos y a ver como se ven.

``` r
goleadores <- jugadores %>% 
  separate_longer_delim(Event, delim = " ")

goleadores %>% select(`Player Name`, Event)
# A tibble: 39,419 × 2
   `Player Name`    Event
   <chr>            <chr>
 1 Alex THEPOT      NA   
 2 Oscar BONFIGLIO  NA   
 3 Marcel LANGILLER G40' 
 4 Juan CARRENO     G70' 
 5 Ernest LIBERATI  NA   
 6 Rafael GARZA     NA   
 7 Andre MASCHINOT  G43' 
 8 Andre MASCHINOT  G87' 
 9 Hilario LOPEZ    NA   
10 Etienne MATTLER  NA   
# ℹ 39,409 more rows
# ℹ Use `print(n = ...)` to see more rows

```

Recordemos que el campo `Event` tiene el tipo de evento y el minuto en el que ese vento ocurrio.  La letra _G_ es la que indica que se metio un gol.

Usamo el codigo que ya escribimos para contar cuantos goles metio cada jugador:

1. Primero vamos a filtrar los eventos que son goles usando `filter` y `str_detect` para buscar la letra "G" en el campo `Event`.
2. Luego vamos a contar cuantos goles metio cada jugador usando `count` y `arrange` para ordenar de mayor a menor.

``` r
goleadores %>% 
  filter(str_detect(Event,"G")) %>% 
  count(`Player Name`) %>%
  arrange(desc(n))
```  

Para poder contestar la pregunta necesitamos saber cuando se metieron los goles. Esa informacion esta al lado de la letra G, asi que necesitamos poder tener los minutos en otra columna para luego poder filtrar.

Vamos a usar la funcion `mutate` para crear una nueva columna llamada `minutes` que va a tener el minuto en el que se metio el gol.  Para eso vamos a usar la funcion `parse_number` de readr que permite extraer el numero del string. 

> En el siguiente codigo seleccionamos solo las columnas que nos interesan para ver mejor el resultado del mutate.

``` r
goleadores %>% 
    filter(str_detect(Event,"G")) %>%
    mutate(minutes = parse_number(Event)) %>% 
    select(`Player Name`, Event, minutes)

# A tibble: 2,194 × 3
   `Player Name`    Event minutes
   <chr>            <chr>   <dbl>
 1 Marcel LANGILLER G40'       40
 2 Juan CARRENO     G70'       70
 3 Andre MASCHINOT  G43'       43
 4 Andre MASCHINOT  G87'       87
 5 Lucien LAURENT   G19'       19
 6 Tom FLORIE       G45'       45
 7 Bart McGHEE      G23'       23
 8 Bert PATENAUDE   G69'       69
 9 Ivica BEK        G30'       30
10 PREGUINHO        G62'       62
# ℹ 2,184 more rows
# ℹ Use `print(n = ...)` to see more rows
```

Ahora que tenemos los minutos en una columna podemos filtrar los goles que se metieron en el segundo tiempo.  Para eso vamos a usar la funcion `filter` de dplyr y la funcion `between` que nos permite filtrar los valores que estan entre dos numeros.  

un partido de futbol tiene dos tiempos de 45 minutos cada uno, asi que los minutos del segundo tiempo estan entre 45 y 90.  En algunos mundiales hay alargue, que va del minuto 91 en adelante. Vamos a filtrar los goles que se metieron en el segundo tiempo y a contar cuantos goles metio cada jugador. Finalmente vamos a ordenarlos de mayor a menor.

``` r
goleadores %>% 
  filter(str_detect(Event,"G")) %>%
  mutate(minutes = parse_number(Event)) %>% 
  filter(minutes > 45, minutes < 90) %>%
  count(`Player Name`) %>%
  arrange(desc(n))

# A tibble: 778 × 2
   `Player Name`                          n
   <chr>                              <int>
 1 RONALDO                               11
 2 PEL� (Edson Arantes do Nascimento)     8
 3 Uwe SEELER                             8
 4 JAIRZINHO                              7
 5 KLOSE                                  7
 6 SNEIJDER                               7
 7 Teofilo CUBILLAS                       7
 8 Diego MARADONA                         6
 9 Helmut RAHN                            6
10 Just FONTAINE                          6
# ℹ 768 more rows
# ℹ Use `print(n = ...)` to see more rows  
```

## Mas graficos

En la clases pasadas generamos varios graficos de barra. En R hay dos funciones que permiten hacer graficos de barra: `geom_bar` y `geom_col`.  La diferencia entre las dos funciones es que `geom_bar` calcula los valores de la variable que se esta graficando y `geom_col` usa los valores que se le pasan.  

Vamos a usar un tutorial para entender la diferencia.  En ese tutorial ademas repasaremos como hacer graficos de area, de lineas y de puntos.  Vamos a usar el dataset `gapminder`.

Sigue estas instrucciones para utilizar el tutorial:

* Para instalar la versión de desarrollo desde GitHub, escribe el siguiente código :

``` r
remotes::install_github("yabellini/tutorialgRaficosFN")
```

* Si este codigo te da un error que el paquete remotes no existe, entonces instala el paquete remotes con `install.packages("remotes")` y luego ejecuta el codigo de arriba nuevamente. 

* Si se intaló correctamente y tienes la última versión de RStudio aparecerá en tu panel de Tutorial (arriba a la derecha en la configuracion estandar de RStudio).

* Puedes ejecutar el tutorial escribiendo este codigo en la consola de R:

``` r
learnr::run_tutorial("graficos", package = "TutorialgRaficosFN")
``` 

* Si el codigo de arriba te da un error que el paquete learnr no existe, entonces instala el paquete learnr con `install.packages("learnr")` y luego ejecuta el codigo de arriba nuevamente.


Así se ve el tutorial cuando está ejecutandose:

![](learnr_contenido_ggplot.png)

> Luego que Juan Cruz termino el tutorila vimos las dudas y terminamos la clase.  En el proximo encuentro seguiremos con mas detalles sobre como funcionan las capas de ggplot y como podemos empezar a mejorar el aspecto de nuestros graficos.
