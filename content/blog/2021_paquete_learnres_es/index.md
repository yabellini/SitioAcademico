---
date: "2021-01-15"
draft: false
summary: Basado en learnr este paquete te presenta una serie de plantillas para tutoriales en español.
title: Learnres. Un paquete de plantillas para tutoriales en español
authors: Yanina Bellini Saibene
categories:
  - Education
  - Español
  - rstats
tags: 
  - Technical Tips
  - Packages
  - learnr
  - rstats
---


{{< figure src="/media/learnres_portada.png" alt="fabrica de paquetes">}}
<a href="http://www.freepik.com">Designed by pch.vector / Freepik</a>

El paquete `learnres` es un paquete open source con plantillas en español para generar tutoriales interactivos. Al día de hoy este paquete contiene dos plantillas para generar tutoriales con {learnr}:

- La misma plantilla que viene por defecto en `learnr`, pero traducida al español.

- Una segunda plantilla con una sugerencia de estructura y elementos que contribuyen a que el material pueda ser compartido, reutilizado y citado.

## Casos de uso

Pensamos que `learnres` se utilizará de varias formas.

### Generar un tutorial interactivo en español con ejercicios

* _Romina:_ conoce y enseña R en su cátedra en la universidad. Está familiarizada con RMarkdown, es parte de lo que enseña a sus estudiantes y uno de los formatos en los que comparte ejercicios resueltos. La cantidad de estudiantes de su materia le hace cada vez más difícil poder corregir todos los ejercicios de código así que está interesada en proporcionar feedback automatizados a la respuesta de los ejercicios de programación con R que dan en su materia.  Las plantillas con ejercicios de código y preguntas de opción múltiple pueden ayudarla a generar tutoriales interactivos.

### Generar un tutorial interactivo en español con elementos pedagógicos

* _Juan:_ es docente de adultos, tiene muchos cursos de un par de horas a varios días enseñando programación. En estos cursos ha utilizado tutoriales interactivos como requisito previo al inicio presencial del curso y como material de uso posterior.  Pone a disposición estos cursos para que más personas puedan aprovecharlo para aprender de forma individual.  Por eso le parece importante definir con cuidado que temas cubre cada tutorial, cual es la audiencia y que tipo uso se puede hacer del material.  La plantilla de `learnres` con secciones sugeridas le da estructura y la información de base necesaria para generar estos tutoriales.  Además está toda traducida al español.

### Llevar la ayuda de un paquete a otro nivel

* _Augusto:_ es investigador de INTA y como resultado de sus investigaciones a generado paquetes de R que están publicados en CRAN. Está familiarizado con RMarkdown. Sabe que en la nueva IDE de RStudio hay un panel de tutoriales donde se podría cargar la ayuda de su paquete en formato de tutorial y quiere explorar esta opción.  Todos sus paquetes y la ayuda están en español, asi que la plantilla _por defecto_ de learnr le resulta adecuada y `learnres` le ahorra el tiempo de traducción.

### Personalizar el diseño visual y el idioma del tutorial

* _Rene:_ trabaja en diseño gráfico, en una empresa de educación on-line sobre ciencia de datos ha generado varios tutoriales `learnr` como material de sus cursos. Los tutoriales se publican en la web y deben tener la identidad visual de la empresa, además debe tener en cuenta aspecto de accesibilidad y multilenguaje.  El paquete `learnres` tiene una plantilla CSS con cada elemento explicado y también un archivo `JSON` para la configuración del lenguaje lo que permite contribuye a realizar una personalización de forma más sencilla. 

## Instalación y uso

Para poder usar el paquete primero debes instalarlo, como aún no está en CRAN, debes instalar la versión de desarrollo desde GitHub, de esta manera:

``` r
  remotes::install_github("yabellini/learnres")
```

Necesitas el paquete `remotes`, si no lo tienes instalado, puedes hacerlo con esta función:

``` r
  install.packages("remotes")
```

### Como generar un tutorial usando las plantillas

Para generar un nuevo tutorial con las plantillas en español, luego de instalar el paquete y dentro de RStudio seleccionamos **File** -> **New File** -> **RMarkdown** -> **From Template** -> y allí seleccionamos que plantilla queremos utilizar

{{< figure src="/media/learnres_how_to.png" alt="fabrica de paquetes">}}


En [este post](https://learning-learnr.netlify.app/post/tutorialesconlearnr/) puedes encontrar indicaciones detalladas para usar las plantillas para generar un tutorial interactivo.


## Otras personalizaciones

### Diseño visual

También tiene una hoja CSS con los estilos explicados para que la puedas editar y generar los propios.  En [este post](https://learning-learnr.netlify.app/post/learnr_desing_css/) se explica como personalizar el diseño visual de nuestros tutoriales utilizando nuestra plantilla como ejemplo.

### Idioma

El paquete presenta un archivo `JSON` con todas las partes de la interfaz, como por ejemplo los botones de la caja para ejecutar código, traducidas al español.


¿Cómo lo usarías?, ¿te parece útil contar con estas plantillas?, ¿qué otras te gustaría generar?