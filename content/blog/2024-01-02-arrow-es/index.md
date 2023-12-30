---
date: "2024-01-02"
draft: false
summary: 
title: "Usando Apache Arrow para analizar el padron electoral argentino del 2011"
authors: []
categories:
  - Español
  - Data Science
  - Apache Arrow
  - 100DaysToOffload
tags: 
  - 100DaysToOffload
  - rstats
---

En 2020 volvi a dar clases en la Universidad. Una de las materias era sobre datos masivos y no estructurados para una diplomatura en ciencia de datos aplicada a politicas publicas.  En 2021, Danielle Navarro fue una de las keynote de LatinR y nos presento Apache Arrow y como usarlo en R. Luego de esa keynote cambie mi clase sobre manejo de grandes datos e incorpore Apache Arrow como parte de la materia.

En mis clases siempre incorporo programacion en vivo, y para esta clase adapte los ejemplos de la charla de Danielle a un conjunto de datos de Argentina. Todos los ejemplos de clase los hice con un conjunto de datos del padron electoral argentino del 2011 al que tuve acceso por ser parte de Open Data Cordoba. No puedo publicarlo ni compartirlo, pero espero que este blog post sea un lindo ejemplo en castellano del paquete y como se usa. 


## Algunos conceptos sobre Arrow

Apache Arrow es un conjunto de herramientas multilenguaje para el intercambio rapido de datos y procesamiento en memoria. Arrow provee un formato estándar para conectar diferentes lenguajes y sistemas. Hay un tipo de archivos llamado _parquet_ que se utiliza con Arrow y optimiza la lectura y escritura de los datos.

Los datos tabulares se almacenen como columnas representando variables y conteniendo datos similares, por ejemplo, si hablamos del padron electoral tendremos una columna con el documento nacional de identidad de las personas, otra con su nombre y otra con su apellido. Cada fila de ese conjunto de datos representa un caso, una persona, pero los datos son disimiles, ya que por cada persona tendremos el DNI, el nombre, el apellido, la fecha de nacimiento, la provincia donde vive, etc.  La representacion en memoria de estos datos tabulares por fila hace que los datos adyacentes en memoria sean disímiles. Arrow cambia esa forma de representacion a un formato por columna haciendo que los datos adyacentes en memoria sean similares.

Vamos a ver las diferencias de velocidad en la lectura de datos con diferentes formatos leyendo un dataset de mas de 26 millones de filas.

## Un poco de codigo

### Leyendo y escribiendo datos con Arrow

Vamos a usar tidyverse para analizar los tiempos de lectura y tambien para analizar los datos posteriormente. Arrow porque es el paquete que vamos a aprender a usar y tictoc que nos permite calcular el tiempo que tarda en ejecutarse cada porcion de codigo. 

``` r
library(tidyverse) 
library(arrow) 
library(tictoc)
```

#### Leer un CSV con read_csv

Ahora vamos a leer el archivo separado por comas CSV con la clasica funcion read_csv.  Usamos tictoc para calcular el tiempo que tarda la ejecucion y glimpse() para tener una idea del conjunto de datos (edite el resultados del DNI para ocultar el dato completo).

La lectura de las 26.694.811 filas y 8 columnas se realizo en **20.7** segundos.

