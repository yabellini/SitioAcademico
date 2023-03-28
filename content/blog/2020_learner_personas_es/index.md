---
date: "2020-10-25"
draft: false
linktitle: Tutoriales interactivos y personas tipo
summary: Qué son las personas tipo y como podemos utilizarlas en el diseño de nuestros tutoriales. 
title: Tutoriales interactivos y personas tipo
authors: 
    - Yanina Bellini Saibene
categories:
  - Education
  - Español
  - rstats
tags: 
  - learner personas
  - Open Education
  - rstats
  - Technical tips
---

{{< figure src="/media/personas_post.jpg" alt="Estudiantes viendo conferencia grabada con profesor hablando desde tableta">}}
<a href="http://www.freepik.com">Designed by vectorjuice / Freepik</a>

## ¿Qué es una persona tipo?

Las [personas tipo](https://teachtogether.tech/es/index.html#s:process-personas) se conocen en inglés como _Learner Personas_ y su objetivo es describir el público para el que fue pensado el curso. Esta información debería ayudar en:

* el desarrollo de las lecciones,
* la decisión de usar los materiales, tanto sea para tomar el curso, como para usarlos con el objetivo de generar los propios,
* la forma de presentar y difundir el curso.

Cada lección debe ser pensada, organizada y generada para una audiencia en particular y, como se explica en el libro [_Teaching Teach Together_](https://teachtogether.tech/es/) debe contemplar los siguientes aspectos:

* los antecedentes generales del estudiante,
* los conocimientos y/o experiencia previa relevante,
* lo que estos estudiantes creen que quieren aprender (en contraposición a lo que el instructor cree que deberían aprender), y
* cualquier consideración especial, como las necesidades de accesibilidad o las restricciones tecnológicas.

## Ejemplos de personas tipos

Para ver a las personas tipo en acción, voy a compartirles las tres personas en las cuales pienso cuando genero material sobre {learnr} para este sitio web:

* **_Josefina:_** conoce y enseña R en su cátedra en la universidad.  Está familiarizada con _RMarkdown_ (es parte de lo que enseña a sus estudiantes y uno de los formatos en los que comparte ejercicios resueltos).  La cantidad de estudiantes de su materia le hace cada vez más difícil poder corregir todos los ejercicios de código _a mano_ así que está interesada en proporcionar feedback automatizados a la respuesta de los ejercicios de programación con R que dan en su materia.

* **_Francisco:_** es investigador de INTA y como resultado de sus investigaciones a generado paquetes de R que están publicados en CRAN. Está familiarizado con _RMarkdown_. Sabe que en la nueva IDE de RStudio hay un panel de tutoriales donde se podría cargar la ayuda de su paquete en formato de tutorial y quiere explorar esta opción. 

* **_Rene:_** es docente y ha tenido que llevar su clase de _introducción a R_ a formato virtual, esto le hace muy difícil poder ayudar a sus alumnos con la configuración de sus máquinas personales con todo el software necesario para llevar adelante la clase. Ya tiene ejercicios generados en formato rmarkdown. Con la idea de que puedan empezar a trabajar enseguida con R sin sufrir con la instalación en un inicio le parece buena idea generar tutoriales interactivos porque escuchó que se pueden publicar como una aplicación shiny.


## Personas tipo ya definidas

Para empezar a generar nuestras propias personas, puede ser buena idea, ver la descripción que han realizado otras y otros docentes para sus cursos y ver si las podemos usar y adaptar para nuestras propias lecciones.

### Personas tipo de mis cursos

En [este repositorio](https://github.com/yabellini/learner_personas) pueden encontrar todas las personas tipo que he definido para mis cursos y tutoriales relacionados con **herramientas informáticas y programación**.  La licencia es [CC-BY](https://creativecommons.org/licenses/by/4.0/legalcode.es) por lo que pueden utilizarlas tal cual están o adaptarlas a sus necesidades, sólo deben mencionarme como fuente. 

La más popular de todas esas personas es _Romina_ a quien definí para un curso de _Introducción a Git con RStudio_. Se las comparto en este post porque las personas que participan en ese curso reaccionan con sentimientos de motivación y comunidad, al verse identificadas en la descripción de la persona tipo. _Motivación_ porque el curso fue pensado para ellas y ellos, _comunidad_ porque no están solas y solos en la necesidad de aprender este recurso.

* **_Romina:_** trabaja ordenando y analizando datos utilizando R para una variedad de clientes. Utiliza proyectos en RStudio para ordenar su trabajo. Comparte sus avances y resultados utilizando herramientas en la nube (como dropbox y google drive). Compartir de esta manera le ha traído varios dolores de cabeza Sabe que Git puede ayudarla con estos problemas pero no le queda claro como. Tiene usuario en GitHub pero nunca usó. Quiere entender como funciona y como usarlo con R y RStudio para poder incorporarlo a sus proyectos.


### Personas tipo de [MetaDocencia](https://www.metadocencia.org)

**MetaDocencia** es una organización sin fines de lucro que enseña a enseñar a docentes de habla hispana (y de la cual soy co-fundadora).  [Las personas tipo](https://www.metadocencia.org/post/personas-tipo/) de estos cursos describen **diferentes perfiles de docentes**.  La licencia de estas personas tipo también es CC-BY.

### Personas tipo de [RStudio Education](https://education.rstudio.com)

En este [blog post](https://education.rstudio.com/blog/2020/10/learner-personas/) en _Inglés_ escrito por Greg Wilson se describen nueve personas tipo desarrolladas por el equipo de educación de RStudio y que intentan capturar las características clave de las personas a las que les gustaría ayudar con sus clases y materiales.


## ¿Cómo las integro en mis tutoriales interactivos?

En todos mis tutoriales y cursos agrego una sección llamada presentación que tiene como primer punto un [Mapa Conceptual](/post/concept_maps/), luego las _personas tipo_ y finalmente la licencia del material.

De esta manera toda la información relacionada al alcance del tutorial, para quien fue pensado, que contenidos se van a desarrollar y como puede ser utilizado por estudiantes y docentes está concentrado en un solo lugar.  En la imagen se ve un ejemplo de una persona tipo en un tutorial:

{{< figure src="/media/personas_tipo.png" alt="Captura de pantalla de la definición de una persona tipo en un tutorial de learnr">}}

Espero que este concepto de _persona tipo_ te sea de utilidad, como también los ejemplos mencionados y los lugares donde buscar más personas definidas. Me encantaría saber si utilizas algunas de mis personas o conocer cuales son las tuyas.
