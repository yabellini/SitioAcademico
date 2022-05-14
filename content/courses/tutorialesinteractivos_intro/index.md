---
title: "Generando tutoriales interactivos con el paquete {learnr}"
subtitle: ""
excerpt: "Aprende como usar {learnr} para construir tutoriales interactivos con R.  Curso en desarrollo."
date: 020-10-03
author: "Yanina Bellini Saibene and Paola Corrales"
featured: true
draft: false
tags:
  - Community
  - Education
  - MetaDocencia
  - R
  - packages
categories:
  - Community
  - Education
  - Español
  - R
# layout options: single or single-sidebar
layout: single
links:
- icon: images
  icon_pack: fas
  name: slides
  url: https://docs.google.com/presentation/d/14HkcCZ5t0isM9k9P0E5iNPJjO7LCE-Th02rZ0PceHeE/edit?usp=sharing
- icon: github
  icon_pack: fab
  name: code
  url: https://github.com/yabellini/curso_learnr
---

## Español

>> Autoras: Yanina Bellini Saibene y Paola Corrales para MetaDocencia (2021)

### Objetivos

El **objetivo** de este curso es introducir a las personas que participan al paquete {learnr} de R y como utilizarlo para generar tutoriales interactivos que permitan a los y las estudiantes escribir y ejecutar código R directamente desde el tutorial, contestar preguntas y recibir feedback inmediato.

### ¿Para quién está pensado este taller?

Cada lección debe ser pensada, organizada y generada para una audiencia en particular, estas son las [personas tipo](/personas/) en la que pensamos cuando preparamos este taller:

* _Josefina_: conoce y enseña R en su cátedra en la universidad.  Está interesada en proporcionar feedback automatizados a la respuesta de los ejercicios de programación con R que dan en su materia. 

* _Francisco_: es desarrollador de paquetes, quiere explorar la opción de generar tutoriales interactivos como parte de la ayuda.  

* _Alex_: quiere desarrollar tutoriales para publicarlos como aplicaciones shiny con la idea de que sus estudiantes puedan empezar a trabajar enseguida con R sin sufrir con la instalación de herramientas. 

### Qué *no* incluye este taller

Si bien realizaremos actividades en RStudio, este taller NO es un curso de programación (es un taller sobre cómo enseñar programación).

Entre otras cosas, quedan fuera del alcance del taller:

* Entrenamiento en técnicas de programación
* Desarrollo en profundidad y práctica extensiva de las técnicas mencionadas
* Contenidos teóricos sobre pedagogía


### Duración

El taller tiene una duración de 2 horas con intervalos (idealmente lejos de cualquier pantalla) de aproximadamente 5 minutos cada 50 minutos de contenidos.


### Cronograma tentativo  


|  Duración (min)  |  Actividad  |
| :------:|:----------- |
| 5 <img width="200"/> | Tiempo previo para conectarse y asegurarse que anda bien tu conexión de audio y video (si no tienes camara no importa) |
| 10 | Introducción de las docentes y del curso y repaso de las opciones comunes de las herramientas que vamos a usar. |
| 15 | Episodio 1: ¿Qué es un tutorial interactivo? | 
| 20 | Episodio 2:  ¿Cómo agrego preguntas a mi tutorial? | 
| 10 | Pausa |
| 15 | Episodio 3: ¿Cómo puedo realizar ejercicios con código en mis tutoriales? |
| 15 | Episodio 4: ¿Cómo comparto mis tutoriales? |
| 10 | Episodio 5: ¿Dónde aprendo más? |
| 10 | Cierre del taller: resumen y devolución |


#### Episodio 1 

* Pregunta: ¿Qué es un tutorial interactivo?
* Objetivos: 
  - Entender los beneficios de un tutorial interactivo 
  - Entender los componentes básicos de un tutorial interactivo
* Práctica: analizar la plantilla de learnr y reconocer las partes del tutorial, cambiar alguna opción en el YAML y analizar el cambio de comportamiento.

#### Episodio 2 

* Pregunta: ¿Cómo agrego preguntas a mi tutorial?
* Objetivos:
  - Entender los tipos de preguntas que existen en un tutorial learnr
  - Entender los componentes básicos de las preguntas multiple choice
  - Entender los componentes básicos de las preguntas de texto 
* Práctica: modificar una serie de preguntas en un tutorial de ejemplo armado para este taller.

#### Episodio 3 

* Pregunta: ¿Cómo puedo realizar ejercicios con código en mis tutoriales?
* Objetivos:
  - Entender los componentes básicos de los ejercicios
  - Entender el chunk exercise
  - Entender el chunk hint
  - Entender el chunk solution
  - Entender el setup previo de los chunks
* Practica: modificar un chunk de ejercicio previamente generado en el ejemplo y modificarlo para que entregue un hint y muestre una solución

#### Episodio 4