``` r

tic()
padron_2011 <- read_csv("clase9_data/padron-2011.csv",
                        locale = locale(encoding = "ISO-8859-1")) %>%
  glimpse()
toc()

Rows: 26,694,811
Columns: 8
$ provincia      <dbl> 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17…
$ documento      <dbl> 1194..., 723..., 176..., 22..., 354...., 297...., 2131..., 1448....., 3397....., 20....., 1878...., 175....., 2535034…
$ nacimiento     <dbl> 1955, 1934, 1966, 0, 0, 0, 0, 0, 1989, 1968, 0, 1966, 1976, 0, 1967, 0, 1949, 1980, 0, 0, 0, 0, 0, 0, 0, 0, 1938, 0, 0, 0, 0, …
$ nombre         <chr> "FRANKLIN JESUS", "GABRIEL", "GABRIEL ROQUE", "MARIA ARACELI", "ANA LAURA", "ANDREA LORENA", "MONICA MARCELA", "GRACIELA ELIZA…
$ apellido       <chr> "ABALOS", "ABALOS", "ABALOS", "ABALOS", "ABAN", "ABAN", "ABAN CABRERA", "ABAN", "ABAN", "ABAN", "ABBOUDI", "ABDENUR", "ABELEND…
$ ocupacion      <chr> "ESTUD", "ESTUD", "EMPL", "ESTUD", "ESTUD", "ESTUD", "DOCENTE", "ESTUD", "ESTUD", "ESTUD", "A/C", "ABOG", "MEDICO", "ESTUD", "…
$ tipo_documento <chr> "DNI", "L", "DNI-EA", "DNI", "DNI", "DNI", "DNI", "DNID", "DNI", "DNID", "DNI", "DNID", "DNI-EA", "DNI", "DNI", "DNIC", "L", "…
$ sexo           <chr> "M", "M", "M", "F", "F", "F", "F", "F", "M", "M", "F", "M", "M", "F", "M", "F", "M", "M", "F", "F", "F", "F", "F", "F", "F", "…

20.7 sec elapsed
```

#### Leer el mismo CSV con Arrow

Ahora leemos el mismo archivo pero usamos la funcion read_csv_arrow.  En esta ocasion el tiempo empleado en la lectura fue de **15.327** segundos. Cinco segundos menos que la funcion anterior. 

``` r 
tic()
padron_2011_arrow<- read_csv_arrow("clase9_data/padron-2011.csv",
                                   read_options = csv_read_options(encoding = "ISO-8859-1")) %>%
  glimpse()
toc()

Rows: 26,694,811
Columns: 8
$ provincia      <int> 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17…
$ documento      <int> 119..., 723..., 176..., 221..., 35..., 297..., 21...., 14...., 33...., 20..., 187..., 17...., 25...…
$ nacimiento     <int> 1955, 1934, 1966, 0, 0, 0, 0, 0, 1989, 1968, 0, 1966, 1976, 0, 1967, 0, 1949, 1980, 0, 0, 0, 0, 0, 0, 0, 0, 1938, 0, 0, 0, 0, …
$ nombre         <chr> "FRANKLIN JESUS", "GABRIEL", "GABRIEL ROQUE", "MARIA ARACELI", "ANA LAURA", "ANDREA LORENA", "MONICA MARCELA", "GRACIELA ELIZA…
$ apellido       <chr> "ABALOS", "ABALOS", "ABALOS", "ABALOS", "ABAN", "ABAN", "ABAN CABRERA", "ABAN", "ABAN", "ABAN", "ABBOUDI", "ABDENUR", "ABELEND…
$ ocupacion      <chr> "ESTUD", "ESTUD", "EMPL", "ESTUD", "ESTUD", "ESTUD", "DOCENTE", "ESTUD", "ESTUD", "ESTUD", "A/C", "ABOG", "MEDICO", "ESTUD", "…
$ tipo_documento <chr> "DNI", "L", "DNI-EA", "DNI", "DNI", "DNI", "DNI", "DNID", "DNI", "DNID", "DNI", "DNID", "DNI-EA", "DNI", "DNI", "DNIC", "L", "…
$ sexo           <chr> "M", "M", "M", "F", "F", "F", "F", "F", "M", "M", "F", "M", "M", "F", "M", "F", "M", "M", "F", "F", "F", "F", "F", "F", "F", "…

15.327 sec elapsed
```

#### Ahora leemos el mismo CSV con Arrow y con el formato de Arrow

Ahora ademas de leer con la funcion de Arrow le indicamos que utilice el formato de Arrow con el parametro _as_data_frame = FALSE_. La lectura tomo 7.263 segundos en esta oportunidad.  Ocho segundos menos que la opcion anterior y 13 segundos menos que _read_csv()_.  

