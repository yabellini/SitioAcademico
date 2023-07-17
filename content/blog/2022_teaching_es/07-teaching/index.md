---
title: "Diez consejos rápidos para enseñar con programación (participativa) en vivo (en línea)"
weight: 7
subtitle: ""
excerpt: " "
date: 2023-07-17
draft: false
tag:
  - Education
  - Community
  - Español
---

La programación participativa en vivo y la programación en vivo son estrategias eficaces para enseñar a programar, ya que permite que les estudiantes vean el proceso de pensamiento de quien enseña y sus técnicas de resolución de problemas en tiempo real mientras programan. Además, posibilitan una enseñanza activa al permitir a los y las profesores/as seguir los intereses, las preguntas y los comentarios de sus estudiantes. Sin embargo, con el cambio a las aulas virtuales, tenemos que adaptar estas prácticas docentes al contexto online. 

En este artículo, comparto mis diez consejos basados en mi experiencia en la enseñanza de la codificación en línea utilizando codificación participativa en vivo.

## ¿Qué es programación participativa en vivo?

Una de las formas más eficaces de enseñar a programar es usar **programación en vivo**. En lugar de presentar material ya escrito, el profesor o la profesora escribe el código delante de la clase mientras sus estudiantes lo siguen, escribiendolo y ejecutándolo sobre la marcha.

## Consejos existentes de programación en vivo.

Utilicé tres fuentes que se centran en la enseñanza en persona con programación en vivo:


