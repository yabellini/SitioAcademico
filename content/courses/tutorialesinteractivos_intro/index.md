---
title: "Generando tutoriales interactivos con el paquete {learnr}"
subtitle: ""
excerpt: "Aprende como usar {learnr} para construir tutoriales interactivos con R."
date: 2020-10-03
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
layout: single-sidebar
links:
- icon: images
  icon_pack: fas
  name: slides v1.0
  url: https://docs.google.com/presentation/d/14HkcCZ5t0isM9k9P0E5iNPJjO7LCE-Th02rZ0PceHeE/edit?usp=sharing
- icon: images
  icon_pack: fas
  name: slides v3.0
  url: https://docs.google.com/presentation/d/1Kh8aSX_0LR3YXVPj6J7Gfr1ZWFGAS4WCAfNTIUQNkPY/edit?usp=sharing
- icon: github
  icon_pack: fab
  name: code
  url: https://github.com/yabellini/curso_learnr
- icon: youtube
  icon_pack: fab
  name: video
  url: https://youtu.be/d7eXzRzEdC8
---

## Español

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

* Pregunta: ¿Cómo puedo chequear los ejercicios de codigo en mi tutorial?
* Objetivos:
    * Entender las diferentes formas de chequear los ejercicios de código
    * Entender las ventajas y desventajas de las diferentes opciones
* Practica: modificar un ejercicio de código para proporcionar más y mejor feedback.

#### Episodio 5

* Pregunta: ¿Cómo comparto mis tutoriales?
* Objetivos: 
  - Entender las diferentes maneras de publicar/compartir un tutorial con learnr
  - Entender las ventajas y desventajas de cada una
* Práctica: publicar el tutorial como una shiny app.

#### Episodio 6 

* Pregunta: ¿Dónde aprendo más?
* Objetivos:
  - Detalles de lugares donde aprender más sobre learnr
  - Detalle de paquetes que se pueden usar con learnr
  - Detalle de repositorios con código fuente de diferentes tipos de tutoriales.


### Materiales


### ¿Te vienen bien cualquiera de estos contenidos? ¡Servite sin culpa!

Este curso se comparte bajo la licencia [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/deed.es_ES).
Es decir, podés reusar o editar cualquier material que aparece acá, lo único que pedimos a cambio es que cuando tomes material de acá incluyas una referencia a esta página web y compartas tu material con esta misma licencia.

> Este curso fue originalmente desarrollado para MetaDocencia (2020-2022).