``` r

tic()
padron_2011_arrow <- read_csv_arrow("clase9_data/padron-2011.csv",
                                    read_options = csv_read_options(encoding = "ISO-8859-1"), 
                                    as_data_frame = FALSE) %>%
  glimpse()
toc()

Table
26,694,811 rows x 8 columns
$ provincia       <int64> 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 1…
$ documento       <int64> 11..., 72..., 17..., 2..., 35..., 29..., 21..., 14..., 33..., 2..., 18..., 1..., 2...…
$ nacimiento      <int64> 1955, 1934, 1966, 0, 0, 0, 0, 0, 1989, 1968, 0, 1966, 1976, 0, 1967, 0, 1949, 1980, 0, 0, 0, 0, 0, 0, 0, 0, 1938, 0, 0, 0, 0,…
$ nombre         <string> "FRANKLIN JESUS", "GABRIEL", "GABRIEL ROQUE", "MARIA ARACELI", "ANA LAURA", "ANDREA LORENA", "MONICA MARCELA", "GRACIELA ELIZ…
$ apellido       <string> "ABALOS", "ABALOS", "ABALOS", "ABALOS", "ABAN", "ABAN", "ABAN CABRERA", "ABAN", "ABAN", "ABAN", "ABBOUDI", "ABDENUR", "ABELEN…
$ ocupacion      <string> "ESTUD", "ESTUD", "EMPL", "ESTUD", "ESTUD", "ESTUD", "DOCENTE", "ESTUD", "ESTUD", "ESTUD", "A/C", "ABOG", "MEDICO", "ESTUD", …
$ tipo_documento <string> "DNI", "L", "DNI-EA", "DNI", "DNI", "DNI", "DNI", "DNID", "DNI", "DNID", "DNI", "DNID", "DNI-EA", "DNI", "DNI", "DNIC", "L", …
$ sexo           <string> "M", "M", "M", "F", "F", "F", "F", "F", "M", "M", "F", "M", "M", "F", "M", "F", "M", "M", "F", "F", "F", "F", "F", "F", "F", …

7.263 sec elapsed

```

#### Guardar los datos con el formato parquet

``` r
padron_2011_arrow %>%
  write_dataset(path = "clase9_data/padron-2011", format = "parquet")
```

Luego de ejecutar este codigo mostrar que se genera una carpeta que contiene el archivo


#### Leer los datos desde un archivo parquet a un dataframe

``` r
tic()
padron_2011_parquet <- read_parquet("clase9_data/padron-2011/part-0.parquet") %>%
  glimpse()
toc()

Rows: 26,694,811
Columns: 8
$ provincia      <int> 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17…
$ documento      <int> 11..., 72..., 17..., 22..., 35..., 29..., 21...., 14...., 33..., 20..., 18..., 17..., 25....…
$ nacimiento     <int> 1955, 1934, 1966, 0, 0, 0, 0, 0, 1989, 1968, 0, 1966, 1976, 0, 1967, 0, 1949, 1980, 0, 0, 0, 0, 0, 0, 0, 0, 1938, 0, 0, 0, 0, …
$ nombre         <chr> "FRANKLIN JESUS", "GABRIEL", "GABRIEL ROQUE", "MARIA ARACELI", "ANA LAURA", "ANDREA LORENA", "MONICA MARCELA", "GRACIELA ELIZA…
$ apellido       <chr> "ABALOS", "ABALOS", "ABALOS", "ABALOS", "ABAN", "ABAN", "ABAN CABRERA", "ABAN", "ABAN", "ABAN", "ABBOUDI", "ABDENUR", "ABELEND…
$ ocupacion      <chr> "ESTUD", "ESTUD", "EMPL", "ESTUD", "ESTUD", "ESTUD", "DOCENTE", "ESTUD", "ESTUD", "ESTUD", "A/C", "ABOG", "MEDICO", "ESTUD", "…
$ tipo_documento <chr> "DNI", "L", "DNI-EA", "DNI", "DNI", "DNI", "DNI", "DNID", "DNI", "DNID", "DNI", "DNID", "DNI-EA", "DNI", "DNI", "DNIC", "L", "…
$ sexo           <chr> "M", "M", "M", "F", "F", "F", "F", "F", "M", "M", "F", "M", "M", "F", "M", "F", "M", "M", "F", "F", "F", "F", "F", "F", "F", "…

1.292 sec elapsed
```

