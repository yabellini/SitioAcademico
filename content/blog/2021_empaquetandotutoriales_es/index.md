---
date: "2021-05-17"
draft: false
summary: un paquete es una de las maneras de publicar tu tutorial de learnr, en este blog post te explicamos como generar un paquete para tu tutorial.
title: Empaquetando tutoriales
categories:
  - Community
  - Education
  - Español
tags: 
  - Community
  - Education
  - Package
---
{{< figure src="/media/paquete.jpg" alt="Empaquetando tutoriales interactivos">}}
_Fuente de la imágen:_ <a href='https://www.freepik.es/vectores/negocios'>Vector de Negocios creado por vectorjuice - www.freepik.es</a>

Empaquetar los tutoriales es una excelente alternativa para hacer llegar nuestras lecciones interactivas a un grupo grande de usuarios; una vez que se ha instalado el paquete, se puede ejecutar localmente.  Esto evita los costos de publicar los tutoriales como aplicaciones Shiny y posible problemas en la conexión a Internet. Como es un paquete, también puede contener datos propios para trabajar durante las lecciones.

En este post les comparto el paso a paso para crear un paquete para sus tutoriales de `learnr`. 

### Cómo hacer un paquete para un tutorial {learnr}

Nuestro objetivo es que puedas generar un paquete mínimo para tu tutorial y que el mismo sea descargable e instalable por tus usuarios y estudiantes.  La forma más rápida de lograr este objetivo es usando GitHub como lugar para almacenar tu paquete (aunque se puede realizar con otras plataformas).  

Para realizar este paso a paso, estoy asumiendo los siguientes pre-requisitos:

