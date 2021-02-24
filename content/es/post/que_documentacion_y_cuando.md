---
date: "2021-02-23"
draft: true
type: page
linktitle: Tipos de Documentación de acuerdo al nivel de conocimiento
summary: Una versión resumida y en español de dos post de Greg Wilson y una presentación de Allison Presman Hill.
title: Tipos de Documentación de acuerdo al nivel de conocimiento
authors: 
    - admin
type: post
weight: 1
tags: 
  - MetaDocencia
  - Educación
---

Estamos desarrollando nuevos cursos en [MetaDocencia](www.metadocencia.org) y una de las secciones del curso de [Enseñar a Programar]() se refiere a enseñar como buscar, pedir e interpretar diferentes tipos de ayuda.

Una de mis lecturas obligadas sobre temas relacionados a la educación de la computación y la informática es el [blog de Greg Wilson](https://third-bit.com/) donde el autor publicó dos post ([What Docs and When](https://third-bit.com/2019/04/10/what-docs-and-when/) [What Docs When](https://third-bit.com/2019/04/16/what-docs-when/)) donde resume en dos diagramas qué tipo de documentación es más adecuada para utilizar de acuerdo al nivel de conocimiento que tengas sobre el tema específico que quieres aprender y con conocimientos generales de la disciplina donde se aplica ese tema, en los post se refiere a Ciencia de Datos, Tidyverse, etc.  Más tarde, tuve la oportunidad de disfrutar de una charla de Allison Presman Hill sobre [Aprender sin una red](https://alison.netlify.app/latinr-learn/#1) donde utiliza estos diagramas publicados por Greg para aconsejar como aprender de forma autónoma (por eso sin una red) sobre un tema en particular.

En este post les comparto uno de los diagramas en español (y con algunas adaptaciones menores) y las definiciones de cada tipo de documentación también en nuestro idioma y con ejemplos en castellano.  

Como siempre espero que sea de utilidad.  Los comentarios son muy bienvenidos.


## Diagrama

El siguiente diagrama muestra cómo diferentes tipos de materiales ayudan a diferentes personas.


{{< figure src="/img/DocType_es.png" >}}

El diagrama divide el plano en tres etapas del modelo de desarrollo cognitivo:

* Una persona _principiante ó novata_ aún no tiene un modelo mental del dominio. No saben lo que no saben, no hablan la jerga y hacen las cosas por analogía o de memoria.

* Un/a _practicante competente_ tiene un modelo mental utilizable del dominio. Pueden realizar tareas de rutina y resolver problemas de rutina, saber dónde buscar para encontrar más información y pueden reconocer soluciones a sus problemas cuando las encuentran.

* Una _persona experta_ tiene un modelo bastante completo y densamente conectado del dominio. Pueden resolver problemas comunes de un vistazo y descubrir los casos extraños o pocos comunes.

El **eje X** es el conocimiento general del usuario, por ejemplo sobre R, tidyverse y ciencia de datos. El **eje Y** es qué tan bien comprenden el problema particular que están tratando de resolver.
 
Cada flecha indica un tipo de material que es adecuado para la conjunción de cada etapa de desarrollo cognitivo y hacia cual te puede ayudar a alcanzar. Los materiales que se presentan en el gráfico son:


1. Un **cómo se hace** es una receta paso a paso para resolver un problema en particular. Las personas principiantes pueden usarlo sin entender el _"por qué"_ detrás de cada paso.

2. Una **intro** es una descripción general que ayuda a que las personas se enteren que algo existe. Las introducciones pueden presentarse en *seminarios web*, la *primera parte de un taller o curso más largo*, como *presentaciones de marketing*, como *parte de un libro*, como una *viñeta* (vignette) o como parte de una *guía rápida* (cheatsheet).

3. Un **tutorial** es una lección planificada que ayuda a las personas a construir un modelo mental sobre un dominio y adquirir  habilidades básicas para que puedan comenzar a abordar problemas de interés. Los tutoriales mueven a las personas de novatas a competentes.  Los tutoriales pueden presentarse en forma de *talleres*, *libros*, *charlas principales en conferencias*, *blog post* ó *notebooks* (incluidos paquetes y sitios shyni de {learnr}). 

4. Una **traducción** presenta cómo hacer con la herramienta Y lo que alguien ya sabe hacer con la herramienta X. Aprovecha la comprensión de un tema para aumentar la comprensión de otro.

5. Las **notas de nueva versión** y las **actualizaciones** son para falsos/as principiantes: asumen una comprensión general y completan lagunas de conocimiento identificadas previamente.

6. Los **manuales y referencias** asumen que la persona sabe lo que está buscando, pero no recuerda o nunca conoció los detalles. Siguen siendo útiles sin importar cuánto se avance.
    
7. Los instructivos **paso a paso** contienen ejemplos resueltos y asume que la/el usuaria/o sabe lo suficiente para generalizar a partir de una serie específica de pasos para resolver un problema en particular. Las *listas de verificación* también se incluyen aquí los **sitios de preguntas y respuestas** al estilo Stack Overflow, porque son útiles cuando las personas saben lo suficiente como para hacer una buena pregunta y como reconocer una buena respuesta. 
    
8. Los **casos de estudio** y los **ensayos** contienen estudios de uno o varios casos en particular, con el punto de vista del/la autor/a como valor agregado.  Es necesario contar con un modelo mental bien formado y denso para poder aprovechar este tipo de material.