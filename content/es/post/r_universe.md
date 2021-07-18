---
date: "2021-07-17"
draft: false
type: page
linktitle: Creando tu r-universe
summary: Durante useR! 2021 Jeroen Ooms presentó el proyecto universo R.  En este post the explico como crear el tuyo.
title: Creando tu r-universe
authors: 
    - admin
type: post
weight: 1
tags: 
  - conferences
  - tips
  - rstats
---

## El proyecto universo R (R-universe).

Durante [useR! 2021](https://user2021.r-project.org/) Jeroen Ooms presentó [el proyecto universo R](https://jeroen.github.io/user2021/#1) en su _keynote_.  

En la web de [ROpenSci](https://ropensci.org) se define a [r-universe](https://r-universe.dev/organizations/) como una plataforma que proporciona a usuarias/os y organizaciones un __repositorio personal similar a CRAN__ para publicar software, artículos _rmarkdown_ y otro contenido que un un paquete de R pueda contener.

Cuando te unes a _r-universe_, el sistema rastrea automáticamente los repositorios _git_ que registraste en tu perfil y que contienen paquetes de R. Crea los binarios para instalarlos en Windows y MacOS, genera viñetas y hace que todos estos datos estén disponibles a través de paneles, feeds y API en subdominios personales.

El subdominio tendrá _tu nombre de usuario_ de github, más el dominio `r-universe.dev/`, de esta manera, mi subdominio es:

**`https://yabellini.r-universe.dev/`**

Una de las características más interesantes es que puedes empezar a instalar los paquetes que están en tu _universo-r_ con la función `install.packages` aunque el paquete no esté en CRAN.  Esta funcionalidad es muy interesante para quines somos docentes y generamos paquetes para nuestras clases. 

## Cómo generar tu propio universo

Durante esta charla, el disertante, compartió [este blog post](https://ropensci.org/blog/2021/06/22/setup-runiverse/) que explica como generar tu propio universo.  Aquí mi paso a paso siguiendo estas instrucciones:

### Paso 1: crear un respositorio en tu github para tu universo R

La siguiente figura resume los pasos a seguir para crear el resposirio necesario para generar nuestro `universo-r`: 

{{< figure src="/img/r_univserse_crear_repo.png" >}}

a. Crea un nuevo repositorio llamado `universe` en tu cuenta de GitHub.  Para eso ingresas a tu cuenta de github (paso 1), 

b. luego haces click en el signo más que se encuentra arriba a la derecha y seleccionas la opción _New repository_, que siginifca nuevo repositorio en inglés (paso 2). 

c. En la pantalla que aparece completamos el _repository name (nombre del repositorio)_ con **universe** (paso 3), seleccionamos el repositorio como _public (público)_ (paso 4) y lo generamos presionando el botón _Create repository (crear repositorio)_ (paso 5).


### Paso 2. Detallar los paquetes que agregaremos a nuestro universo

a. Una vez que el repositorio se creó se nos mostrará una pantalla con opciones para iniciar ese repo (ver figura siguiente).

{{< figure src="/img/r_univserse_repo_vacio.png" >}}

b. Presionar en el link _create a new file (crear un nuevo archivo)_ (paso 1) para generar un archivo llamado `packages.json`. Este archivo debe enumerar los repositorios de los paquetes que queremos incluir en nuestro `universo-r`. 

c. Completar este archivo con los datos de los paquetes siguiendo el siguiente formato: 

  - en el campo `url` se debe completar con __una URL pública de git del repositorio del paquete__.
  
  - en el campo `package` va el nombre del paquete __tal cual está escrito__ en el archivo `DESCRIPTION` en la url. 
  
  - Si el paquete R no se encuentra en la raíz del repositorio, también debe establecer el campo `subdir` en la ruta del directorio raíz del paquete R. 
  
En la figura se ven los paquetes que yo agregué a mi universo.  

{{< figure src="/img/r_univserse_packages.png" >}}

d. Cuando terminamos de completar los datos, presionamos en el botón _Commit new file_.  Se mostrará una pantalla similar a la siguiente figura.

{{< figure src="/img/r_univserse_repo_listo.png" >}}


### Paso 3: instalar la aplicación R-universe en GitHub

En este paso debes instalar la aplicación R-universe en tu cuenta de GitHub haciendo click en [este link](https://github.com/apps/r-universe/installations/new) y seleccionando tu cuenta de la primera pantalla que aparece (paso 1 en la siguiente figura). En la segunda pantalla se recomienda seleccionar _all the repositories (todos los repositorios)_ (paso 2) y luego hacer click en el botón _Next (siguiente)_ (paso 3). 

{{< figure src="/img/r_univserse_instalar_app.png" >}}


### Paso 4: R-universe listo