* Tienes una cuenta de [GitHub](https://github.com/) y podes usar GitHub desde RStudio (solo es necesario un conocimiento básico de git).
* Estás comoda/o con conceptos básicos de uso de R y RStudio.
* Entiendes cómo funcionan los proyectos de R.
* Entiendes los conceptos básicos de Rmarkdown.
* Estás familiarizada/o con la creación de tutoriales con {learnr}.

### Paquetes necesarios

Tenes que tener instalados y cargados lo siguientes paquetes: `devtools, usethis, roxygen2, learnr`

### Generando el repositorio de GitHub

Este paso a paso nos permitirá generar el repositorio de GitHub y el proyecto de RStudio para generar nuestro paquete.

_Nota: Para quienes quieran aprender más sobre Git y proyectos de RStudio pueden leer [este post](https://yabellini.netlify.app/es/post/githubconr/) o mirar y seguir [este curso](https://yabellini.netlify.app/es/courses/tallerdegitconr/)._

**1. Crear un nuevo repositorio en GitHub.** El nombre del repositorio que elijas terminará siendo el nombre de tu paquete, asi que seleccionemos con cuidado.

**2. Copia la URL del repositorio en tu portapapeles.** Para esto hacer clic en el botón verde _Clonar (Clone)_ o _Descargar (Download)_. Copia la _URL HTTPS_ (se parece a: https://github.com/{tuusuariodegit}/{elnombredeturepo}.git ).

**3. Abre RStudio y crea un nuevo proyecto de RStudio a través de git clone.** Hacer esto haciendo clic en _File> New project> Version Control> Git_. Pegar la URL copiada. Seleccionar con cuidado la carpeta dónde RStudio creará este nuevo proyecto.

**4. Hacer clic en Crear proyecto.** Tu proyecto R ahora está conectado a GitHub
    
### Agregar archivos y carpetas para un paquete

Ahora crearemos la estructura para convertir este proyecto de R en un paquete. 
1. La infraestructura de paquetes básica necesaria se creará cuando ejecutes el siguiente código: 

`usethis::create_package("<ruta_a_carpeta/nombre_del_paquete>")`


2. La salida de la consola te preguntará si quieres sobrescribir el proyecto R preexistente. Selecciona _No_. El detalle de la salida en la consola se puede ver en la siguiete figura.

{{< figure src="/media/empaquetando_1.png" alt="Salida de la consola luego de ejecutar el comando usethis::create_package. Se presentan 3 opciones de las cuales se debe seleccionar No.">}}

3. Se abrirá una segunda sesión de RStudio. Esta sesión tiene una pestaña de _Build_ en el panel que también tiene las pestañas de _Environment_, _History_, etc. Esta pestaña es específica para construir paquetes, y la usaremos más adelante. Puedes cerrar la primera instancia de RStudio.

### Agregue archivos y directorios para un tutorial

Ahora vamos a agregar el contenido del tutorial.  

1. Creemos el tutorial ejecutando este código:

`usethis::use_tutorial("<nombre-del-tutorial>", "<Título del Tutorial")`

El primer argumento es el nombre del archivo `learnr` sin la extensión .Rmd. El segundo argumento es el título del tutorial que verán los usuarios.

{{< figure src="/media/empaquetando_2.png" alt="Salida de la consola luego de ejecutar el comando usethis::use_tutorial.">}}

Esto crea un directorio `inst/` con algunas subcarpetas. Esta es la estructura tradicional de los tutoriales `learnr`, no cambia por estar en un paquete. 

2. Puedes abrir la carpeta `inst/` y sus subcarpetas hasta llegar al archivo .Rmd que creamos:

`/inst/tutorials/<nombre-del-tutorial>/<nombre-del-tutorial>.Rmd`
    
3. Puedes editar ese archivo para generar tu tutorial o bien copiar allí otros archivos .Rmd que ya tengas armados de tus tutoriales.

Los pasos 1 a 3 deben ser repetidos tantas veces como tutoriales queramos incluir en este paquete.

### Crear, instalar y usar tu paquete con tutoriales {learnr}

Ahora tenemos que generar el paquete e instalarlo para poder usarlo.

1. Se puede generar desde el panel o menu _Build_ de RStudio, haciendo clic en _Install and Restart_ (instalar y reiniciar).

2. También se puede hacer por código: 

    `devtools::install()`

¡Listo! Ya creamos un paquete con un tutorial interactivo. Para probar que nuestro paquete se ha creado correctamente vamos a cargar el tutorial desde el paquete instalado siguiendo estos pasos:

3. Todos los tutoriales `learnr` se indexan y muestran automáticamente en el panel _Tutorial_ de RStudio.  Al hacer click en _Start Tutorial_ (iniciar tutorial), se ejecutará el tutorial en dicho panel (se puede agrandar o abrirse en una ventana en el navegador).

{{< figure src="/media/empaquetando_4.png" alt="Pestaña tutorial dentro de RStudio con el Tutorial que creamos.">}}

4. También se puede ejecutar por código con la forma `learnr::run_tutorial("<nombre-del-tutorial>", "<nombre-del-paquete>")`.

El nombre del tutorial aquí se refiere al nombre del archivo .Rmd, no al título que se presenta al usuario.  En este ejemplo:

`learnr::run_tutorial("TextMining", package = "TextMiningTutorial")`

El tutorial se abrirá en una ventana del navegador local.

### Publicando tu tutorial

Llegó el momento de compartir nuestro paquete con tutoriales interactivos con el mundo y para eso debemos publicarlo en GitHub.

1. Si hasta el momento no lo has hecho, ahora necesitamos hacer _commit_ y  _push_ a GitHub.  Esto lo hacemos desde el panel _Git_ en RStudio.

2. En el `README.md` agregar las instrucciones para la instalación y ejecución de tu tutorial como se presenta en la imágen de ejemplo:

{{< figure src="/media/empaquetando_3.png" alt="Readme.md con las instrucciones para instalar el paquete">}}

Esas instrucciones deben incluir:

* Como instalar el paquete `learnr` y el paquete `remotes` (en caso que no los tengan instalado)
* El código para instalar el paquete: `remotes::install_github("github/nombre-del-tutorial")`, para el ejemplo sería:

`remotes::install_github("yabellini/TextMiningTutorial")`

* Instrucciones para ejecutar el tutorial, indicando tanto el uso del panel Tutorial, como la ejecución por código, como este ejemplo:

`learnr::run_tutorial("TextMining", package = "TextMiningTutorial")`

### Trabajo terminado

Con estos pasos terminamos de generar un tutorial de learnr en un paquete.  Cada vez que actualicemos o cambiemos algo, deberemos generarlo de nuevo usando _Build_ y luego _Install_ y _Restart_ el paquete localmente antes de hacer _Commit_ y _Push_ de estos cambios a GitHub.

### Fuentes

1. [How to deliver learnr tutorials in a package. Desirée De Leon](https://education.rstudio.com/blog/2020/09/delivering-learnr-tutorials-in-a-package/)

2. [Empaquetando tutoriales interactivos. Yanina Bellini Saibene](https://yabellini.netlify.app/es/post/empaquetandotutoriales/)

3. [Primeros pasos de Git con R.  Yanina Bellini Saibene, Marysol Gatti ](https://yabellini.netlify.app/es/post/githubconr/)
