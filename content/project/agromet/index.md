---
title: "AgroMet Package"
subtitle: ""
excerpt: "The {agromet} package includes a series of functions to calculate climatic and hydrological indices and statistics from tidy data."
date: 2019-07-02
author: "Yanina Bellini Saibene"
featured: true
draft: false
tags:
  - package
  - Español
categories:
  - R
  - package
# layout options: single or single-sidebar
layout: single
links:
- icon: github
  icon_pack: fab
  name: code
  url: https://github.com/AgRoMeteorologiaINTA/agromet
#- icon: newspaper
#  icon_pack: far
#  name: Blog post
#  url: https://education.rstudio.com/blog/2020/07/palmerpenguins-cran/
---

## English

## Package agromet

<img src='featured.jpg' align="right" height="200" alt='Hex sticker of the package. Shows a rainf of 0 and 1 and a field with the word AgroMet.'/>

The {agromet} package includes a series of functions to calculate climatic and hydrological indices and statistics from tidy data, including a function for plotting geo-referenced results and cartographic information. 

For example `thresholds()` allows to count the number of observations that meet a certain condition and `average_days()` returns the first and last day of the average year of occurrence of an event.

Other functions such as `spi()` function as function wrappers for other packages and seek to be compatible with the handling of tidy data.

Finally, the package includes a `map()` georeferenced data graphing function with INTA's own style and logo.

## Español

## Paquete agromet

<img src='featured.jpg' align="right" height="200" alt='Hex sticker of the package. Shows a rainf of 0 and 1 and a field with the word AgroMet.'/>


El paquete {agromet} incluye una serie de funciones para calcular índices y estadísticos climáticos e hidrológicos a partir de datos tidy, incluyendo una función para trazar resultados georreferenciados e información cartográfica. 

Por ejemplo `umbrales()` permite contar la cantidad de observaciones que cumplen una determinada condición y `dias_promedios()` devuelve el primer y último día del año promedio de ocurrencia de un evento.

Otras funciones como `spi()` funcionan como wrappers de funciones de otros paquetes y que buscan ser compatibles con el manejo de datos tidy.

Finalmente el paquete incluye una función de graficado de datos georeferenciados `mapear()` con el estilo y logo propios de INTA.
