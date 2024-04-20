---
title: "Tercer Encuentro. Aprendiendo a Programar en 30 lecciones"
weight: 3
subtitle: "Tercer encuentro"
excerpt: "Mi sobrino de 14 años quiere aprender a programar y yo voy a enseñarle. En esta clase aprendimos que son los proyectos y como nos pueden ayudar a ordenar nuestro trabajo, tambien vemos que es Rmarkdown y como leer y mirar los datos que vamos descargamos la clase pasada."
date: 2024-03-09
draft: false
categories:
  - Español
  - rstats
  - Education
  - 100DaysToOffload
tags: 
  - Education
  - rstats
  - Español
  - 100DaysToOffload
---

En esta clase aprendimos que son los proyectos y como nos pueden ayudar a ordenar nuestro trabajo, tambien vemos que es Rmarkdown y como leer y mirar los datos que vamos descargamos la clase pasada.

## Ordenando nuestro trabajo

### Proyectos

Cuando empezamos a trabajar en un proyecto de programacion vamos a ir generarndo diferentes resultados y productos intermedios hasta que terminemos, ademas de nuestros datos y nuestro codigo, tendremos, por ejemplo graficos y diferentes reportes.

Es una buena practica mantener todos los archivos asociados a un proyecto en un mismo lugar. RStudio cuenta con soporte integrado para esto por medio de los proyectos.

#### ¿Qué ventajas tiene?

-   Te permite "cuidar" los datos que usas al ordenarnos en carpetas que diferencien entre la versión originaly los datos que transformaste y limpiaste o los resultados finales.
-   Te permite compartir tu trabajo de forma mas sencilla con otras personas. Solo tendrías que compartir la carpeta del proyecto sabiendo que incluye todo lo necesario para que cualquiera reproduzca tu análisis.
-   Te permite publicar de manera ordenada tu código si vas a presentar o publicar tu trabajo.
-   Te permite continuar con lo que estabas haciendo hace una semana o hace un mes como si el tiempo no hubiera pasado. De alguna manera es un regalo para tu yo futuro.

#### Creando un proyecto

Vamos a crear un proyecto de RStudio para usarlo durante el resto de este curso.

Hace clic en **File \> New Proyect** (significa que crearemos un proyecto nuevo), y después en la primera ventana selecciona **New Directory** (par crear una carpeta nueva en tu disco rigido para almacenar todo ), en la segunda **Empty Project** (porque es un proyecto vacio).

> Nota: podes seleccionar en que lugar de tu disco vas a crear esa carpeta. Para las personas que usan Windows la recomendacion es que NO usen la carpeta *Descargas* o la carpeta *Escritorio*. Pueden utilizar la carpeta *Documentos* para guardar sus proyectos.

Vamos a poner el nombre de la carpeta que alojará a tu proyecto, por ejemplo "ProgramacionConR" y hacé click en **Create Project** ("Crear Proyecto").

Si todo salió bien, ahora deberías tener una nueva carpeta que se llama *ProgramacionConR*. Pero si bien es una carpeta común y corriente, le llamamos proyecto porque además contiene un archivo con el mismo nombre *ProgramacionConR.Rproj* (o solo *ProgramacionConR* si en tu computadora no ves la extensión de los archivos).

Podemos ver que el nombre del proyecto aparece arriba a la derecha de la IDE y tambien podemos ver en el tab Files la nueva carpeta con el archivo .Rproj. Si salimos de RStudio y usamos el explorador de archivos de la computadora y navegamos hasta la carpeta que recien creamos con el archivo del proyecto.

> #### Primer ejercicio
>
> 1.  Dentro de RStudio, en el Tab **Files** seleccionamos **New Folder**. Vamos a crear una carpeta llamada **datos**.
> 2.  Ahora por fuera de RStudio, utilizando el explorador de archivos, miremos el contenido de la carpeta **ProgramacionConR** en nuestro disco rigido. Que paso?
>
> Si todo esta bien, tenemos que ver la carpeta *datos* ademas el archivo *ProgramacionConR.Rproj*.

