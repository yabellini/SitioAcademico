---
title: Proyectos de GitHub para ordenar el trabajo
author: Yanina Bellini Saibene
summary: "En mi rol de community manager de rOpenSci he estado usando diferentes caracteristicas de GitHub para realizar mi trabajo.  En esta serie de blog post les voy a compartir que uso y como para poder gestionar mis comunidades"
date: '2023-10-05'
tags:
  - Spanish
  - community
  - GitHub
---


{{< figure src="featured.png" alt="Github Octocat">}}


En [rOpenSci](https://ropensci.org) programamos actividades relacionadas con eventos y contenidos, por ejemplo los articulos de blog que vamos a escribir, las sesiones de cotrabajo que vamos a realizar y los posteos que vamos a hacer en redes sociales. Tambien tenemos actividades en las cuales solicitamos la opinion y la ayuda de la comunidad, como las community calls y las traducciones.  

La [mayoria de nuestras actividades utilizan GitHub](https://github.com/ropensci), porque somos una organizacion que se dedica al software libre cientifico y el codigo fuente de ese software se encuentra mayormente en esta plataforma.  

GitHub también ofrece herramientas para gestionar proyectos a través de las Organizaciones. En este blog post, exploraremos qué son los Proyectos en GitHub, cómo puedes crear uno para mantener tu trabajo en equipo organizado con ejemplos sobre como los usuamos en rOpenSci.

## ¿Qué son los Proyectos en GitHub?

Los Proyectos en GitHub son herramientas visuales que te permiten organizar y dar seguimiento a las tareas de tu proyecto en una especie de planilla que luego se puede ver como un tablero. Estos tableros contienen columnas que representan diferentes etapas del trabajo o diferentes categorias de o estado de las actividades.  Por ejemplo [en nuestras actividades de traduccion](https://github.com/orgs/ropensci/projects/7) las columnas se llaman: , "Todo - Automatic Translation", "Todo - First Review", "Todo - Second Review" y "To be merge". Cada tarea se representa como una tarjeta que puedes mover entre las columnas para reflejar su estado actual.

## Creando un Proyecto en una Organización

### Paso 1: Accede a la Organización

Inicia sesión en GitHub y navega hasta la página principal de tu Organización. Si aún no tienes una, puedes crear una nueva desde tu cuenta.

### Paso 2: Dirígete a la pestaña "Projects"

En la barra de navegación de tu Organización, busca y haz clic en la pestaña "Projects". Aquí es donde podrás crear y gestionar proyectos para tu equipo.

### Paso 3: Crea un Nuevo Proyecto

Haz clic en el botón "New project" para comenzar la creación de un nuevo proyecto. Selecciona el tipo de plantilla que se ajuste a tus necesidades, como "Automated kanban" para un tablero simple o "Basic template" para mayor personalización.

### Paso 4: Configura el Proyecto

Ingresa un nombre descriptivo para tu proyecto y personaliza las columnas según el flujo de trabajo de tu equipo. Puedes agregar notas, etiquetas y asignar responsables a cada tarjeta para mayor claridad.

Por ejemplo, en el proyecto que tenemos para gestionar las publicaciones en nuestras redes sociales las columnas son: 

* _Title:_ de que se trata el posteo.
* _Status:_ tiene como opciones "Schedule" o "Done", que indica si es post ya se publico o todavia esta en la lista.
* _Labels:_ tiene una etiqueta por red social (linkedin, mastodon) y una para saber si es un borrador o un tipo especial de posteo como las publicaciones de los Jueves donde seleccionamos un articulo de blog viejo y lo volvemos a compartir con la comunidad.

### Paso 5: Guarda el Proyecto

Haz clic en el botón "Create project" para finalizar la configuración. ¡Ahora tienes un tablero organizado para gestionar las tareas de tu proyecto!

## Gestión Eficiente del Proyecto

Con tu proyecto listo, puedes agregar tarjetas (o filas segun el tipo de vista que hayas seleccionado) para representar tareas, errores, características pendientes, o como nuestros ejemplos capitulos a revisar o posteos a realizar en una red social. Se pueden asignar tareas a diferentes personas, etiquetar cada actividad con categorías relevantes, en nuestros ejemplos con la red social donde debe publicarse el post y se pueden mover las tarjetas entre columnas a medida que avanzas en el proyecto, en nuestro ejemplo de las traducciones cuando terminamos de realizar el review de algun capitulo.

Tambien se puede asociar las diferentes tareas se a _issues_ o _pull request_ o bien pueden generar _issues_ a partir de una tarea en la lista.

Los Proyectos en GitHub no solo proporcionan una forma visual de gestionar el trabajo, sino que también mejoran la colaboración y la transparencia en las actividades que debes realizar, no solo en el desarrollo de software pero tambien como en nuestro caso con tareas de gestion de la comunidad como por ejemplo manejar las traducciones voluntarias de libros u agendar y organizar los posteos en redes sociales.

