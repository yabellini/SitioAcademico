---
title: "Quinto Encuentro. Aprendiendo a Programar en 30 lecciones"
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

```{r}
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
> 

```

Ahora la cantidad de casos (o sea participaciones en mundiales de los cinco paises mas goleadores) se redujo a **59**, versus las **357** filas de la solucion 1 donde estaban todos los paises que alguna vez jugaron en las copas del mundo presentes en el conjunto de datos.


## Solucion al tercer punto

Ahora que tenemos los datos podemos realizar el grafico.  Como primer paso Juan Cruz almaceno el resultado de la solucion del punto 2 en un objeto llamado `masgoleadores`.



```{r}
masgoleadores %>%
ggplot() +
  geom_line(aes(x=Year, y=golestotales, color= `Home Team Name`))

```


```{r}
masgoleadores %>%
ggplot() +
  geom_line(aes(x=Year, y=golestotales,color= `Home Team Name`))+
  geom_point(aes(x=Year, y=golestotales,color= `Home Team Name`))






```