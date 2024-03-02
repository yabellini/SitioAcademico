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

## Empezando a programar

Podemos escribir código, es decir, instrucciones para ser ejecutadas por R en la Consola. Por ejemplo, podemos calcular el resultado dos más siete escribiendo

```{r}
2 + 7
```

en la Consola y pulsando enter. El resultado aparece en la consola

```{r}
[1] 9
```

Junto al resultado aparece un [1]. R te indicaque esta línea de resultados comienza con el primer valor. Algunas instrucciones devuelven más de un valor, y sus resultados pueden llenar varias líneas. Por ejemplo, el comando `10:50` devuelve 40 valores; crea una secuencia de enteros del 10 a 50. Cuando ejecutamos esa orden en la consola aparecen números nuevos entre corchetes al principio de la segunda líneas de salida. Estos números sólo significan que la segunda línea comienza con el 37º valor del resultado. Por el momento (y en la mayoria de los casos) se pueden ignorar los números que aparecen entre corchetes.

```{r}
> 10:50 
[1] 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45
[37] 46 47 48 49 50
```

Si escribimos una instruccion que R no reconoce, R devuelve un mensaje de error. No hay porque preocuparse. R sólo nos vaisa que no pudo entender o hacer lo que le pedimos. Se puede intentar una instruccion diferente en el siguiente prompt.  

> Vamos a aprender sobre los errores y como leerlos mas adelante

Ahora probemos on otras operaciones, como la division y la multiplicacion. 

```{r}
2/3
2*5
```

El resultado siempre aparece justo debajo. También podemos guardar ese resultado en un objeto, en este caso llamado `resultado`.

```{r}
resultado <- 2 + 7
```

Esa flechita es el *operador de asignación* y funciona como un `=`. Ahora el resultado se guarda en el Entorno (Environment) como una variable con nombre `resultado` y no se imprime en la consola. Para ver el contenido, ademas de verla en el Entorno, podemos escribir el nombre de la variable (asi se llama este tipo de objeto) en la consola


```{r}
> resultado

[1] 9

```
Tambien podemos empezar a usar la variable para realizar calculos

```{r}
> resultado + 5

[1] 14

```

Que pasa si escribimos  

```{r}
> resultado <- 5 * 2

```

El valor de la nueva operacion se almacena en resultado y sobreescribe el nueve.  Si escribimos el nombre de la variable en la consola obtendremos 10 en vez de 9.  Esto significa que si queremos poder usar ambos valores en el futuro necesitamos poder guardarlos en dos objetos o variables diferentes.

```{r}
> resultado

[1] 10

```



numeros <- 10:25, numeros
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



Esto es útil cuando estamos probando el código para ver si funciona pero lo perderemos todo cuando cerremos RStudio. Lo que tenemos que hacer es guardar el código que genera su análisis. Para ello utilizamos R Scripts y archivos RMarkdown.