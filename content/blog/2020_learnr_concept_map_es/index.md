---
date: "2020-10-26"
draft: false
type: page
linktitle: Un mapa conceptual sobre {learnr}
summary: En este mapa conceptual intento describir los componentes de un tutorial de learnr.
title: Un mapa conceptual sobre {learnr}
authors: 
    - yabellini
type: post
weight: 1
tags: 
    - Recursos
    - Mapas Conceptuales
    - Open Education
---
{{< figure src="/media/concept_map_learnr_post.jpg" alt="Esquema con estilo dibujado a mano de un mapa conceptual sobre tutoriales">}}
<a href="http://www.freepik.com">Designed by Freepik</a>

## Mapas conceptuales

En un [post anterior](https://learning-learnr.netlify.app/post/concept_maps/) hablamos sobre los [mapas conceptuales](https://teachtogether.tech/es/index.html#s:memory-concept-maps) y como representan un modelo mental del tema que se quiere enseñar. 

Como parte de las actividades de [LatinR](https://latin-r.com/) y en el marco de [MetaDocencia](https://www.metadocencia.org) desarrollamos un curso sobre {learnr} y generamos el mapa conceptual correspondiente (el cual agregamos a la [colección de mapas conceptuales](https://github.com/rstudio/concept-maps) de RStudio Education):


{{< figure src="/media/learnr-tutorial_concept_map.svg" alt="Mapa conceptual de un tutorial {learnr}">}}

## Descripción del mapa conceptual

El paquete {learnr} se basa en {rmarkdown} para generar los tutoriales, por eso el mapa dice que un documento **rmarkdown** puede ser un **tutorial**.  Ese documento contiene:

* **rmarkdown** que produce **texto con formato** incluido en el **documento**, 
* un encabezado **YAML** que es usado por **metadatos** y controla el formato y comportamiento del **documento**.
* y por supuesto, **código R** que puede estar **en línea** en el texto o bien en **chunks** de código.

Ese **código R** en los **chunks** genera diferentes tipos de **contenido** como **texto, tablas y gráficos** que se incluyen en el **documento**. El código puede o no ser visible en el documento; este mismo código puede o no ser ejecutado en el documento rmarkdown. En general no se ejecuta cuando el código es el objeto que queremos incluir y mostrar en el documento final.

En un tutorial de {learnr} los **chunks** pueden tener **nombre** y **parámetros** como en cualquier otro documento **rmarkdown**; la diferencia está en algunos nombres y parámetros especiales.

Si un **chunk** de código se marca con el parámetro _exercise = TRUE_ entonces este es un tipo especial de chunk que solo está presente en {learnr}: es un tipo **ejercicio**, que puede contener **código completo o incompleto** como ejemplo de lo que se desea enseñar o demostrar, puede tener **pistas** para ayudar en la resolución del ejercicio y **soluciones** que presenta una de las posibles soluciones válidas al ejercicio.  Los chunks de código de pistas y soluciones tienen nombres especiales que deben terminar con las palabras _-hint_ y _-solution_ respectivamente.  Estos ejercicios también pueden tener **comentarios (correcciones)** cada vez que se ejecuta una porción de código.

En un **chunk** de código también podemos utilizar las funciones de **preguntas**, que pueden ser de **opción múltiple** con respuestas excluyentes o no.  Las preguntas también pueden proveer **comentarios personalizados** con los cuales se puede guiar al estudiante en el entendimiento de los conceptos determinando que se ha entendido de forma errónea en caso que resuelva de forma incorrecta la pregunta.

Finalmente, el mapa conceptual relaciona el concepto de **documento**, que en nuestro caso es el tutorial, con la forma en que podemos distribuir o publicar el mismo: como **paquete** o como **sitio web**.

## En construcción

Este mapa es una primera aproximación describiendo los elementos más importantes de un tutorial de {learnr} como parte del universo {rmarkdown}. ¿Qué más le agregarías?, ¿Qué parte necesita más detalle?, ¿Cómo sería tu mapa conceptual de {learnr}?




