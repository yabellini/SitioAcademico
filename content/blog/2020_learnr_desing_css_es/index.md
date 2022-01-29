---
date: "2020-11-24"
draft: false
linktitle: Cambiando el diseño visual de los tutoriales
summary: Ejemplo de una plantilla CSS explicando como cambiar fuentes y colores de los elementos de un tutorial .
title: Cambiando el diseño visual de los tutoriales
authors: Yanina Bellini Saibene
categories:
  - Education
  - Español
tags: 
  - R
  - Technical tips
  - CSS
---

{{< figure src="/media/css_post.jpg" alt="grupo de personas diseñando">}}
<a href="http://www.freepik.com">Designed by vectorjuice / Freepik</a>

## Personalizando nuestros tutoriales

Los tutoriales generados con learnr terminan generando un archivo HTML (siglas en inglés de _Hiper Text Markup Language_), por lo que podemos cambiar su estilo utilizando _CSS_ (siglas en inglés de _Cascading Style Sheets_), en español _Hojas de estilo en cascada_.

CSS está diseñado para separar el contenido del formato de presentación en un documento HTML. El formato de presentación incluye, entre otros elementos, los botones, los menús, las tablas y permite configurar aspectos como que fuente, color y tamaño tendrá cada elemento.  En la figura vemos el estilo por defecto con el que cuentan los tutoriales de `learnr`.

{{< figure src="/media/css_default.png" alt="Elementos de un tutorial learnr y su estilo por defecto">}}

Creando un archivo `.css` podemos personalizar todos los elementos de nuestro tutorial.

## Los elementos de un CSS

En CSS, existen _selectores_ que se utilizan para hacer referencua a los elementos HTML en las páginas web que queremos diseñar. Hay una muy amplia variedad de selectores de CSS  que permiten un diseño detallado con una precisión muy fina.

En este post veremos los selectores y las propiedades principales para personalizar el diseño de nuestros tutoriales.

### Elementos principales

