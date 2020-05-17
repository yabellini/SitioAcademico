---
date: "2020-05-18"
draft: false
type: page
linktitle: Version Control. Primeros pasos de Git con R
summary: En este post introducimos los primeros pasos para usar Git con RStudio
title: Primeros pasos de Git con R
authors: 
    - admin
    - Marysol Gatti
type: post
weight: 1
tags: 
  - R-Ladies
---

Este post corresponde al meetup realizado en conjunto por los capítulos de R-Ladies Santa Rosa, R-Ladies General Pico y R-Ladies Buenos Aires realizado el 18 de Mayo sobre realizar primeros pasos en Git utilizando R.

El material presentado en este post tiene como fuente el libro [Happy Git and GitHub for the useR](https://happygitwithr.com/index.html) by [Jennifer Bryan](https://github.com/jennybc/happy-git-with-r)

## ¿Quién sos vos?

Cada lección debe ser pensada, organizada y generada para una audiencia en particular, esta es la persona en la que pensamos cuando preparamos este taller:

>*Romina* trabaja ordenando y analizando datos utilizando R para una variedad de clientes.  
Utiliza proyectos en RStudio para ordenar su trabajo.
Comparte sus avances y resultados utilizando herramientas en la nube (como dropbox y google drive).  
Compartir de esta manera le ha traído varios dolores de cabeza
Sabe que Git puede ayudarla con estos problemas pero no le queda claro como.
Tiene usuario en GitHub pero nunca usó.  
Quiere entender como funciona y como usarlo con R y RStudio para poder incorporarlo a sus proyectos.


## ¿Qué vamos a ver?

Este mapa conceptual presenta el contenido de este taller

   {{< figure src="/img/git_concept_map.png" alt="Mapa conceptual: en tu computadora tienen RStudio IDE y un proyecto de RStudio, con un directorio de trabajo, que será el repositorio local de Git, al que podremos hacer Add de archivos a la Staging area, dede la cual podremos hacer Commit al repositorio local. Desde este respositrio local podemos hacer Push y Pull hacia el respositorio remoto que puede estar en GitHub.  Esta misma configuraci{on est{a en la maquina de todos los colaboradores.">}}


## A usar Git desde RStudio

### Primera situación: Nuevo proyecto, GitHub primero

#### Paso 1: Hacer un repositorio en GitHub

Estos pasos se deben realizar sólo una vez por cada proyecto nuevo:

 * Ir a https://github.com y asegúrate de haber iniciado sesión.

 * Hacé clic en el botón verde "Nuevo repositorio" o, si estás en tu página de perfil, hacé clic en "Repositorios", luego haga clic en el botón verde "Nuevo".  complear con los siguientes datos:

  - Nombre del repositorio: MiRepo (o el nombre que quieras)
    
  - Público
    
  - *SÍ* inicialice este repositorio con un archivo _README_

* Hacé clic en el botón verde grande "Crear repositorio".

Copia la URL HTTPS para clonar el repositorio mediante el botón verde "Clonar o descargar" (o copia la URL SSH si elegiste utilizar claves SSH).


#### Paso 2: Nuevo proyecto RStudio a través de git clone

* En RStudio, generar un nuevo proyecto:

   _File > New Project > Version Control > Git_ .En la "URL del repositorio", pegue la URL de su nuevo repositorio de GitHub. Será algo como esto https://github.com/nombreusuario/MiRepo.git.  Seleccionar _Open in new session_ y hacé clic en _Create Project_. Esto debería descargar el archivo README.md  que creamos en GitHub en el paso anterior. (pasos 1 a 5 de la siguiente figura). 
   
   {{< figure src="/img/git_githubfirst_new_project.png" alt="Pasos para crear un proyecto con control de versiones desde RStudio si ya existe el repositorio en GitHub">}}
    
  Cuando hacemos click en _Create Project_ se crea un nuevo directorio (carpeta), que cumplirá todas estas funciones:
    - un directorio o "carpeta" en su computadora
    - un repositorio de Git, vinculado a un repositorio de GitHub remoto
    - un proyecto RStudio
 

#### Usando el nuevo proyecto

El proyecto ya está listo para ser usando con control de versiones. 

En ausencia de otras restricciones, se sugiere que todos tus proyectos de R tengan exactamente esta configuración.

Hay una gran ventaja en el flujo de trabajo “GitHub primero, luego RStudio”: el repositorio de GitHub se agrega como remoto para tu repositorio local y tu _master local_ está ahora mirando los cambios de la _master en GitHub_. Este es un punto muy técnico pero importante sobre Git. La parte práctica es que ahora está configurado para hacer `pull` y `push`, sin necesidad de la linea de comandos.

#### Realizar cambios locales, guardar, confirmar

Deberías hacer esto cada vez que termines una parte valiosa del trabajo, probablemente muchas veces al día.  No deberían ser espacios mayores a una hora.

Desde RStudio, vamos a modificar el archivo README.md, por ejemplo, agregando la línea "Esta es una línea desde RStudio". Guarda tus cambios.

Ahora vamos a confirmar estos cambios en el repositorio local. ¿Cómo?

  1. Hacé clic en la pestaña _Git_ en el panel superior derecho.
  2. Marca la casilla _Staged_ para los archivos que querramos gurdar (sean nuevos o modificados).
  3. Hacé clic en _Commit_.
  
   {{< figure src="/img/git_git_staged.png" alt="Agregar (add) un archivo a la Staged area y luego iniciar un Commit desde RStudio">}}
  
  
  4. Aparece una ventana emergente.  Escribe un mensaje en _Commit message_, como "Commit desde RStudio" y hacé clic en _Commit_.

{{< figure src="/img/git_commit_rstudio.png" alt="Realizar un Commit desde RStudio">}}

#### Actualice (push) sus cambios locales a GitHub

Deberías hacer esto varias veces al día, pero menos veces que las que hacés _commit_.  En este momento tienes trabajo nuevo en tu repositorio local, pero los cambios aún no están en el repositorio remoto.

Ahora vamos a actualizar esos cambios del repositorio local al remoto. ¿Cómo?

  1.  Primero hacemos _Pull_ desde GitHub. Esto puede parecer contradictorio pero si realizaste cambios en el repositorio remoto desde la interfaz web o desde otra máquina o (un día) un colaborador ha realizado cambios, será mucho mas sencillo (y serás mucho más feliz) si traes esos cambios a tu repositorio local antes de enviar los tuyos haciendo _push_.  
  Para hacer _Pull_ presionamos la flecha azul en la pestaña Git en RStudio.  Lo más probable es que recibas un mensaje de que está todo actualizado (_Already up-to-date_).
  
  2. Hacé clic en el botón verde _Push_"_ para enviar tus cambios locales a GitHub. Puede ser que solicite el usuario y contraseña de github. Debería ver algún mensaje similar a la siguiente figura.
  
  {{< figure src="/img/git_push_rstudio.png" alt="Realizar un Push desde RStudio">}}
  
  
  
  