* Pregunta: ¿Cómo comparto mis tutoriales?
* Objetivos: 
  - Entender las diferentes maneras de publicar/compartir un tutorial con learnr
  - Entender las ventajas y desventajas de cada una
* Práctica: publicar el tutorial como una shiny app.

#### Episodio 5 

* Pregunta: ¿Dónde aprendo más?
* Objetivos:
  - Detalles de lugares donde aprender más sobre learnr
  - Detalle de paquetes que se pueden usar con learnr
  - Detalle de repositorios con código fuente de diferentes tipos de tutoriales.


### Materiales

* [Presentación que usamos en el curso](https://docs.google.com/presentation/d/1QLRUbERgEk85s8qK6mzmMJn7avQ_bEmTn_NzFYgqwkc/edit?usp=sharing) con notas ampliando el contenido para quienes dan la clase

* [Video del curso](https://youtu.be/d7eXzRzEdC8)

### ¿Te vienen bien cualquiera de estos contenidos? ¡Servite sin culpa!

Este curso se comparte bajo la licencia [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/deed.es_ES).
Es decir, podés reusar o editar cualquier material que aparece acá, lo único que pedimos a cambio es que cuando tomes material de acá incluyas una referencia a esta página web y compartas tu material con esta misma licencia.

## English

>> Authors: Yanina Bellini Saibene y Paola Corrales para MetaDocencia (2021)

### Objectives 

To introduce the {learnr} package and show how to use it to create interactive tutorials. These interactive tools allow the students to run R code directly in the tutorial, to answer to questions and to receive immediate feedback. 

### Intended public of this course

When we designed this workshop, we had in mind Josefina, Francisco and Alex as our learner personas. 

* _Josefina_: teaches R at University. She is interested in giving automated feedback to the R exercises given to her students. 

* _Francisco_: is a professional developer and wants to explore the interactive tutorials as possible part of the help and documentation of his packages. 

* _Alex_: wants to develop tutorials to publish them as shiny applications so that their students could start right away with R without painful installations. 


### _Not_ included in this workshop

Since we only have 3 hours, a lot of things will be out of reach of the workshop. Among other things, we will not learn:

* Programming techniques 
* Theory of pedagogy
* Rmarkdown 
* Package development

### Duration

This is a 3-hour workshop with intervals (ideally away from any screen) of approximately 5 minutes for every 50 minutes of content.

### Sample schedule 


|  Duration (min) |  Activity  |
| ---:  | :----------- |
 | 5  <img width="150"/>|  Time to connect and make sure your audio and video connection is good (if you don't have a camera it doesn't matter, but if you do, it helps)|
 | 10 |  Introduction to the course |
  | 15 |  What is an interactive tutorial? |
  | 20 |  How can I add questions to my tutorial? |
  | 10 |  Break |
  | 15 |  How can I include coding exercises in my tutorial? |
   | 15 |  How can I share my tutorials? |
  | 10 |  Where could I learn more about {learnr} tutorials? |
 |  10 | End of the workshop: summary and feedback |

#### Chapter 1

* Question: What is an interactive tutorial?
* Goals:
    - Understand the benefits of an interactive tutorial
    - Understand the basic different parts of the {learnr} tutorials
* Practice:
    - Analyze a {learnr} tutorial template and recognize the different parts. Modify options in the YAML and analyze the changes.

#### Chapter 2

* Question: How can I add questions to my tutorial?
* Goals:
    - Understand the different type of questions
    - Understand the basic components of multiple choice questions
    - Understand the basic components of text questions
* Practice: Modify some of the questions of the  tutorial provided for this exercise.

#### Chapter 3

* Question: How can I include coding exercises in my tutorial? 
* Goals:
    * Understand the basic components of the exercises
    * Understand the chunk exercise
    * Understand the chunk hint
    * Understand the chunk solution
    * Understand the default set up of the chunks
* Practice: Modify an exercise chunk in order to provide a hint and a solution

#### Chapter 4

* Question: How can I share my tutorials?
* Goals:
    * Understand the different ways to publish/share a {learnr} tutorial 
    * Understand the advantages and shortages of the different options
* Practice: Publish the tutorial as a Shiny App

#### Chapter 5

* Question: Where can I learn more?
* Goals:
    * Details of sites to learn more about {learnr}
    * Details of the packages that can be combined with {learnr}
    * Details of repositories with code that generate learnr tutorials.


### Course materials

* [Presentation used during the course](https://docs.google.com/presentation/d/14HkcCZ5t0isM9k9P0E5iNPJjO7LCE-Th02rZ0PceHeE/edit?usp=sharing)

* [Recording of the course](https://youtu.be/BGmM_E6BrRI)

### Do you want to re-use any of our contents? Please, be our guest!

Our materials are available for free under this [license](https://creativecommons.org/licenses/by/4.0/deed.es). You can reuse or edit any material that appears here, the only thing we ask in return is that when you reuse our materials you include a reference to this website.