El siguiente código define la fuente y el tamaño de la letra para el cuerpo (`body`) del tutorial.  El tamaño y tipo de letra está de acuerdo a las sugerencias de accesibilidad realizadas por MetaDocencia. [Acceder al post](https://www.metadocencia.org/post/accesibilidad_1/)

```{css, eval=FALSE}
body {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 14;
}
```
Los siguientes elementos configuran los títulos, `h1` es el título, es el encabezado que en rmarkdown configuramos con un numeral (#), `h2` corresponde a un subtítulo (dos numerales) y así hasta el encabezado de quinto nivel (`h5`).  En el caso de `h1` y `h2` definimos un color para la fuente (`color`), un color de fondo (`background-color`) y un espacio alrededor del título (`padding`). 

```{css, eval=FALSE}
h1, h2 {
  color: #C83737;
  background-color: #f7f7f7;
  padding: .5em;
}

h3, h4, h5{
  color: #C83737;
}
```
Asi se ven los cambios que realiza este css en la plantilla.  Cambia el color y tamaños del texto de la fuente y del fondo de los encabezados y del título:

{{< figure src="/media/css_cambios_body_encabezados.png" alt="Elementos de un tutorial learnr y su estilo en títulos y encabezados cambiado">}}

Este código configura la apariencia de los links, el selector `a:hover` hace referencia a la apariencia del link cuando estamos _arriba_ del link, queda del mismo color pero agrega el subrayado.  

```{css, eval=FALSE}
a {
    color: #C83737;
    text-decoration: none;
}

a:hover {
    color: #C83737;
}

```
Si no configuramos ese selector, entonces cuando estemos arriba del link cambiará a un color celeste con el subrayado.  En la figura se muestra la diferencia:

{{< figure src="/media/css_cambios_links.png" alt="Diferente aspecto en color de un link">}}

### Botones

Los tutoriales presentan varios botones, por ejemplo: `Continue` que separa los temas; `Submit Answer` y `Try Again` en las preguntas; `Run Code` y `Hints` en los ejercicios.

Para cambiar su apariencia es necesario especificar las propiedades de los botones en general y luego de acuerdo al estado y acciones sobre esos botones (`.btn:hover, .btn:active, .btn:disabled`), como se muestra en el siguiente código:

```{css, eval=FALSE}
.btn {
  background-color: #C83737;
  color: #fff;
}

.btn-default {
    color: #ffffff;
    background-color: #C83737;
    border: none;
}

.btn-light {
  background-color: #aa2f2f;
  color: #fff;
}

.btn-primary , .btn-success, .btn-info{
  background-color: #C83737;
  color: #fff;
}

.btn:hover, .btn:active, .btn:disabled {
  background-color: #aa2f2f;
  color: #fff;
}
```

{{< figure src="/media/css_botones.png" alt="Diferente aspecto en color de los botones en diferentes estados">}}


### Código

En la plantilla por defecto el código cambia de fuente y tiene un fondo gris, aqui nosotros cambiamos el tamaño y color de la fuente y el color de fondo del texto.

```{css, eval=FALSE}
code {
    color: #C83737;
    background-color:  #f7f7f7;
    font-size: 14px;
}
```

## Tabla de contenidos 

Finalmente vamos a configurar la tabla de contenidos del tutorial.  Con esto cambiamos los colores del texto de los temas, del fondo y como se comportan cuando se seleccionan o se pasa por "arriba".

```{css, eval=FALSE}
.topicsList {
  padding: .5em;
}

.topicsHeader {
  background-color: #f7f7f7;
  color: #2b2b2b;
  padding: .5em;
}

.topicsList #doc-metadata {
  background-color: #f7f7f7;
  color: #2b2b2b;
  padding: .5em;
}

.topicsList .topic.current {
  background-color: #f7f7f7;
  color: #C83737;
}

.topicsList .topic:hover, .topicsList .topic:active {
  background-color: #f7f7f7;
  color: #C83737;
}
```
## Recuadros para ejemplos, notas o advertencias

Este código genera un recuadro con una imágen que puede servir para resaltar información dentro de los tutoriales.

```{css, eval=FALSE}
.note {
    padding: 1em;
    margin: 1em 0;
    padding-left: 100px;
    background-size: 70px;
    background-repeat: no-repeat;
    background-position: 15px 15px;
    min-height: 120px;
    color: black;
    background-color: lightgrey;
    border: solid 5px #C83737;
    background-image: url("manzana.png");
  }
```

La nota se visualiza como un recuadro gris con marco rojo, una manzanita roja a la izquierda alineada al centro y texto.

{{< figure src="/media/css_nota.png" alt="Ejemplo de nota de información">}}

Se pueden generar muchos tipos diferentes de notas de acuerdo a nuestras necesidades.

## Para aprender más sobre CSS

Los siguientes sitios rescatados de twitter tienen diferentes recursos para aprender y probar cosas con CSS:

* https://cssstats.com/
* https://csstriggers.com/
* https://cubic-bezier.com/#.17,.67,.83,.67
* https://flexbox.tech/
* https://type-scale.com/

## Fuentes

Para realizar el armado del css de MetaDocencia para los tutoriales y escribir este post utilicé los siguientes recursos:

* [Making pretty note boxes](https://desiree.rbind.io/post/2019/making-tip-boxes-with-bookdown-and-rmarkdown/) de Desirée De Leon

* [Paquete ouitheme](https://github.com/Athanasiamo/uiothemes) de Athanasia Monika Mowinckel

* [Teach R with learnr: a powerful tool for remote teaching](https://education.rstudio.com/blog/2020/05/learnr-for-remote/) de Allison Horst

* [Mozilla Developer CSS guide](https://developer.mozilla.org/es/docs/Web/CSS).

* [Tutorial CSS](https://www.w3schools.com/css/default.asp)

