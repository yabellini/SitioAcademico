---
date: "2020-10-24"
draft: false
linktitle: Mapas conceptuales en un tutorial interactivo
summary: Qué son los mapas conceptuales, como podemos utilizarlos para enseñar y como agregarlos a un tutorial de learnr.
title: Mapas conceptuales en un tutorial interactivo
authors: Yanina Bellini Saibene
categories:
  - Education
  - Español
  - rstats
tags: 
  - Concept Maps
  - Open Education
  - rstats
  - Technical tips
---
{{< figure src="featured.jpg" alt="esquemas de dos mapas conceptuales vacios">}}
<a href="http://www.freepik.com">Designed by Freepik</a>

## ¿Qué es un mapa conceptual?

Los [mapas conceptuales](https://teachtogether.tech/es/index.html#s:memory-concept-maps) representan un modelo mental del tema que se quiere enseñar. Ayudan a las y los docentes a describir lo que quieren enseñar, brindan a otras y otros instructores una descripción general rápida de una lección y permiten a las y los estudiantes verificar que han construido el modelo mental correcto.

Un mapa conceptual está compuesto por dos componentes principales: los conceptos que queremos enseñar (en general se los nombra usando sustantivos) y las relaciones entre esos conceptos (en general se los nombra con verbos).

El siguiente ejemplo es un mapa conceptual sobre **RMarkdown** realizado por _Yanina Bellini Saibene, Gabriela Sandoval, Florencia D'Andrea y Mónica Alonso_:

{{< figure src="/img/rmarkdown_concept_map.svg" alt="Mapa conceptual de RMarkdown">}}

## Usos de un mapa conceptual

Los mapas conceptuales pueden usarse para construir una lección ya sea por tu cuenta o con tus colegas.  El desarrollo del mapa conceptual permitirá ponerse de acuerdo con los conceptos y las relaciones que estos tienen y decidir que temas entran en el curso, cuales no y quien puede enseñar cada uno.  Con el mapa conceptual terminado también se puede analizar cuantos conceptos debemos enseñar y organizar las lecciones para introducir los conceptos necesarios de una manera que nos permita bajar la carga cognitiva de los estudiantes.

Los mapas también pueden ser utilizados como una herramienta de evaluación, por ejemplo: 

* presentar un mapa conceptual incompleto y pedir a los estudiantes que lo terminen: por ejemplo sin relaciones, relaciones sin nombre o sin presencia de conceptos importantes.

* pedir a las y los estudiantes que generen un mapa conceptual propio.

* pedir a las y los estudiantes que comparen su mapa conceptual con el mapa del docente.

## Agregando un mapa conceptual a un tutorial interactivo

Hay al menos dos maneras de agregar un mapa conceptual a nuestros tutoriales

* Agregar una imágen con el mapa.
* Generar un diagrama con el paquete `DiagrammeR`.

### Agregar una imágen

Los mapas conceptuales se pueden generar con herramientas como editores de diapositivas (PowerPoint, Google Slides, etc.) o programas para dibujar diagramas como [diagrams.net](https://www.diagrams.net/) que se puede usar online o se puede descargar para usarlo sin conexión.

Sin importar la herramienta que usemos, eventualmente, tendremos una imágen (.png, .jpg, .svn) con nuestro mapa conceptual para agregar a nuestro tutorial.  El código para hacer esto es el siguiente:

````{r}
```{r, echo=FALSE, out.width="100%", fig.align = "center"}
knitr::include_graphics("images/mapa_conpceptual.png")  
```
````
Este código agrega el mapa conceptual al tutorial de esta manera:
{{< figure src="/img/learnr_conceptmap_ggplot.png" alt="Captura de pantalla del tutorial con el mapa conceptual">}}

Antes de ponerte a generar tus mapas conceptuales desde cero, te recomiendo que revises el [listado de mapas conceptuales generados](https://github.com/rstudio/concept-maps) por el equipo de RStudio Education y sus instructores certificados. Su licencia de uso es [CC-BY](https://creativecommons.org/licenses/by/4.0/legalcode.es) y en la carpeta 'es' están las versiones traducidas al español.

También podés revisar mi repositorio con [mapas conceptuales](https://github.com/yabellini/concept_maps) de algunas de mis lecciones y cursos.  La licencia también es CC-BY y en la carpeta _'es'_ están las versiones en español.

### Generar un diagrama con el paquete `DiagrammeR`

[DiagrammeR](https://rich-iannone.github.io/DiagrammeR/) es un paquete que permite compilar texto en diagramas.  Su sintaxis es muy amplia, dependiendo del tipo de diagrama que querramos generar. Vamos a ver un ejemplo: 

* Los _conceptos_ que van dentro de los recuadros se escriben entre corchetes **[]**.  Se puede dar un nombre a este nodo del diagrama para poder referenciar al mismo cuando se deban generar relaciones.  En el código de ejemplo: _A[Gráficos]_ genera un rectángulo, llamado _A_, que en su interior contiene la palabra _“Gráficos”_. La _A_ no se muestra en la visualización.

* Las relaciones se expresan con una flecha compuesta por dos guiones y un signo mayor: **-->**. Para asignarles un texto, se escribe dicho texto después de la flecha encerrado entre pipes **|**. Por ejemplo: **-->|tienen|** genera una flecha con el texto _tienen_.

* Para completar la relación se debe indicar el nodo de origen y de destino. Estos nodos se invocan con el nombre que les dimos al crearlos: por ejemplo _A_, para referirse al rectángulo con la palabra _“Graficos”_.

El siguiente código de ejemplo genera el diagrama del tutorial de gráficos que encontramos al comienzo de este post.

````{r}
```{r echo=FALSE}
DiagrammeR("
graph LR;
  A[Gráficos] -->|tienen| B[Gramática];
  A -->|tipo| C[Barra];
  A -->|tipo| D[Puntos];
  A -->|tipo| E[Lineas];
  A -->|tipo| L[Areas];
  B -->|son| F[Reglas];
  B -->|compuesta por| G[Variables de datos];
  B -->|compuesta por| H[Atributos estéticos];
  B -->|compuesta por| I[Objetos Geométricos];
  F -->|combinan| J[capas]
  K[ggplot2] -->|implementa| B
")

```
````
### Consideraciones finales

Cualquiera sea la herramienta que seleccionemos para generar y agregar nuestros mapas, es una herramienta interesante para ordenar y compartir mapas mentales de nuestras lecciones.

Y si generas algunos mapas conceptuales, compartilos (aún mejor, contribuí a la colección de mapas conceptuales que ya existen), seguro todas y todos vamos a aprender y a aprovecharlos.