* [Top Ten Tips for Participatory Live Coding in a Workshop by The Carpentries](https://carpentries.github.io/instructor-training/17-live/#top-ten-tips-for-participatory-live-coding-in-a-workshop)
* [Ten quick tips for teaching with participatory live-coding paper in Plos Computational Biology](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008090)
* [The live coding session of the book Teaching Tech Together (T3)](https://educarencomunidad.tech/en/index.html#s:performance-live)

Esta tabla muestra los consejos de cada texto uno al lado del otro, emparejando consejos similares. El número de cada recomendación es el lugar que ocupa esta consejo en el texto original.


| The Carpentries | Plos  	| T3           	|
|-----------------|-----------|------------------|
| 1. Levántese y muévase por la habitación si es posible.| 3. Sea visto y escuchado. | 4. Hágase ver y oír,  11. Da la cara a la pantalla, solo de vez en cuando. |
| 2. Ir despacio | 1. Ir despacio | 3. Tomarlo con calma |
| 3. Duplica el entorno de sus estudiantes. | 2.Duplica el entorno de sus estudiantes.| 5. Duplica el entorno de sus estudiantes|
| 4. Utiliza tu pantalla sabiamente.| 4. Utiliza tu(s) pantalla(s) sabiamente| 6. Utiliza tu pantalla sabiamente, 7. Dispositivos dobles |
| 5. Usa ilustraciones | 6. Usa ilustraciones, aún mejor, dibujalos | 8. Dibuja temprano, dibuja seguido |
| 6. Desactiva las notificaciones | 5. Evite las distracciones | 9. Evite las distracciones |
| 7. Seguir el material de la lección. | 7. Seguir el material de la lección | 10. Improvisa después de conocer el material |
| 8. No dejar atrás a ningún estudiante. | 9. Obtener feedback en tiempo real y proporcionar ayuda inmediata, 10. Convertir a tus estudiantes en co-docentes | 2. Pregunta por predicciones |
| 9. Acepta los errores. | 8. Abraza tus errores | 1. Abraza tus errores | 
| 10. Divertete | | |


Muchos consejos se repiten en todas las fuentes o son muy similares entre sí (en distinto orden). He tomado diez de estos consejos y les agregué consideraciones para la enseñanza en línea.

## Consejos para la programación participativa en línea.

### 1. Que te vean y te escuchen

A medida que tus estudiantes van codificando, deben ver y oír lo que estás haciendo. En un entorno en línea, esto puede requerir más recursos en términos de tecnología e infraestructura, como una conexión estable a Internet, una pantalla panorámica o una segunda pantalla para ti y tus estudiantes.

* **Antes de empezar:** Explica a tus estudiantes cómo acomodar su pantalla. En caso de que sólo tengan una (como la mayoría de mis alumnos), demuéstrales cómo pueden dividir la pantalla en dos vertical u horizontalmente.  Si tienen dos pantallas, muestra cómo dividir las ventanas, una con las pantallas del docente y la otra con su entorno de programación.  Puedes tener algunas imágenes o vídeos para mostrar cómo conseguirlo.  

Aquí hay un hermoso ejemplo de [instrucciones de R-Ladies Chile para un taller online](https://github.com/rladieschile/taller-introductorio-mayo/blob/master/preparacion-sesion-1.md)

{{< figure src = "screen_students.jpg" alt = "Ordena tus pantallas, una pantalla en el televisor y la otra en tu computadora. La mitad de la pantalla con la IDE y la otra con el video del docente" >}}

Si estás enseñando cursos largos (más de tres clases), podes hacer una demostración la primera clase y después hacerlo de vez en cuando como recordatorio.  También podes compartir estos videos o imágenes asi tus estudiantes pueden chequear como ordenar sus pantallas.

* **Durante el live coding:**

  * comparte tu pantalla y pregunta antes de empezar a programar si tus estudiantes ven tu pantalla correctamente y si el tamaño de la fuente es adecuado. Cambialo si te lo solicitan.
 
  * Agranda tu puntero del mouse y considera usar un puntero resaltado ([algo como esto](https://www.gnome-look.org/p/999801/)).
 
  * Usa un software que muestre en pantalla las teclas que presionas, como [Screenkey](https://gitlab.com/screenkey/screenkey).  Si te olvidas de decir un atajo de teclado en voz alta, el programa lo mostrará en la pantalla para tus estudiantes.

  * El fondo blanco parece mejor para las clases sincrónicas. El tema nocturno parece mejor para los vídeos grabados porque hay estudiantes que los ven de noche y utilizan dispositivos pequeños.

  * Si puedes, comparte tu código no solo por medio de tu pantalla mientras lo escribes. Antonio Vazquez Brust [explica como hacerlo usando `ngrok` y RStudio para enseñar R](https://bitsandbricks.github.io/post/compartiendo-c%C3%B3digo-en-vivo-con-el-mundo-desde-rstudio/) y Elio Campitelli explica como [enseña R con programación en vivo sin fricción en este vídeo](https://youtu.be/idFpvvH1JyI). Existen otras herramientas para otros lenguajes. Naomi Alterman nos muestra [cómo transmitir en directo tu codificación en vivo a páginas web estáticas para tus estudiantes en esta charla](https://youtu.be/a3uJj7Eqwzg) para CarpentryCon 2022.
 
* **Después del live coding**: debemos considerar la posibilidad de que algunos de tus estudiantes se hayan quedado atrás, no puedan resolver un ejercicio o lo hagan de forma poco eficiente. Por eso es importante compartir después de la clase el código generado en vivo durante la misma. Puedes copiarlo y pegarlo en el chat de la plataforma, copiarlo y pegarlo en los apuntes compartidos o subirlo a la página web del curso o al campus virtual. También puedes compartir una carpeta en un servicio de almacenamiento en la nube. Disponer del código final ayudará a tus alumnos a validar su código y a ponerse al día si no pueden copiar o escribir alguna parte del mismo.


### 2. Ve despacio y no enseñes sola/o.

Cuando se realiza codificación participativa en vivo, es necesario enseñar y programar a un ritmo que permita a tus estudiantes seguir el proceso sin quedarse atrás. En los entornos en línea, es esencial que tus estudiantes cambien de ventana (la demostración del docente y su propia codificación) o de pantalla si tienen más de una.

* Empieza con un script o notebook en blanco para asegurarte de que les explicas todo lo que necesitan para que el código funcione.

* Explica el objetivo del código que vas a desarrollar y escríbelo en la notebook o como comentario en el script.  Nos ayuda a centrarnos en lo que queremos y en el razonamiento que hay detrás de codificar para ese objetivo.

* Explica cada paso que has dado. Di en voz alta lo que estás haciendo mientras lo haces para cada comando que escribes, cada palabra de código que escribes y cada elemento de menú o botón de sitio web que pulsas. A continuación, señala el comando y su resultado en la pantalla y repítelo para que tus estudiantes puedan comprobar lo que han hecho.

* Menciona el número de línea del código al que te refieres.

* Narra lo que escribes (y las combinaciones de teclas y atajos de teclado), especialmente cuando tengas que utilizar signos de puntuación complicados ("corchetes", "paréntesis redondos", etc.). 

* Cuando una IDE autocompleta cosas, es útil señalarlo las primeras veces (y decir cómo se usa o activa esa característica) ya que puede ser la primera vez que algunos estudiantes lo vean.  Por ejemplo, RStudio IDE tiene IntelliSense. Puedes detenerte y explicar lo que está mostrando y cómo cambia cuando escribes, luego necesitas usar la tecla tab (en windows) para completar la palabra, lo cual también explico, para que no piensen que escribo tan rápido. Luego el IDE muestra un resumen de ayuda para la función. También me detengo ahí y leo esa ayuda y explico las diferentes partes de la ayuda para que puedan reconocer parámetros, valores por defecto, etc.


* Si la salida de tu comando o código hace que lo que acabas de escribir desaparezca de la vista, desplázate hacia atrás para que tus estudiantes puedan verlo de nuevo.

* No utilices muchos atajos de teclado, sobre todo al principio. Si utilizas un atajo de teclado, dilo en voz alta la primera vez que lo hagas. Explica una alternativa al atajo (por ejemplo, el uso de menús). Puedes recordar a tus estudiantes qué atajos utilizas de vez en cuando (en caso de que no utilices un programa que muestre las teclas que pulsaste en pantalla). 

* Tu ayudante o co-docente debe prestar atención al chat, ayudando a localizar y resolver los problemas de tus estudiantes, copiando enlaces o trozos de código si es necesario, y avisándote cuando haya que aclarar, volver a explicar o mostrar algo una vez más. 

* Si estás enseñando sin ayuda, informa a tus estudiantes cuándo estarás prestando atención al chat para ayudarles. Deja claro cómo pueden participar y hacer preguntas (utilizando el chat, sin silenciarlos, utilizando una expresión no verbal, notas compartidas, etc.) y cómo responderás tú.

* Utiliza el chat o el documento de las notas compartidas para copiar y pegar el código o los errores de tus estudiantes. Ten cuidado con los sistemas de chat traicioneros que pueden manipular tu código. Las comillas rectas pueden transformarse en comillas tipográficas, y los límites de caracteres pueden cortar partes del código, etc. 


### 3. Duplica el entorno de tus estudiantes.

Si tus estudiantes tienen que trabajar en un entorno distinto al tuyo, tienen que hacer un esfuerzo mental que no contribuye al aprendizaje. La ciencia del aprendizaje llama a esto "carga cognitiva extraña". Intenta crear un entorno lo más parecido posible al que tienen tus estudiantes.  Si son principiantes, es muy probable que tengan la configuración por defecto de la IDE o software que vayas a utilizar.

Una solución basada en la nube es la mejor alternativa para asegurarte de que tú y tus estudiantes tienen la misma configuración. Algunas de estas herramientas te permiten incluir todo el software, paquetes y datos que necesitas evitando problemas de instalación y la consiguiente frustración.

Cuando enseño SQL, utilizo [SQL Lite Online](https://sqliteonline.com/). Cuando enseño R, utilizo [Posit Cloud](https://posit.cloud/) en la primera clase, y luego utilizamos la última parte de esa clase para solucionar problemas de instalación en los ordenadores de mis estudiantes.  También tengo un proyecto Posit Cloud como copia de seguridad en caso de que algunos estudiantes no puedan instalar todo en sus computadoras.  Dentro de los problemas que tienen esta soluviones está el costo y el ancho de banda necesario para usarlas durante las clases.


### 4. Usa tu(s) pantalla(s) sabiamente.

Ya hemos mencionado que [necesitas mostrar a tus estudiantes cómo acomodar su pantalla para verte mejor](#1.-Que-te-vean-y-te-escuchen). Al utilizar live coding, también debes acomodar tu(s) pantalla(s) para enseñar.

La mejor solución es utilizar dos dispositivos o pantallas al enseñar: una para compartir con tus estudiantes y otra para ver sus notas y vídeos, las notas de la lección y la ventana de chat.

Si no tienes dos pantallas, comparte con tus estudiantes sólo las ventanas o paneles que quieras que vean.  Puedes tener las notas de la lección impresas en papel o en una ventana no compartida.

Aquí tienes un bonito ejemplo de configuración de escritorio de [Paola Corrales](https://paocorrales.github.io/) con una o dos pantallas.

{{< figure src = "screen_teacher.jpg" alt = "Tidy your screens" >}}


Amplía el panel de la pantalla que necesitas mostrar. Por ejemplo, si necesitas mostrar el código amplía las ventanas de script. Si necesitas mostrar un resultado, amplía el panel de la consola, o de gráficos, etc.

Una de las ventajas de la enseñanza en línea es que cuando la gente se encuentra con problemas, puede compartir la pantalla y resolver el problema trabajando en conjunto. Si tu estudiante se siente cómodo/a, permitirle compartir su pantalla para resolver problemas con toda la clase; esta es una excelente experiencia de aprendizaje.  También pueden compartir su pantalla para demostrar algo que han hecho.


### 5. Evita las distracciones.

Desactiva las notificaciones en los dispositivos que estés utilizando y en tu teléfono. Ver las notificaciones parpadear en la pantalla te distrae a ti y a tus estudiantes. Abre sólo el software, las aplicaciones y las páginas web que vayas a utilizar durante la clase. Cierra cualquier otra aplicación, incluidos el correo electrónico y las redes sociales. Ten en cuenta qué imagen de escritorio y salvapantallas utilizas porque acabarás compartiéndolos con la clase y en el vídeo si grabas la lección.

Es importante que tu ayudante o co-docente trabaje para resolver las dudas y problemas que puedan tener tus estudiantes durante la clase, de modo que las interrupciones sean ordenadas y sirvan a la lección en lugar de cortar su fluidez.
Acuérdate también de dar instrucciones sobre cómo participar, cómo hacer preguntas y qué herramientas utilizar antes de empezar la demostración en vivo ([ver consejo número 1](#1.-Que-te-vean-y-te-escuchen)).

Por último, pide a tus estudiantes que reduzcan el número de distracciones en sus dispositivos, como notificaciones, correos electrónicos y otras pestañas del navegador que puedan tener abiertas mientras tiene lugar la clase. No puedes controlar lo que hacen, pero hacer una petición amistosa puede ayudarles a cerrar estos distractores.

### 6. Sigue el material de la lección.

Es importante que te ajustes bastante al plan de la lección y que practiques la técnica de codificación en vivo, sobre todo si es la primera vez que impartes la lección. Añade notas a tus impresiones del material de la clase, o tenlas fácilmente disponibles en la segunda pantalla o dispositivo (tableta o portátil), si utilizas uno.

Una vez que el material te sea familiar, puedes y debes empezar a improvisar basándote en los antecedentes de tus estudiantes, sus preguntas en clase y lo que te parezca más interesante.

Si surge una pregunta o un "¿qué pasaría si...?", pero no quieres interrumpir el flujo de la lección, o sabes que te llevará más tiempo del que tienes, o necesitas algo de tiempo para ordenarte, pide a tus estudiantes que las agreguen en un documento compartido en línea o pide a tu co-docente o ayudante que las registre. Luego, puedes pensar en ellas mientras tus estudiantes hacen los ejercicios y responderlas después que terminen, o a la clase siguiente.


### 7. Convierte a tus estudiantes en co-docentes

Durante la codificación participativa en vivo, las/os estudiantes programan activamente junto con el docente.  Esto puede ser un reto en la enseñanza en línea y más aún con principiantes.

Una herramienta valiosa para disminuir esta dificultad es utilizar las salas de reuniones que ofrecen Zoom o Meet (incluso en su versión gratuita). La enseñanza entre pares es la práctica docente escalable más eficaz que conocemos. Podemos utilizarla para reforzar la lección que dimos usando programación en vivo. 

Las salas de reuniones de Zoom hacen que esto sea relativamente fácil de ejecutar en línea: se tarda entre 15 y 30 segundos en meter a todo el grupo en las salas. En una clase de cuarenta personas, uno o dos tendrán dificultades al principio, pero ayuda a mantener a tus estudiantes motivados y atentos.

Yo utilizo esta dinámica con los principiantes cuando hago live coding:

* Hago entre 10 y 20 minutos de live coding.
* Los envío a la salas en grupos de 3 o 4 estudiantes (los grupos más grandes crean subgrupos, o bien alguien no participa) para resolver un ejercicio.
* El ejercicio es el mismo o muy similar al que intentamos hacer durante mi programación en vivo.
* Antes de ir a la sala, doy las instrucciones: cuánto tiempo tienen para resolver el ejercicio (entre 10 y 20 minutos), como se den organizar: un estudiante comparte una pantalla, y programan juntos para resolverlo.
* Tomo el tiempo (ahora la herramienta de videoconferencia lo hace por mí), y cuando se acaba el tiempo, vuelven a la sala común, y hablamos de cómo ha ido, qué problemas y preguntas tienen. Repasamos estos detalles. Es un buen momento para dejarles compartir la pantalla para ver sus problemas o soluciones, sobre todo si han resuelto el ejercicio de forma diferente.

Esta estrategia les permite reforzar el aprendizaje porque programan durante mi live coding y luego una vez más en grupo.

Puedes utilizar diferentes [tipos de ejercicios](https://educarencomunidad.tech/es/index.html#s:exercises) para el trabajo en grupos, como rellenar los espacios en blanco, problemas de Parson y tutoriales interactivos que ofrezcan diferentes tipos de andamiaje.

### 8. Obten información en tiempo real y proporciona ayuda inmediata.

Al programar en vivo en línea puede resultar difícil saber si tus estudiantes están siguiendo el proceso o si están teniendo dificultades para programar que aún no se hemos solucionado.

Una forma de comprobarlo es ofrecer a tus estudiantes una manera diferente de indicarnos su estado. Cuando enseñamos en persona, utilizamos notas adhesivas de colores. Algunas opciones para enseñar en línea son:

* El feedback no verbal en plataformas de videoconferencia aparece como la primera opción para sustituir a las notas adhesivas de colores. Si utilizamos Zoom, se puede pedir a una persona que marque con una marca verde si ha terminado o con una marca roja en caso de que esté atascada. Al igual que con las notas adhesivas, estas marcas no se quitan solas, por lo que es necesario pedir a la persona que las quite si ya ha resuelto el problema o que pase a otro ejercicio.

* Crea una tabla en el documento colaborativo (utilizando [HackMD](https://hackmd.io) o google docs) con los nombres de todos los participantes. Pídeles que pongan un check verde o una cruz roja para comprobar si van por buen camino. Puedes comprobar si alguien no ha rellenado algo.

* En zoom, las otras reacciones con emojis son útiles para un estado general rápido porque también nos muestran el número de cada emoji en la lista de participantes. Pero estos emojis se limpian al cabo de un rato, por lo que puedes perderte alguna información. Con el mismo propósito, también podemos pedirles que escriban en el chat cuando terminen una tarea. Aunque puede ser mucha información junta en grupos de más de 20 personas y complicado determinar quién no contestó.

* Se pueden utilizar otras herramientas, como encuestas o un canal paralelo de Slack, pero agregar más herramientas a la clase sincrónica, sobre todo si es una herramienta nueva, es una carga cognitiva que debemos considerar.

* Algunos temas permiten agregar en el código un elemento de aleatoriedad que va a dar resultados diferentes en diferentes máquinas o entornos y podes preguntarle a tus estudiantes si sus resultados son iguales a los tuyos. Cuando enseño gráficos de redes, el algoritmo es no determinístico por o que el gráfico que obtienen mis estudiantes suele ser diferente al mio, muchas veces no necesito preguntar, el chat se inunda con mensajes avisando que sus gráficos son distintos. De esta forma sabrás que te siguen.

Una vez más, enseñar con otras personas es una buena estrategia para este consejo. El papel principal de tus co-docentes es garantizar que tus estudiantes no se queden atrás debido, por ejemplo, a problemas técnicos. A veces es una buena idea crear una sala para resolver problemas técnicos donde tu estudiante y co-docentes puedan ir y resolver el problema. Tus ayudantes deben prestar atención a los documentos compartidos, los emojis o el canal de Slack, que indican que un/a estudiante está pidiendo ayuda.

### 9. Usa ilustraciones, aún mejor dibujalas en tiempo real.

Los diagramas y mapas conceptuales pueden ayudar a tus estudiantes a comprender las etapas de la lección y a organizar el material. Generar los diagramas junto con tus estudiantes a medida que avanzas en el material puede funcionar muy bien. Hay varias herramientas para hacerlo en línea (Miro, Jamboard, Whiteboard.fi, draw.io y excalidraw, entre otras). Puedes usarlo con el ratón o con una tableta (yo uso la Wacom One, que es estupenda).

Puedes construir diagramas, haciéndolos cada vez más complejos en paralelo con el material que enseñas. Presentar información complementaria utilizando representaciones visuales y verbales ayuda a aprender (conocido como "codificación dual").  

Por ejemplo, yo solía dibujar un mapa conceptual del código de control de flujo con mis alumnos para hablar de los conceptos esenciales antes de hacer la codificación en vivo. También dibujo un mapa del orden de ejecución de una sentencia SQL para explicar el resultado de una consulta o por qué debemos utilizar una función y no otra después de hacer el live coding.

Algunas herramientas permiten escribir y dibujar sobre la pantalla compartida. Esto puede ser útil para marcar parte del código y anotar el valor de una variable mientras ejecutas un fragmento de código o los pasos y el orden de ejecución de una sentencia.

### 10. Acepta tus errores.

Aunque te sepas bien la lección y la sigas, es muy probable que cometas errores mientras demuestras cómo programar en vivo.  Cometer errores suele ser el mayor temor de los/as docentes que utilizan esta técnica. Está bien que ocurra (ya que es lo que pasa en la vida real cuando programamos), y puede ser una excelente oportunidad para aprender a depurar. Esta forma de afrontar los errores se denomina "encuadre positivo del error", y es beneficiosa para el aprendizaje.

Cuando se produzca un error, detente, léelo en voz alta y explica cómo has determinado lo que ha ocurrido.  Marca qué parte del texto del error te da una pista que te ayuda a diagnosticarlo y resolverlo. A continuación, vuelve al código y muestra qué elemento o elementos del código arrojan el error. Es útil aclarar qué hace cada parte del código creando nuevos ejemplos que muestren por qué se produce un error en una situación y no en otra. También puedes involucrar a los estudiantes en la resolución de problemas preguntándoles qué creen que ha fallado y cómo solucionarlo.

Si tiene tiempo, utilice el error para hacer una "búsqueda en vivo".  En esta lección, enseñas cómo buscar un error en Internet, afinar esa búsqueda, leer los resultados y determinar cuál es el que más se acerca a tu problema.  Aquí puedes enseñar cómo leer la ayuda y las preguntas y respuestas de Stack Overflow.

También, como se mencionó en puntos anteriores, si un/a estudiante tiene un error, puedes pedirle que comparta su pantalla, y toda la clase trabaja en conjunto para resolverlo usando estas estrategias.

Una vez que hayas dado una clase varias veces, es poco probable que cometas algo más que errores básicos de tipeo (que pueden seguir siendo informativos). Puedes intentar recordar errores pasados y cometerlos deliberadamente, pero eso puede parecer forzado. Un método alternativo es el twitch coding: pedir a los alumnos que te digan uno por uno qué tienes que escribir a continuación. Es casi seguro que te meterás en algún lío.

## Conclusiones.

La programación participativa en vivo es utilizada con éxito por miles de docentes en todo el mundo, enseñando programación, diferentes aplicaciones y herramientas de software.  Como cualquier otra estrategia de enseñanza, requiere práctica pero es muy útil para obtener mejores resultados para ti y tus estudiantes.   

Aquí tienes dos vídeos de ejemplo contrastando [online live coding hecho mal](https://youtu.be/9ca6FxIdM6w) y [online live coding hecho bien](https://www.youtube.com/watch?v=NmPENPBnYy4).

En esta charla relámpago (en inglés) de CarpentryCon 2022 [Managing Real Estate: Best practices to teach live coding](https://youtu.be/cg_ysne1Q_w), Jennifer Stubbs hizo un excelente resumen de consejos para hacer live coding.


## Agradecimientos.

Gracias a Paola Corrales y Elio Campitelli por sus comentarios sobre un primer borrador de este artículo y a Shern Tee por sus comentarios que enriquecieron este post.

Gracias a Rainier Barrett, Lieke de Boer, Kristin Lee, Jonathan Wheeler y Jannetta Steyn por discutir la logística de la programaicón en vivo en línea durante nuestra formación para convertirnos en formadores de The Carpentries.  
 