#### Leer el formato parquet a una tabla Arrow

``` r
tic()
padron_2011_parquet <- read_parquet("clase9_data/padron-2011/part-0.parquet", as_data_frame = FALSE) %>%
  glimpse()
toc()

Rows: 26,694,811
Columns: 8
$ provincia      <int> 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17…
$ documento      <int> 11..., 72..., 17..., 22..., 35..., 29..., 21...., 14...., 33..., 20..., 18..., 17..., 25....…
$ nacimiento     <int> 1955, 1934, 1966, 0, 0, 0, 0, 0, 1989, 1968, 0, 1966, 1976, 0, 1967, 0, 1949, 1980, 0, 0, 0, 0, 0, 0, 0, 0, 1938, 0, 0, 0, 0, …
$ nombre         <chr> "FRANKLIN JESUS", "GABRIEL", "GABRIEL ROQUE", "MARIA ARACELI", "ANA LAURA", "ANDREA LORENA", "MONICA MARCELA", "GRACIELA ELIZA…
$ apellido       <chr> "ABALOS", "ABALOS", "ABALOS", "ABALOS", "ABAN", "ABAN", "ABAN CABRERA", "ABAN", "ABAN", "ABAN", "ABBOUDI", "ABDENUR", "ABELEND…
$ ocupacion      <chr> "ESTUD", "ESTUD", "EMPL", "ESTUD", "ESTUD", "ESTUD", "DOCENTE", "ESTUD", "ESTUD", "ESTUD", "A/C", "ABOG", "MEDICO", "ESTUD", "…
$ tipo_documento <chr> "DNI", "L", "DNI-EA", "DNI", "DNI", "DNI", "DNI", "DNID", "DNI", "DNID", "DNI", "DNID", "DNI-EA", "DNI", "DNI", "DNIC", "L", "…
$ sexo           <chr> "M", "M", "M", "F", "F", "F", "F", "F", "M", "M", "F", "M", "M", "F", "M", "F", "M", "M", "F", "F", "F", "F", "F", "F", "F", "…

1.184 sec elapsed
```

### Analizando datos

Ahora vamos a utilizar dplyr sintaxis para analizar los datos

#### Ver cuales son los nombres mas usados

Usamos count para ver cuales son los nombres mas usados. Vemos los primeros 10.  Se puede jugar buscando el nombre de los estudiantes.

```r
nombre <- padron_2011 %>% 
  count(nombre)
  
View(nombre)

1 JUAN CARLOS 181835
2 MIGUEL ANGEL 154287
3 CARLOS ALBERTO 117332
4 JOSE LUIS 99595
5 ANA MARIA 95920
6 MARIA CRISTINA 76394
7 LUIS ALBERTO 73048
8 MARIA DEL CARMEN 65597
9 STELLA MARIS 54061
10 JUAN JOSE 53647

```

#### Analizar las ocupaciones por provincia

Ademas de filtrar se puede almacenar los resultados en un dataset y analizar todos los resultados.  Es interesante que hay muchos oficios detallados pero no tantas profesiones universitarias. 

``` r

padron_2011 %>%
  filter(provincia == 11) %>% 
  count(ocupacion)

1 A.DE C 45383
2 ESTUD. 44341
3 EMPL. 31665

```

#### Analizar otras caracteristicas

Aqui se pregunta a les estudiantes que les gustaria analizar y se generan consultas de acuerdo a sus propuestas.
algunas ideas que surgen:

* Mujeres y varones por provincia
* El apellido mas comun
* Cuanto dato faltante hay
* El nombre mas comun de varon y de mujer
* Grafico de cantidad de votantes por fecha de nacimiento
* Tipos de documentos diferentes

Discusiones sobre limpieza de datos, por ejemplo de la ocupacion para que los agrupamientos y calculos sean mas exactos.

