---
title: "Octavo Encuentro. Aprendiendo a Programar en 30 lecciones"
weight: 8
subtitle: "Octavo encuentro"
excerpt: "Mi sobrino de 14 años quiere aprender a programar y yo voy a enseñarle. En esta clase volvemos a trabajar con los conjuntos de datos y las preguntas que nos hicimos. Vamos a convertir algunos tipos de datos y trabajar con characteres para contestar dos preguntas y hacer un grafico."
date: 2024-04-29
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

En esta clase volvemos a trabajar con los conjuntos de datos y las preguntas que nos hicimos. Vamos a convertir algunos tipos de datos y trabajar con characteres para contestar dos preguntas y hacer un grafico.


## Preguntas para (mas adelante) ahora.

En el quinto encuentro dejamos una serie de preguntas para mas adelante.  Hoy vamos a seleccionar de ese listado y vamos a resolverlas

* Copas: ordenar de mayor a menor o al revez la audiencia de los mundiales. 

* Jugadores:

  - todos los jugadores que metieron 1 o mas goles en el segundo tiempo. 
  - ordenar los jugadores por cantidad de goles. 
  
## Ordenar las copas por audencia.

El conjunto de datos copas tiene una columna llamada `Attendance` En este caso el problema esta en el tipo de dato que tiene esa columna.  Al importar los datos lo hace como caracter.  Cuando intentamos asignar el tipo correcto en la lectura de los datos no pudimos lograrlo:

- la columna se leia con todos valores nulos.
- la columna se leia con datos pero contenia valores erroneos.

Analicemos los datos de esa columna para determinar que esta pasando:

``` r 
glimpse(copas)

Rows: 20
Columns: 10
$ Year           <date> 1930-01-01, 1934-01-01, 1938-01-01, 1950-01-01, 1954-01-01, 1958-01-01, 1962-01-01, 1966-01-0…
$ Country        <chr> "Uruguay", "Italy", "France", "Brazil", "Switzerland", "Sweden", "Chile", "England", "Mexico",…
$ Winner         <chr> "Uruguay", "Italy", "Italy", "Uruguay", "Germany FR", "Brazil", "Brazil", "England", "Brazil",…
$ `Runners-Up`   <chr> "Argentina", "Czechoslovakia", "Hungary", "Brazil", "Hungary", "Sweden", "Czechoslovakia", "Ge…
$ Third          <chr> "USA", "Germany", "Brazil", "Sweden", "Austria", "France", "Chile", "Portugal", "Germany FR", …
$ Fourth         <chr> "Yugoslavia", "Austria", "Sweden", "Spain", "Uruguay", "Germany FR", "Yugoslavia", "Soviet Uni…
$ GoalsScored    <int> 70, 70, 84, 88, 140, 126, 89, 89, 95, 97, 102, 146, 132, 115, 141, 171, 161, 147, 145, 171
$ QualifiedTeams <int> 13, 16, 15, 13, 16, 16, 16, 16, 16, 16, 16, 24, 24, 24, 24, 32, 32, 32, 32, 32
$ MatchesPlayed  <int> 18, 17, 18, 22, 26, 35, 32, 32, 32, 38, 38, 52, 52, 52, 52, 64, 64, 64, 64, 64

$ Attendance     <chr> "590.549", "363.000", "375.700", "1.045.246", "768.607", "819.810", "893.172", "1.563.135", "1…
> 
```  


## Goleadores.

Hay que ver manejo de cadenas porque los datos estan en la columna “Event” y con anotaciones al estilo “G20” o “Y56” que significan: “Gol a los 20 minutos” y “Tarjeta amarilla a los 56 minutos”, respectivamente.