---
title: "Proyecto 2 - Las Estrellas del Universo R"
author: Yanina Bellini Saibene
summary: "Un proyecto de entrevistas multilingües con desarrolladores del mundo académico, la industria y el gobierno, que utilizan R-Universe. En este articulo comparto detalles de cómo las organizamos, cómo ejecutamos el proyecto y qué resultados obtuvimos." 
date: '2024-06-30'
categories:
  - Community
  - 100DaysToOffload
  - rOpenSci
tags:
  - Community
  - 100DaysToOffload
  - rOpenSci
---

{{< figure src="featured.jpg" alt="Cohete despegando.">}}

> Foto de <a href="https://unsplash.com/es/@ivvndiaz?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Iván Díaz</a> en <a href="https://unsplash.com/es/fotos/avion-blanco-y-negro-volando-en-el-cielo-durante-el-dia-YOy-ek-aBR0?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  

## R-Universe

Mi primera contribucion a rOpenSci, incluso antes de convertirme en Community Manager, fue [un blog post en castellano sobre como cree mi propio universo R](https://ropensci.org/es/blog/2021/09/21/creando-tu-r-universe/). 

[R-Universe](https://ropensci.org/r-universe/) es la plataforma de rOpenSci para facilitar la publicacion, búsqueda, desarrollo y el uso de paquetes de R. Algunas de sus características clave incluyen:

* Actúa como un **repositorio centralizado** para encontrar y descargar paquetes de R.

* Tiene un **sistema automatizado para la construcción y distribución de paquetes**, lo que facilita la publicación y actualización del software por parte de quienes lo desarrollan.

* Proporciona la **documentación, ejemplos y otros recursos útiles** para los paquetes disponibles, ayudando a sus usuarios a comprender y utilizar los paquetes.

* Asegura que los paquetes sean compatibles y estén disponibles para diferentes sistemas operativos, incluyendo Windows, macOS y Linux **proveyendo soporte múltiplataforma**. 

* Permite a los desarrolladores **vincular sus repositorios de GitHub con R-Universe**, facilitando la integración continua y el despliegue de actualizaciones.


Cuando me convertí en Community Manager, [Jeroen Ooms](https://ropensci.org/author/jeroen-ooms/), compartió conmigo su idea de entrevistar a los usuarios de la plataforma para conocer mejor su trabajo, cómo utilizaban R-Universe y sus características y necesidades. Fue una excelente oportunidad para mí de hablar y conocer a las personas que forman parte de la comunidad rOpenSci.

## De la idea a la serie de entrevistas multimedia

La propuesta final fue generar una serie de entrevistas multimedias, blog post y video, llamada ["Conociendo a las estrellas del universo R."](https://ropensci.org/es/tags/r-universe-stars/) 

Nuestro _objetivo principal_ fue dar a conocer a los grupos de trabajo y a las personas que están detrás del desarrollo de software y paquetes que muchas personas utilizan y que están disponibles a través del universo R. 

Como _objetivos secundarios_ queriamos entender cómo las personas utilizan la plataforma, identificar problemas comunes, obtener retroalimentación sobre nuevas funciones y escuchar sugerencias para mejoras. 

Con estos objetivos en mente y utilizando la lista inicial de Jeroen como base, seleccionamos a los primeros entrevistados en función de su actividad, diversidad geográfica y uso de R-Universe.

Generamos una plantilla de mail de invitacion y la enviamos a los primeros seleccionados. Esperabamos poder hacer entre 4 y 6 entrevistas. 

Mientras esperabamos las respuestas, la periodista [Alejandra Bellini](https://ropensci.org/es/author/alejandra-bellini/) me ayudo a desarrollar el guion de la entrevista. Preparamos una lista de preguntas abiertas para que las personas entrevistadas puedan compartir sus opiniones y experiencias de manera libre. Estas preguntas estaban alineadas con los objetivos definidos.

Alejandra también dirigió la primera entrevista que hicimos en español para que yo pudiera ver cómo se desarrollaba el proceso. También me dio consejos sobre cómo entrevistar para las siguientes entrevistas que realicé en inglés. Jeroen también participó en algunas de las entrevistas.

Todo el material (texto del mail, guion de la entrevista) se genero de forma bilingüe. 

## Las entrevistas

Enviamos ocho invitaciones y realizamos seis entrevistas. El proceso para organizar las entrevistas fue el siguiente:

1) Luego de recibir la confirmación de la persona entrevistada, coordinamos una fecha y hora para la entrevista.  Yo enviaba una invitacion de Zoom y la guia de preguntas con anterioridad para que las personas puedieran prepararse. 

2) Realizamos las entrevistas utilizando una herramienta de videoconferencia. Primero expliqué el objetivo y cómo realizaríamos la entrevista, y luego empecé a grabar la reunión. Empezábamos con las preguntas guionizadas y seguíamos el hilo de la conversación. En algunas ocasiones, la persona entrevistada compartía su pantalla para mostrarnos cómo utiliza R-Universe en su trabajo o cómo funcionan los paquetes que desarrolla. Los entrevistados también tenían la oportunidad de hacernos preguntas.

3) Al finalizar la entrevista, agradeciamos a la persona entrevistada y le explicámos los próximos pasos: editar el video, escribir el blog post y compartirles ambos para que puedan revisarlos antes de publicarlos. 

4) Luego de la entrevista, se generaba un resumen escrito de la misma seleccionando el contenido relevante para el texto, las citas de los entrevistados y que se complemente con el contenido seleccionado para el video. 

5) Alejandra Bellini y [Lucio Casalla](https://ropensci.org/es/author/lucio-casalla/) también me ayudaron en la edición del vídeo. Las entrevistas duraron entre 60 y 90 minutos, pero los vídeos finales duraron entre 10 y 15 minutos. Seleccionar las partes relevantes fue una tarea muy interesante.

6) Se escribía un primer borrador en inglés del post en la web de rOpenSci que era editado por [Steffi LaZerte](https://ropensci.org/author/steffi-lazerte/), una de las editoras de nuestro blog. La version editada se enviaba a las personas entrevistadas haciendo los cambios que solicitaran hasta obtener su aprobación. En ese momento generabamos los subtituilos en inglés y español del video y tradujimos el blog post al español.  En el caso de uno de los blog post, el entrevistado tambien lo tradujo al francés, ya que es su lengua materna. Para las traducciones usamos nuestro paquete [babeldown](https://docs.ropensci.org/babeldown/).

7) Finalmente, se publicaba el blog post en la [web de rOpenSci](https://ropensci.org/blog/) y se subia el video a [nuestro canal de Vimeo](https://vimeo.com/ropensci) (para el cual se escribia tambien un resumen). Lucio genero una bonita animacion del isologotipo de rOpenSci para agregar al inicio y final de todos nuestros videos.

## Publicacion

Luego de publicar el blog post en nuestra web con los videos en nuestro canal, se realizaba la difusion del material. El plan de comunicacion incluyo:

* Escribir post sobre la entrevista para redes sociales y compartirlo en Twitter/Mastodon, LinkedIn y espacios de Slack relevantes. Tanto en Ingles como en castellano.

* Escribir un resumen para el newsletter de rOpenSci.

* Compartir el material con las personas entrevistadas para que puedan compartirlo en sus redes sociales y con sus comunidades.

## Resultados

El proceso de entrevistas fue muy interesante y enriquecedor. Aprendimos mucho de las personas que entrevistamos y de los proyectos que lideran.  Ademas de los blog post de cada equipo entrevistados, hicimos un resumen de la serie completa:

* noviembre 6, 2023, [El multiverso de rOpenSci](https://ropensci.org/es/blog/2023/11/06/r-universe-stars-finale-es/)
* septiembre 15, 2023, [Conociendo a las estrellas del Universo R: El universo R contra las enfermedades.](https://ropensci.org/es/blog/2023/09/15/r-universe-stars-5-es/)
* junio 6, 2023, [Conociendo a las estrellas del Universo R: PEcAn, un proyecto de código abierto para cuidar el planeta](https://ropensci.org/es/blog/2023/06/06/r-universe-stars-4-es/)
* marzo 30, 2023, [Conociendo a las estrellas del Universo R: Investigando nuestro cerebro con la magia del universo R](https://ropensci.org/es/blog/2023/03/30/r-universe-stars-3-es/)
* febrero 28, 2023, [Aprender, ayudar y compartir. El método de ThinkR para crear una comunidad cada vez más grande y amigable de R](https://ropensci.org/es/blog/2023/02/28/r-universe-stars-2-es/)
* noviembre 23, 2022, [Conociendo a las estrellas del universo R: comunidad R, intercambiar y aprender](https://ropensci.org/es/blog/2022/11/23/r-universe-stars-1-es/)

Destacamos y exploramos diferentes equipos y proyectos de software abierto de todo el mundo, del ambito academico, como de gobierno e industria; el trabajo que realizan, sus procesos y usuarios. Aprendimos sobre las necesidades y desafíos que enfrentan y obtuvimos valiosa retroalimentación sobre R-Universe. 

También generamos un conjunto diverso y multilingüe de casos de uso de R-Universe, que pueden servir de inspiración para otros desarrolladores y grupos de usuarios.

Esta fue una oportunidad de trabajar con Jeroen, Alejandra, Lucio y Steffi en un proyecto que me permitió aprender mucho sobre la comunidad rOpenSci y sobre detalles muy interesantes de R-Universe.

Quiero dar las gracias a todos las personas entrevistadas por su tiempo y por compartir con nosotros su entusiasmo por su trabajo y el software abierto. 

Espero que en algún momento podamos retomar este tipo de entrevistas con más personas que forman parte de rOpenSci.