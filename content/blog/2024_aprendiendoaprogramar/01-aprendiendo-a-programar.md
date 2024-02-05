---
title: "Aprendiendo a Programar en 30 lecciones"
weight: 1
subtitle: "Primer encuentro"
excerpt: "Mi sobrino de 15 años quiere aprender a programar y yo voy a enseñarle. Esta es la primera entrada del blog de nuestro viaje juntos que detalla como instalar el entorno que vamos a usar por el resto de las clases."
date: 2024-02-05
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

Mi sobrino de 15 años quiere aprender a programar y yo voy a enseñarle. Esta es la primera entrada del blog de nuestro viaje juntos.

La idea del primer encuentro era charlar sobre que podia ensenarle y acordar cuando nos juntariamos. Debido a su entusiasmo tambien preparamos todo el entorno para poder tener las clases.

## Objetivo de aprendizaje

El objetivo general al finalizar el curso es que Juan Cruz pueda leer archivos de datos, analizarlos y procesarlos para realizar agregaciones y visualizaciones adecuadas, generar un reporte con sus resultados y publicarlo en la web. Todo esto con buenas practicas para poder compartir y reproducir su trabajo.

## Entorno de trabajo

Empezamos instalando el software que necesitamos:

### Instalando R

Estos pasos corresponden a **Windows**

-   Entrá a <https://cran.r-project.org/bin/windows/base/> y bajate el instalador haciendo click en el link grandote que dice *"Download R x.x.x for Windows"*.

-   Una vez que se bajó, hacé doble click en el archivo y seguí las instrucciones del instalador.

-   Una vez que se termine de instalar, te va a aparecer un ícono como este en el escritorio o en los programas instalados: {{< figure src="r-logo.jpeg" height="20px" >}}

-   Al ejecutarlo, les tiene que aparecer algo como esto:

![](r-en-windows.png) 

Si ves una ventana así significa que ya tenés instalado R, pero seguí leyendo! **Todavía falta unos pasos** para poder sacarle todo el jugo: necesitamos instalar **RTools**.

### Instalando RTools

Para instalar algunos paquetes de R en Windows, vas a necesitar instalar un programa adicional llamado rtools. 

1. Entrá a https://cran.r-project.org/bin/windows/Rtools/ y descargate el instalador de version mas nueva, en este momento es Rtools43. Para eso hacer click en Rtools43 y en es nueva pagina hacer clik en [Rtools43 installer](https://cran.r-project.org/bin/windows/Rtools/rtools43/files/rtools43-5948-5818.exe).  

2. Ejecuta el instalador y segui las instrucciones.

3. Abrí la consola de R, escribí esto en la consola y apretá enter:

```{r, eval = FALSE}
Sys.which("make")
```

Debería salir algo como esto:
```{r, echo=FALSE}
c(make = "C:\\rtools40\\usr\\bin\\make.exe")
```

### Instalando RStudio

- Ingresa en el sitio web de Posit y descarga RStudio para desktop: https://download1.rstudio.org/electron/macos/RStudio-2023.12.1-402.dmg.

- Una vez descargado, como siempre, doble click en el archivo y seguir los pasos de instalación.

- Terminada la instalacion, al ejecutar RStudio les tiene que aparecer una ventana como esta:


![](rstudio-principal.png) 

### Crear una cuenta en GitHub.

- Ir a https://github.com/.

- Hacer clik en Registrarse or Sign up.

- Seguir las indicaciones para crear la cuenta personal.

- Uno de los pasos implica chequear que son una persona y luego validar la direccion de email que usaste para crear la cuenta. 

## Primer ejercicio

Crear el perfil en github:

1 - crear un repo con el mismo nombre que tu usuario de github.

2 - Agregarle un archivo README.md 

3 - Pensar en que queres poner en tu perfil y modificar el readme son esa informacion. Tenerlo listo para la proxima clase.