Podemos crear tantas carpetas y archivos como necesitemos. Nuestro proyecto va a evolucionar a medida que avanzamos.

#### Abrir un proyecto

Cada vez que salgamos de RStudio, tendremos que volver a abrir nuestro proyecto. La manera más simple de abrirloes entrando en la carpeta que lo contiene y haciendo doble click sobre el archivo *ProgramacionConR.Rproj*. Al hacer esto se abrirá RStudio y la sesión de R en la misma carpeta y, por defecto, cualquier archivo que quieras abrir o guardar lo hará en esa misma ubicación. Esto ayuda a mantener tu trabajo ordenado y que luego sea simple retomar o compartir lo que hiciste.

RStudio permite tener varios proyectos abiertos, y esto es posible porque justamente cada proyecto tiene su propia carpeta. Si en algún momento trabajas con proyectos en paralelo vas a poder hacerlo sin que el código o los resultados de un análisis interfieran con otro.

> #### Segundo ejercicio: Abrí tu nuevo proyecto desde el explorador de archivos
>
> 1.  Cerrá RStudio
> 2.  Desde el explorador de archivos, buscá la carpeta donde creaste tu proyecto.
> 3.  Hacé doble click en el archivo que tiene el nombre de tu proyecto (y que termina con *.Rproj*) que encontrarás en esa carpeta.

### Borrón y cuenta nueva... todos los días!

Vamos a configurar RStudio para que nos ayude a seguir ordenandonos con la idea de poder replicar el analisis que vamos a hacer. Nos vamos a ocupar en que al menos en tu computadora puedas repetir los cálculos o el análisis desde cero.

Y además de organizar proyectos y no modificar los datos originales, ¿cómo podés asegurarte de que guardaste todo el código que estuviste escribiendo y usaste?

La manera más directa es reiniciar la sesión de R y correr el código de nuevo, si da error o no devuelve lo que esperabas significa que te faltó guardar algún paso.

> Tip: Podés reiniciar la sesión de R con el atajo `Ctrl+Shif+F10`

Esto puede pasar si por ejemplo leés una base de datos en memoria pero no guardás el código que lo hace. Mientras estemos trabajando, R tendrá esa base de datos en memoria y podremos hacer cálculos y gráficos.

Por defecto además RStudio va a recordar las variables que estés usando mañana o pasado en un archivo oculto (.RData) a menos que le indiques lo contrario.

Y si bien suena práctico volver a R al otro día y tener el análisis tal cual lo dejamos, esto puede significar que nunca nos demos cuenta que nos faltó guardar una línea de código clave en nuestro análisis.

> #### Tercer ejercicio: Configurá RStudio
>
> 1.  Hacé click en el menú **Tools (Herramientas)** y luego **Global Options (Opciones globales)**.
> 2.  Destildá la opción **Restore .RData into workspace at startup (Recuperar .RData al inicio de la sesión)**.
> 3.  Hacé click en **Apply (Aplicar)**.

## Objetivo final de nuestro curso

A partir de ahora vamos a empezar a trabajar con nuestro proyecto de curso. El objetivo final es poder realizar un analisis de un conjunto de datos que ustedes elijan. Este analisis debera contener lectura y limpieza de datos, visualizaciones, reportes y un sitio web con la publicacion de los resultados.

Para ver un ejemplo del tipo de resultado que podemos obtener vamos a revisar este proyecto sobre los Pingüinos Papúa.

> #### Cuarto ejercicio: Explorar el proyecto de los Pingüinos
>
> 1.  Descarga el archivo [rstudio-project-pinguinos.zip](rstudio-project-pinguinos.zip) que contiene el proyecto y descomprimirlo.
> 2.  Abrir el proyecto project.Rproj.
> 3.  Analizar su estructura (que carpetas y archivos tiene el proyecto?)

Hasta la clase pasada todo el codigo que escribimos lo hicimos en la consola, por lo que lo perdimos todo cuando cerremos RStudio. Para poder volver a utilizarlo tenemos que guardarlo. Para ello utilizamos R Scripts y archivos RMarkdown o archivos Quarto.

