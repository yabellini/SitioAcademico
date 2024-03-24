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

Primero, filter puede tener mas de una condicion. 

> #### Ejercicio 1
>
> 


* Solucion propuesta
```{r}
copas %>% 
  filter(Winner == "Brazil") %>% 
  filter(GoalsScored != 161)
```

* Otra solucion:
```{r}
copas %>% 
  filter(Winner == "Brazil", GoalsScored != 161) 
```
Las condiciones se generan con operadores logicos:


operator	definition		operator	definition
<	less than		x | y	x OR y
<=	less than or equal to		is.na(x)	test if x is NA
>	greater than		!is.na(x)	test if x is not NA
>=	greater than or equal to		x %in% y	test if x is in y
==	exactly equal to		!(x %in% y)	test if x is not in y
!=	not equal to		!x	not x
x & y	x AND y

```{r}
copas %>% 
  filter(Winner == "Argentina" | `Runners-Up` == "Argentina" | Third == "Argentina")
```

Al ver los resultados, nos dimos cuenta que si Argentina llego a la semifinal, siempre paso a la final.  Nunca perdimos una semifinal.  Armamos esta consulta para chequear ese datos

```{r}
copas %>% 
  filter(Third == "Argentina")
```

* para jugadores:
 - todos los jugadores que tuvieron la 10
 
```{r}
diez <- jugadores %>% 
  filter(`Shirt Number` == 10) %>% 
  distinct(`Player Name`)
```

* para partidos:
  - todos los cuartos de final de argentina
  
```{r}
partidos %>% 
  filter(Stage == "Quarter-finals", `Away Team Name` == "Argentina" | `Home Team Name` == "Argentina")
```
  
  - todos los partidos que en el primer tiempo se metieron 2 goles o mas
  
```{r}
partidos %>% 
  mutate(goles = `Half-time Home Goals` + `Half-time Away Goals`) %>% 
  filter(goles >= 2)
```
  
  
  - todos los partidos que se jugaron en wembley

```{r}
partidos %>% 
  filter(Stadium == "Wembley Stadium")
```
  
  
  - todos los partidos que argentina fue local

```{r}
partidos %>% 
  filter(`Home Team Name` == "Argentina")
```
  
  
  - ordenar los partidos por audiencia de menor a mayor
  
```{r}
partidos %>% 
  arrange(desc(Attendance))
```
  

## Preguntas para mas adelante:

jugadores:
  - todos los jugadores que metieron 1 o mas  goles en el segundo tiempo - manejo de cadenas
  - todos los jugadores que tuvieron de técnico a un sudamericano - manejo de cadenas y join con otras tablas.  Switch.
  - ordenar los jugadores por cantidad de goles

partidos y jugadores:
  - todos los partidos de di maria
  - todos los goles de neymar
  - todos los partidos donde un europeo fue visitante

copas:
  - ordenar de mayor a menor o al revez la audiencia de los mundiales. Cambiar al tipo correcto. 


## Graficos

```{r}
goles <- partidos %>% 
  group_by(Year) %>% 
  summarise(goles_v = sum(`Away Team Goals`),
            goles_l = sum(`Home Team Goals`),
            goles_t = goles_v + goles_l)
```

El paquete para hacer graficos se llama ggplot2 y la funcion es ggplot.

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






