---
date: "2021-01-08"
draft: false
type: page
linktitle: Recursos para explorar y aprender learnr
summary: Lista de recursos para seguir aprendiendo learnr.
title: Recursos para explorar y aprender learnr
authors: 
    - yabellini
type: post
weight: 1
tags: 
    - Recursos
---
{{< figure src="/media/recursos.png" alt="Captura de pantallas de diferentes tutoriales learnr">}}
En este post les comparto una lista de materiales que me ayudaron a aprender sobre `learnr`.  Este listado se va actualizando en [este repositorio](https://github.com/yabellini/curso_learnr).


## Información oficial del paquete

RStudio generó un [sitio web](https://rstudio.github.io/learnr/) sobre `learnr` con contenido muy completo de todas las etapas del armado de un tutorial.  Además también está disponible el [repositorio con el código fuente del paquete](https://github.com/rstudio/learnr).

## Tutoriales

Los tutoriales construidos por otras personas fue uno de los primeros recursos que exploré para ver como y para qué se usaban estos tutoriales, van aquí mis favoritos.  Además comparten el código fuente y por ende podemos aprender como están hechas cada una de las herramientas que se usan en el tutorial.

* [RStudio Primers](https://rstudio.cloud/learn/primers): son una serie de tutoriales de RStudio generados para aprender conceptos básicos de ciencia de datos con los tutoriales interactivos.  Se agrupan en seis temas: conceptos básicos, trabajando con datos, visualizando datos, ordenando tus datos, iterando y escribiendo funciones.  Desde [este repositorio de github](https://github.com/rstudio-education/primers) se puede acceder a su código fuente.

* [Data Science in a box](https://datasciencebox.org/interactive-tutorials.html): serie de tutoriales del conocido curso de Mine Çetinkaya-Rundel.  Presenta 8 tutoriales que se pueden usar desde Shiny, instalarse como paquete y acceder a su código fuente. Los he ustilizado para aprender como usar el paquete `gradethis` junto con `learnr` para evaluar ejercicios de forma automática.

* [Teacups, Giraffes, & Statistics](https://tinystats.github.io/teacups-giraffes-and-statistics/index.html): una hermosa serie de módulos para aprender estadísticas y programación en R para estudiantes, científicas/os y entusiastas de las estadísticas.  En [este repo](https://github.com/tinystats/teacups-giraffes-and-statistics) se encuentra el código fuente.


## Blogpost

Este listado de blog post presentan de forma clara, paso a paso y ejemplos funcionales de diferentes partes del desarrollo de un tutorial de `learnr`, la mayoría están en Inglés.

### Utilizando learnr con gradethis

* [Data science tutorials with learnr and gradethis](http://www.citizen-statistician.org/2020/08/data-science-tutorials-with-learnr-and-gradethis/) por Lee Suddaby, Zeno Kujawa 

### Publicando tutoriales:

* [Delivering learnr tutorials in a package](https://education.rstudio.com/blog/2020/09/delivering-learnr-tutorials-in-a-package/) por Desirée De Leon

* [Getting a learnr tutorials to run on mybinder.org](http://laderast.github.io/2020/09/15/getting-learnr-tutorials-to-run-on-mybinder-org/) por Ted Laderas

* [Publishing learnr Tutorials on shinyapps.io](https://cran.r-project.org/web/packages/learnr/vignettes/shinyapps-publishing.html) por Angela Li

## Paquetes para usar con `learnr`

Hay paquetes que nos pueden ayudar a agregarle funcionalidades a nuestros tutoriales.

* [Gradethis](https://rstudio-education.github.io/gradethis/): proporciona varios métodos para calificar los ejercicios en un tutorial interactivo.

* [Parsons](https://rstudio.github.io/parsons/): permite crear problemas de Parsons personalizados para enseñar programación. 

* [Sortable](https://github.com/rstudio/sortable): agrega la posibilidad de hacer drag and drop a los tutoriales y permite clasificar preguntas con arrastrar y soltar.

* [glosario](https://github.com/carpentries/glosario-r): permite a los usuarios crear y recuperar glosarios multilingües y se pueden agregar como links a las definiciones dentro de los tutoriales.

* [Flash Cards](https://github.com/jienagu/flashCard): crear tarjetas de memoria para Shiny a partir de un set de datos.

* [DiagrammeR](https://rich-iannone.github.io/DiagrammeR/): permite compilar texto en diagramas.  En [este post explico como usarlo.](https://learning-learnr.netlify.app/post/concept_maps/)

* [learnres](https://github.com/yabellini/learnres): paquete de plantillas en español para armar tutoriales interactivos

Espero que este listado de materiales te resulten tan útiles como a mi, ¿tenés alguno que no está listado aquí?, compartilo en los comentarios.