Vamos a tener nuestra primera experiencia con archivos RMarkdown, así que vamos a ver qué es un documento RMarkdown. En el proyecto de los pinguinos que recien abriste te preparamos un reporte de ejemplo, por favor abri el archivo [reporte_pinguinos.Rmd](rstudio-project-pinguinos/reporte_pinguinos.Rmd). El archivo aparecerá en un nuevo panel arriba en el lado izquierdo de la pantalla, y el panel de la consola se moverá hacia abajo.

## RMarkdown

Un archivo RMarkdown es un archivo de texto plano, con algunas reglas y una sintaxis especial que nos permite escribir código y texto juntos - ya usamos markdown cuando creamos el archivo readme de nuestro repositorio de github. Cuando se "teje" (knit), el código se evaluará y ejecutará y el texto se formateará de manera que se cree un informe o documento reproducible que sea agradable de leer y que contenga todo tu trabajo.

Esto es crítico para la reproducibilidad de nuestro trabajo. También nos ahorra tiempo y puede ayudar en las tareas de automatización. Este documento recreará tus figuras por ti en el mismo documento donde estás escribiendo el texto que las explica. Esto te ahorrará el esfuerzo de hacer un análisis, guardar un gráfico en un archivo, copiar y pegar ese gráfico en Word o Power Point o Google Slides, y tener que hacerlo todo de nuevo después de descubrir un error tipográfico.

Ahora veamos cómo es nuestro Informe de Pingüinos.

-   La parte superior tiene el Título y el tipo de salida (que en este caso es un documento HTML).
-   Debajo hay secciones alternas *blancas* y *grises*. Estas son las dos secciones principales que componen un archivo RMarkdown: \* Las secciones grises son el código R \* Las secciones blancas son el texto de Markdown
-   Hay texto negro, azul y verde.

> Sigamos adelante y "tejamos (knit)" el documento haciendo clic en el ovillo de hilo azul (<img src="knit-boton.png">) en la parte superior del archivo RMarkdown.

¡Acabamos de crear un archivo html! Se trata de una única página web que estamos viendo localmente en nuestros propios ordenadores. Al generar este documento RMarkdown, R ha formateado el texto markdown y ha ejecutado el código R.

<img src="markdown-knit.png" alt="Rmarkdown a la izquierda. Documento generado a la derecha"/>

### Texto markdown

