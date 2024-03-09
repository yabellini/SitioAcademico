---
title: "Tercer Encuentro. Aprendiendo a Programar en 30 lecciones"
weight: 3
subtitle: "Tercer encuentro"
excerpt: "Mi sobrino de 14 años quiere aprender a programar y yo voy a enseñarle. En esta clase aprendimos que son los paquetes, repasamos el proceso de analizar datos y descargamos los datos que vamos a usar para el resto de las clases"
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

## Ordenando nuestro trabajo

Cuando empezamos a trabajar en un proyecto de programacion vamos a ir generarndo diferentes resultados y productos intermedios hasta que terminemos, ademas de nuestros datos y nuestro codigo, tendremos, por ejemplo graficos y diferentes reportes.

Es una buena practica mantener todos los archivos asociados a un proyecto en un mismo lugar. RStudio cuenta con soporte integrado para esto por medio de los proyectos.

### ¿Qué ventajas tiene?

-   Te permite "cuidar" los datos que usas al ordenarnos en carpetas que diferencien entre la versión originaly los datos que transformaste y limpiaste o los resultados finales.
-   Te permite compartir tu trabajo de forma mas sencilla con otras personas. Solo tendrías que compartir la carpeta del proyecto sabiendo que incluye todo lo necesario para que cualquiera reproduzca tu análisis.
-   Te permite publicar de manera ordenada tu código si vas a presentar o publicar tu trabajo.
-   Te permite continuar con lo que estabas haciendo hace una semana o hace un mes como si el tiempo no hubiera pasado. De alguna manera es un regalo para tu yo futuro.

### Creando un proyecto

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

### Abrir un proyecto

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

Esto puede pasar si por ejemplo leés una base de datos en memoria pero no guardás el código que lo hace.
Mientras estemos trabajando, R tendrá esa base de datos en memoria y podremos hacer cálculos y gráficos.

Por defecto además RStudio va a recordar las variables que estés usando mañana o pasado en un archivo oculto (.RData) a menos que le indiques lo contrario.

Y si bien suena práctico volver a R al otro día y tener el análisis tal cual lo dejamos, esto puede significar que nunca nos demos cuenta que nos faltó guardar una línea de código clave en nuestro análisis.


> #### Tercer ejercicio: Configurá RStudio
> 
> 1.  Hacé click en el menú **Tools (Herramientas)** y luego **Global Options (Opciones globales)**.
> 2.  Destildá la opción **Restore .RData into workspace at startup (Recuperar .RData al inicio de la sesión)**.
> 3.  Hacé click en **Apply (Aplicar)**.


## Objetivo final de nuestro curso

A partir de ahora vamos a empezar a trabajar con nuestro proyecto de curso.  El objetivo final es poder realizar un analisis de un conjunto de datos que ustedes elijan.  Este analisis debera contener lectura y limpieza de datos, visualizaciones, reportes y un sitio web con la publicacion de los resultados. 

Para ver un ejemplo del tipo de resultado que podemos obtener vamos a revisar este proyecto sobre los Pingüinos Papúa.

> #### Cuarto ejercicio: Explorar el proyecto de los Pingüinos 
> 
> 1. Descarga el archivo [rstudio-project-pinguinos.zip](rstudio-project-pinguinos.zip) que contiene el proyecto. 

## Leyendo y observando datos

read_csv("Data/pinguinos.csv") pinguinos \<- read_csv("Data/pinguinos.csv") pinguinos View(pinguinos) View(pinguinos) pin_xls \<- readxl::read_excel("Data/pinguinos.xlsx") str(pinguinos) glimpse(pinguinos) View(pinguinos)

## Ejercicio: analizando los datos que vamos a usar como ejemplo.

copas \<- read_csv("Data/WorldCups.csv") jugadores \<- read_csv("Data/WorldCupPlayers.csv") partidos \<- read_csv("Data/WorldCupMatches.csv") View(copas)
