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
  
## Ordenar las copas por audiencia.

El conjunto de datos copas tiene una columna llamada `Attendance` que contiene la cantidad de gente que fue a ver los partidos a los estadios.

La funcion para ordenar es `arrange` y si la usamos este es el resultado que obtenemos:

``` r
copas %>% 
  arrange(Attendance)

# A tibble: 20 × 10
   Year       Country      Winner     `Runners-Up`   Third   Fourth GoalsScored QualifiedTeams MatchesPlayed Attendance
   <date>     <chr>        <chr>      <chr>          <chr>   <chr>        <int>          <int>         <int> <chr>     
 1 1950-01-01 Brazil       Uruguay    Brazil         Sweden  Spain           88             13            22 1.045.246 
 2 1978-01-01 Argentina    Argentina  Netherlands    Brazil  Italy          102             16            38 1.545.791 
 3 1966-01-01 England      England    Germany FR     Portug… Sovie…          89             16            32 1.563.135 
 4 1970-01-01 Mexico       Brazil     Italy          German… Urugu…          95             16            32 1.603.975 
 5 1974-01-01 Germany      Germany FR Netherlands    Poland  Brazil          97             16            38 1.865.753 
 6 1982-01-01 Spain        Italy      Germany FR     Poland  France         146             24            52 2.109.723 
 7 1986-01-01 Mexico       Argentina  Germany FR     France  Belgi…         132             24            52 2.394.031 
 8 1990-01-01 Italy        Germany FR Argentina      Italy   Engla…         115             24            52 2.516.215 
 9 2002-01-01 Korea/Japan  Brazil     Germany        Turkey  Korea…         161             32            64 2.705.197 
10 1998-01-01 France       France     Brazil         Croatia Nethe…         171             32            64 2.785.100 
11 2010-01-01 South Africa Spain      Netherlands    Germany Urugu…         145             32            64 3.178.856 
12 2006-01-01 Germany      Italy      France         Germany Portu…         147             32            64 3.359.439 
13 2014-01-01 Brazil       Germany    Argentina      Nether… Brazil         171             32            64 3.386.810 
14 1994-01-01 USA          Brazil     Italy          Sweden  Bulga…         141             24            52 3.587.538 
15 1934-01-01 Italy        Italy      Czechoslovakia Germany Austr…          70             16            17 363.000   
16 1938-01-01 France       Italy      Hungary        Brazil  Sweden          84             15            18 375.700   
17 1930-01-01 Uruguay      Uruguay    Argentina      USA     Yugos…          70             13            18 590.549   
18 1954-01-01 Switzerland  Germany FR Hungary        Austria Urugu…         140             16            26 768.607   
19 1958-01-01 Sweden       Brazil     Sweden         France  Germa…         126             16            35 819.810   
20 1962-01-01 Chile        Brazil     Czechoslovakia Chile   Yugos…          89             16            32 893.172   
> 
  
```

Como podemos ver, el orden no es el esperado si la variable fuera numerica, ese orden corresponde a un orden alfabetico. Por lo que el problema esta en el tipo de dato que tiene esa columna.  Al importar los datos leyendo el CSV lo hace como caracter.  Cuando intentamos asignar el tipo correcto en la lectura de los datos no pudimos lograrlo:

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

Los valores en `Attendance` son numeros que estan usando el punto como separador de miles. Y es por eso que son leidos como texto en vez de numeros. 

El paquete `readr` tiene una funcion llamada `parse_number` que extrae los numeros. Esto elimina cualquier carácter no numérico antes o después del primer número. El separador de miles especificado por la *configuración regional* se ignora dentro del número. Veamos que hace esta funcion:

``` r
copas %>% 
  mutate(asistencia = parse_number(Attendance))

# A tibble: 20 × 11
   Year       Country   Winner `Runners-Up` Third Fourth GoalsScored QualifiedTeams MatchesPlayed Attendance asistencia
   <date>     <chr>     <chr>  <chr>        <chr> <chr>        <int>          <int>         <int> <chr>           <dbl>
 1 1930-01-01 Uruguay   Urugu… Argentina    USA   Yugos…          70             13            18 590.549        591.  
 2 1934-01-01 Italy     Italy  Czechoslova… Germ… Austr…          70             16            17 363.000        363   
 3 1938-01-01 France    Italy  Hungary      Braz… Sweden          84             15            18 375.700        376.  
 4 1950-01-01 Brazil    Urugu… Brazil       Swed… Spain           88             13            22 1.045.246        1.04
 5 1954-01-01 Switzerl… Germa… Hungary      Aust… Urugu…         140             16            26 768.607        769.  
 6 1958-01-01 Sweden    Brazil Sweden       Fran… Germa…         126             16            35 819.810        820.  
 7 1962-01-01 Chile     Brazil Czechoslova… Chile Yugos…          89             16            32 893.172        893.  
 8 1966-01-01 England   Engla… Germany FR   Port… Sovie…          89             16            32 1.563.135        1.56
 9 1970-01-01 Mexico    Brazil Italy        Germ… Urugu…          95             16            32 1.603.975        1.60
10 1974-01-01 Germany   Germa… Netherlands  Pola… Brazil          97             16            38 1.865.753        1.86
11 1978-01-01 Argentina Argen… Netherlands  Braz… Italy          102             16            38 1.545.791        1.54
12 1982-01-01 Spain     Italy  Germany FR   Pola… France         146             24            52 2.109.723        2.11
13 1986-01-01 Mexico    Argen… Germany FR   Fran… Belgi…         132             24            52 2.394.031        2.39
14 1990-01-01 Italy     Germa… Argentina    Italy Engla…         115             24            52 2.516.215        2.52
15 1994-01-01 USA       Brazil Italy        Swed… Bulga…         141             24            52 3.587.538        3.59
16 1998-01-01 France    France Brazil       Croa… Nethe…         171             32            64 2.785.100        2.78
17 2002-01-01 Korea/Ja… Brazil Germany      Turk… Korea…         161             32            64 2.705.197        2.70
18 2006-01-01 Germany   Italy  France       Germ… Portu…         147             32            64 3.359.439        3.36
19 2010-01-01 South Af… Spain  Netherlands  Germ… Urugu…         145             32            64 3.178.856        3.18
20 2014-01-01 Brazil    Germa… Argentina    Neth… Brazil         171             32            64 3.386.810        3.39
  
```