Podes ver una guia sobre rmakdown [en esta guía rápida](https://raw.githubusercontent.com/rstudio/cheatsheets/main/translations/spanish/rmarkdown_es.pdf), pero aquí hay una sintaxis mínima para empezar:

-   encabezados empiezan con `#` o `##`y asi siguiendo (es importante poner un espacio después del último `#`).
-   las palabras en negrita están rodeadas de `**`
-   y las cursiva, con `_` o un solo `*`

### Código de R

El código R se escribe dentro de "chunks (trozos)" de código. Los trozos de código comienzan con `{r label}` (donde _"label"_ es un nombre opcional y único) y terminan con \```. En RStudio, podes crear un nuevo chunk con el atajo de teclado `Ctrl + Alt + I`.

Este informe muestra información sobre los pingüinos Papúa, pero podríamos cambiar algunas líneas de código para crear el mismo análisis para las otras dos especies, Adelia y Barbijo.

> Ahora es tu turno. Sigue buscando en el código, si encuentras alguna mención a "Papúa", cámbiala por cualquiera de las otras especies.

Esta tarea es un poco engorrosa si hay que cambiar muchas cosas cada vez que queremos volver a ejecutar el análisis para diferentes especies. Pero no te preocupes, aprenderemos a hacer todo más automático durante el curso.

## Leyendo y observando datos

El cnojunto de datos que usa nuestro reporte son los datos de **Pingüinos de Palmer** y fueron recogidos y puestos a disposición por la Dra. Kristen Gorman y la [Estación Palmer en la Antártida, LTER](https://pal.lternet.edu/).

Estos datos están disponibles en R instalando el paquete `palmerpenguins` (en inglés) o el paquete `datos` (en español), pero como queremos aprender a leer datos en R, vamos a leerlos desde archivos csv y xls.

## Leyendo archivos csv

Empezaremos cargando el paquete **tidyverse**, como hicimos en la clase pasada. Este paquete nos da acceso a docenas de paquetes y funciones con las que trabajar. Por ahora usaremos la función `read_csv()` para leer un archivo .csv que está almacenado en la carpeta `datos` del proyecto.

``` r 
library(tidyverse)

pinguinos <- read_csv("datos/pinguinos.csv")
```

Ya vimos que en R, los datos se almacenan en objetos. Cuando leemos un archivo csv, los datos van directo a un data.frame llamado `pinguinos` y están listos para ser utilizados. En la solapa "Environment" podemos ver el objeto `pinguinos`, y si hacemos clic en ese objeto los datos se abrirán en una nueva pestaña para que veamos que pinta tiene.

<img src="view_en_rstudio.png" alt="La pestaña de visualización del data.frame con los datos de pinguinos luego de llamar a la función View()" />

Esta previsualización es lo más parecida a la que tenemos en una hoja de cálculo. Podemos llegar a este panel ejecutando `View(pinguinos)` en la consola (Importante: R distingue mayúsculas de minísculas!). Hay otras funciones que nos sirven para visualizar nuestros datos. Vamos a utilizar dos de ellas:

``` r
glimpse(pinguinos)
str(pinguinos)
```
Estas salidas son diferentes y nos dan información sobre el tipo de datos en cada columna (o variable).

> Podes encontrar diferencias en la salida?
> Hay algo que te llame la atencion en los datos?

A veces nuestros datos no son tan amigables y necesitamos dar más información a la función para poder leer los datos correctamente. Puedes encontrar estas opciones buscando en la documentación de la función.

> Escribe `?read_csv()` en la consola y revisa la documentación. ¿Cómo se llama la opción para cambiar el delimitador por defecto?


## Leyendo archivos xlsx

¿Cómo podemos trabajar con archivos xlsx? Necesitaremos otro paquete de R, **readxl** que ya está instalado en el proyecto RStudio Cloud, solo necesitamos cargar la librería. En este caso la función se llama `read_excel()`.

``` r
library(readxl)

pinguinos_xls <- read_excel("datos/pinguinos.xlsx")
```

Y listo, hemos leído un archivo xlsx. Por supuesto, a veces tenemos que trabajar con archivos con múltiples hojas o con datos que no están muy organizados. Esta función viene con varias opciones o argumentos para leer hojas específicas (`sheet = <nombre de la hoja>`) o un rango específico (`range = "C1:E7"`) y otros.

Ahora que tenemos los datos leídos en R, es el momento de analizar esos datos.

> #### Ejercicio cinco: analizando los datos que vamos a usar como ejemplo.
>
>Cada uno puede seleccionar el conjunto de datos a utilizar.  Vamos a trabajar con ejemplos del conjunto de datos sobre [las copas del mundo de futbol](https://www.kaggle.com/datasets/abecklas/fifa-world-cup) para mostrar el codigo y las salidas.
> 
> 1. Deberas generarte una cuenta en Kaggle para poder descargar el conjunto de datos. 
> 2. Descarga todos los archivos y copialos en la carpeta datos de tu proyecto para este curso.
> 3. Carga los datos en R 

``` r
copas <- read_csv("Data/WorldCups.csv")

jugadores <- read_csv("Data/WorldCupPlayers.csv") 

partidos <- read_csv("Data/WorldCupMatches.csv")

```

> #### Ejercicio seis: analizando el conjunto de datos
>
> Para la proxima clase utiliza las funciones que vimos para ver la estructura del conjunto de datos y responde estas preguntas:
>
> 1. Cuantos conjuntos de datos tenes?
> 2. Cuantas variables tiene cada uno?
> 3. De que tipo son?
> 4. Ves alguna cosa particular sobre los datos?
> 5. Te podes imaginas preguntas para hacerle a los datos?

