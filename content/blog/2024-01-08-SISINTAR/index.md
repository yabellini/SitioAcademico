---
title: SisINTAR. Un paquete para gestionar datos de perfiles de suelos de Argentina
author: Elio Campitelli, Paola Corrales, Marcos Angelini, Dario Rodriguez, Yanina Bellini Saibene
summary: "El Instituto Nacional de Tecnología Agropecuaria (INTA) de Argentina desarrolla y mantiene  SISINTA (Sistema de Información de Suelos del INTA), un sistema de información y de bases de datos para gestionar información de suelos. Almacena específicamente datos de perfiles de suelo con sus datos de campo y laboratorio, así como la ubicación en diferentes sistemas de coordenadas. También permite búsquedas por atributos y ubicación, así como la descarga de los datos. El paquete SISINTAR fue desarrollado para permitir el acceso, lectura y manipulación de datos de perfiles de suelo de SISINTA de forma programática, utilizando estándares en el procesamiento, visualización y representación de información de suelos y desde el entorno R, uno de los más utilizados en la institución."
date: '2024-01-08'
categories:
  - Spanish
  - Open Data
  - Open Science
  - AgTech
  - 100DaysToOffload
tags:
  - Spanish
  - Open Data
  - Open Science
  - AgTech
  - 100DaysToOffload
  - rstats
---

{{< figure src="featured.jpeg" alt="Mapa de Argentina mostrando difernetes tipos de suelos. Molisoles, Entisoles, Arisisoles son los tres mas presentes.">}}

> Mapa de suelos de Argentina realizado por el INTA.

El Instituto Nacional de Tecnología Agropecuaria (INTA) de Argentina desarrolla y mantiene  SISINTA (Sistema de Información de Suelos del INTA), un sistema de información y de bases de datos para gestionar información de suelos. Almacena específicamente datos de perfiles de suelo con sus datos de campo y laboratorio, así como la ubicación en diferentes sistemas de coordenadas. También permite búsquedas por atributos y ubicación, así como la descarga de los datos. El [paquete SISINTAR](https://github.com/INTA-Suelos/SISINTAR) fue desarrollado para permitir el acceso, lectura y manipulación de datos de perfiles de suelo de SISINTA de forma programática, utilizando estándares en el procesamiento, visualización y representación de información de suelos y desde el entorno R, uno de los más utilizados en la institución.

## El paquete sisintar

El paquete presenta una serie de funciones para acceder a los datos de suelos y luego procesarlos. Actualmente el paquete cuenta con datos de más de 5877 suelos y la opción de descargar perfiles adicionales desde la plataforma SISINTA, inclusive los privados que requieren autenticación. Los perfiles privados son aquellos que están aún en el proceso de curado de datos y por eso aún no están disponibles para su uso público. Esta información de suelos es de suma importancia para modelado y mapeo de variables específicas de suelos.

Para conocer los datos disponibles en sisintar, la función `buscar_perfiles()` permite buscar perfiles en función de la localización, la fecha y la clase o, si se corre sin argumentos, devolver la lista de todos los perfiles disponibles en el paquete..

Para acceder a los datos de los perfiles se usa la función `get_perfiles()`. Ésta toma un vector con los ids de los perfiles de interés. 

``` r
get_perfiles(c(6653, 6347, 6580)) |> 
  subset(select = 1:5) |> 
  head(10)
#>       no_registro eq_humedad sum_bases   cic ph_pasta
#> 23652       21711         NA      5.93 19.73       NA
#> 23653       21712         NA      5.82 18.22       NA
#> 23654          NA         NA        NA    NA       NA
#> 22537          NA         NA        NA    NA       NA
#> 22538          NA         NA        NA 15.84       NA
#> 22539          NA         NA        NA 15.07       NA
#> 22540          NA         NA        NA 16.10       NA
#> 22541          NA         NA        NA    NA       NA
#> 23390       21687         NA      1.49 20.89       NA
#> 23391       21688         NA      1.24 18.34       NA

```

La función guarda los datos en un directorio y luego los lee preferentemente desde esa ubicación y por defecto utiliza los datos incluidos en el paquete. De esta manera, el resultado es reproducible ya que sólo depende de la versión del paquete, no requiere conexión de internet ni falla si el servicio SISINTA cambia su API o no se encuentra disponible. Un argumento opcional permite forzar la descarga de los datos desde SISINTA para obtener perfiles nuevos o datos corregidos que no estén incluidos en la versión del paquete instalada.  

La función `interpolar_perfiles()` permite interpolar perfiles de suelo utilizando distintos métodos. El paquete implementa el método de promedios ponderados y de splines, pero en su interfaz permite que cualquier persona implemente métodos nuevos. 

Para aprovechar las funcionalidades del paquete aqp, es posible convertir un perfil a un objeto `SoilProfileColection`. Finalmente, dado que el público usuario de estos datos también utiliza excel, se implementó la función `exportar_excel()`. 

Tanto las funciones como la documentación del paquete se realizaron en español, ya que la audiencia objetivo del paquete habla mayormente este idioma. El paquete fue pensado en primera instancia para un uso interno institucional por investigadores que necesitan datos de suelos para sus proyectos. Pero se realizó como un software libre, con el objetivo que sea también aprovechado por científiques de otras instituciones, por desarrolladores de software del ámbito público y privado y por productores o asesores del sector agropecuario.

## Aplicacion Shiny

Si bien el foco está en el acceso y manipulación programática de los datos, también se tuvo en cuenta que las personas que usan estos datos pueden no estar familiarizadas con R, de modo que también desarrollamos una interfaz gráfica con Shiny, accesible desde https://sisinta.shinyapps.io/sisintar-web/. 

La misma permite seleccionar los perfiles a descargar en base a su ubicación geográfica y disponibilidad temporal así como seleccionar las variables a descargar y un paso opcional de interpolación. Los datos luego se pueden descargar en formato csv o excel.
