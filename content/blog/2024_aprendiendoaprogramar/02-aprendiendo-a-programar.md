---
title: "Segundo encuentro. Aprendiendo a Programar en 30 lecciones"
weight: 2
subtitle: ""
excerpt: "Mi sobrino de 14 años quiere aprender a programar y yo voy a enseñarle. La segunda clase empezamos a encontranos con cenceptos sobre programacion y como eso funciona en R."
date: 2024-03-02
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

## Lenguaje de programacion e IDE

Vamos a usar R como lenguaje de programación y RStudio como una IDE (Integrated Development Environment), un Entorno Integrado de Desarrollo.  Estas son dos herramientas diferentes. Podriamos usar R sin RStudio o tambien utilizando otras IDEs como Visual Studio Code.  El objetivo de una IDE es ayudarnos a programar presentando informacion y herramientas que nos permiten acceder a cosas utiles en el mismo entorno.

Para iniciar RStudio, hacé doble click en el ícono de RStudio. Iniciar  RStudio también inicia R (en realidad, es probable que nunca abras R por sí mismo).

<img src="rstudio-principal.png" alt="Pantalla principal de RStudio. Paneles de consola, entorno y archivos" />

Observa los paneles por defecto:

  * Consola (toda la izquierda)
  * Environment/History (pestaña en la parte superior derecha)
  * Files/Plots/Packages/Help (con pestañas en la parte inferior derecha)

No es necesario que sepamos utilizar todo esto de inmediato. Nos familiarizaremos con más opciones y capacidades a lo largo del taller.

Podemos escribir código, es decir, instrucciones para ser ejecutadas por R en la Consola. Por ejemplo, podemos calcular el resultado dos más dos escribiendo

```{r}
2 + 7
```

en la Consola y pulsando enter. 

10:50
10:100
a:z
2/3
2*5


El resultado aparece justo debajo. También podemos guardar ese resultado en un objeto, en este caso llamado `x`.

```{r}
x <- 2 + 2 
```

Esa flechita es el *operador de asignación* y funciona como un `=`. Ahora el resultado se guarda en el Entorno (Environment) como una variable con nombre `x` y no se imprime en la consola. 





resultado <- 2 + 7
resultado
resultado <- 5 * 2
resultado
numeros <- 10:25
numeros
numeros[4]
numeros[16]
Numeros
numeros
ls()
ls
?ls()
decimal <- 2/3
?round()
round(decimal)
round(2/3)
round(decimal, 3)
round(decimal, 2)
round(decimal, 1)
round(decimal)
install.packages("tidyverse")
library(tidyverse)
read_csv("Data/pinguinos.csv")
pinguinos <- read_csv("Data/pinguinos.csv")
pinguinos
View(pinguinos)
View(pinguinos)
pin_xls <- readxl::read_excel("Data/pinguinos.xlsx")
str(pinguinos)
glimpse(pinguinos)
View(pinguinos)