Al utilizarla entiende el punto como un decimal y cambia el tipo de dato a doble. Esto no es correcto ya que los valores presentados corresponden a cientos de miles y a millones. Podemos indicarle a la funcion que el separador de miles es el punto y el de decimales es la coma.  Para eso usamos la funcion `readr::parse_number` y le pasamos los argumentos `locale = locale(grouping_mark = ".", decimal_mark = ",")`:

``` r
  copas %>%
    mutate(asistencia = parse_number(Attendance, locale = locale(grouping_mark = "."))) %>% 
    select(Attendance, asistencia) 
    
# A tibble: 20 × 2
   Attendance asistencia
   <chr>           <dbl>
 1 590.549        590549
 2 363.000        363000
 3 375.700        375700
 4 1.045.246     1045246
 5 768.607        768607
 6 819.810        819810
 7 893.172        893172
 8 1.563.135     1563135
 9 1.603.975     1603975
10 1.865.753     1865753
11 1.545.791     1545791
12 2.109.723     2109723
13 2.394.031     2394031
14 2.516.215     2516215
15 3.587.538     3587538
16 2.785.100     2785100
17 2.705.197     2705197
18 3.359.439     3359439
19 3.178.856     3178856
20 3.386.810     3386810
> 

```

Ahora si, los datos estan en el formato correcto y podemos ordenarlos usando `arrange`.

``` r
copas %>% 
  mutate(asistencia = parse_number(Attendance, locale = locale(grouping_mark = "."))) %>% 
  arrange(desc(asistencia)) %>% 
  select(Year, Country, Attendance, asistencia)
 
 # A tibble: 20 × 4
   Year       Country      Attendance asistencia
   <date>     <chr>        <chr>           <dbl>
 1 1994-01-01 USA          3.587.538     3587538
 2 2014-01-01 Brazil       3.386.810     3386810
 3 2006-01-01 Germany      3.359.439     3359439
 4 2010-01-01 South Africa 3.178.856     3178856
 5 1998-01-01 France       2.785.100     2785100
 6 2002-01-01 Korea/Japan  2.705.197     2705197
 7 1990-01-01 Italy        2.516.215     2516215
 8 1986-01-01 Mexico       2.394.031     2394031
 9 1982-01-01 Spain        2.109.723     2109723
10 1974-01-01 Germany      1.865.753     1865753
11 1970-01-01 Mexico       1.603.975     1603975
12 1966-01-01 England      1.563.135     1563135
13 1978-01-01 Argentina    1.545.791     1545791
14 1950-01-01 Brazil       1.045.246     1045246
15 1962-01-01 Chile        893.172        893172
16 1958-01-01 Sweden       819.810        819810
17 1954-01-01 Switzerland  768.607        768607
18 1930-01-01 Uruguay      590.549        590549
19 1938-01-01 France       375.700        375700
20 1934-01-01 Italy        363.000        363000
>  
```

> Otra forma de solucionar el mismo problema es remover los puntos y luego transformalo en numero con las funciones `str_remove_all`, que remueve los caracteres indicados en todas las ocurrencias que aparecen y `as.numeric`, que transforma al tipo numerico.
>
>
 ``` r
 copas <- copas %>% 
  mutate(asistencia = as.numeric(str_remove_all(Attendance, fixed("."))))
```
>

## Goleadores.

Para estas preguntas vamos a usar el conjunto de datos de jugadores. Hay una columna llamada `Event` con anotaciones al estilo “G20” o “Y56” que significan: “Gol a los 20 minutos” y “Tarjeta amarilla a los 56 minutos”, respectivamente.  La columna puede tener ninguno (NA), uno o mas eventos por jugador.  En el caso que tenga mas de un evento se separan con un espacio, como se muestra en la fila siete de la siguiente figura. 

![](jugadores.png)



### Ordenar los jugadores por cantidad de goles

Para resolver este problema vamos a usar la funcion `str_extract` que extrae la primera ocurrencia de una cadena que cumple con un patron. En este caso el patron es una letra seguida de uno o mas digitos. 

``` r

```{r}

goleadores <- jugadores %>% 
  separate_longer_delim(Event, delim = " ")

```

```{r}

goleadores %>% 
  filter(str_detect(Event,"G")) %>% 
  group_by(`Player Name`) %>% 
  summarise(goles = n())
  
goleadores %>% 
  filter(str_detect(Event,"G")) %>% 
  count(`Player Name`) %>% 
  arrange(desc(n))

```

## Sacar los 10 jugadores mas importantes y realizar un grafico de barras

```{r}
Top10_gol <- goleadores %>% 
  filter(str_detect(Event,"G")) %>% 
  count(`Player Name`) %>% 
  arrange(desc(n)) %>% 
  top_n(10) 
```

```{r}
Top10_gol %>% 
  ggplot(aes(`Player Name`, n)) +
  geom_col()
```
