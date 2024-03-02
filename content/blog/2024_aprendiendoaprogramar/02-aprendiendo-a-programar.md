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

El valor de la nueva operacion se almacena en resultado y sobreescribe el nueve.  Si escribimos el nombre de la variable en la consola obtendremos 10 en vez de 9.  Esto significa que si queremos poder usar ambos valores en el futuro necesitamos poder guardarlos en diferentes objetos o variables.

```{r}
> resultado

[1] 10

```

El operador `:`, que usamos antes, devuelve como resultado un **vector**, un conjunto unidimensional de numeros. Vamos a crear el objeto `numeros` con la serie de numeros del 10 al 25

```{r}
> numeros <- 10:25

> numeros
[1] 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

```

Como podemos acceder al numero 13? o al numero 25?. El vector tiene un indice que indica la posicion de cada numero en el vector.  En R los indices inician en 1 y se indican entre corteches a la derecha del nombre del vector 

```{r}
> numeros[4]
[1] 13

> numeros[16]
[1] 25

```
Tambien recordemos que R considera que dos objetos son diferentes si alguna de las letras esta en minusculas y las otras en mayuscula, por ejemplo `Numeros` y `numeros` no es el mismo objeto.

```{r}
> Numeros
Error: object 'Numeros' not found
```

## Funciones

Los lenguajes de programacion son poderosos porque cuentan con un conjunto de comandos o instrucciones pre programadas que nos permiten realizar diferentes acciones.  Esos comandos o instrucciones son conocidos como **funciones**. 

Las funciones tienen una **firma** que tiene la forma

```{r}
nombre_de_la_funcion(parametros, de, la, funcion){

  otras funciones que hacen cosas cuando llamamos a la funcion

}
```

Veamos un ejemplo, la funcion `ls()` lista los objetos en memoria

```{r}

> ls()
[1] "numeros"   "resultado"

```
Siempre se deben usar los parentesis al final del nombre para llamar a la funcion y que R la ejecute. Si solo ponemos el nombre veremos el codigo de la funcion, pero no se ejecutara.

```{r}
> ls
function (name, pos = -1L, envir = as.environment(pos), all.names = FALSE, 
    pattern, sorted = TRUE) 
{
    if (!missing(name)) {
        pos <- tryCatch(name, error = function(e) e)
        if (inherits(pos, "error")) {
            name <- substitute(name)
            if (!is.character(name)) 
                name <- deparse(name)
            warning(gettextf("%s converted to character string", 
                sQuote(name)), domain = NA)
            pos <- name
        }
    }
    all.names <- .Internal(ls(envir, all.names, sorted))
    if (!missing(pattern)) {
        if ((ll <- length(grep("[", pattern, fixed = TRUE))) && 
            ll != length(grep("]", pattern, fixed = TRUE))) {
            if (pattern == "[") {
                pattern <- "\\["
                warning("replaced regular expression pattern '[' by  '\\\\['")
            }
            else if (length(grep("[^\\\\]\\[<-", pattern))) {
                pattern <- sub("\\[<-", "\\\\\\[<-", pattern)
                warning("replaced '[<-' by '\\\\[<-' in regular expression pattern")
            }
        }
        grep(pattern, all.names, value = TRUE)
    }
    else all.names
}
<bytecode: 0x1064e50c0>
<environment: namespace:base>
```

Tambien podemos obtener ayuda sobre que hacen las funciones utilizando el operador `?`. En RStudio ese operador abrira la documentacion de la funcion en el panel **Help**.  

```
?ls
```

<img src="help_rstudio.png" alt="Pantalla principal de RStudio. Panel Help muestra la ayuda de la funcion ls y esta remarcado.  En la consola esta escrito el comando ?ls que tambien esta remarcado." />

### Parametros o argumentos

Algunas funciones tienen parametros.  Vamos a realizar otra operacion con R, dividiremos 2 dividido 3

```
decimal <- 2/3
```

Esta operacion nos devuelve un numero decimal con 15 decimales.  Nosotros no queremos tantos, asi que necesitamos redondear.  Existe una funcion llamada `round()` que puede ser util.  

> Ejercicio: leamos la ayuda para ver que hace esa funcion.

```
?round()
```

La ayuda nos muestra que la funcion tiene dos parametros (o argumentos): `round(x, digits = 0)`. La `x` se refiere al numero que queremos redondear, `digits` se refiere a la cantidad de decimales que queremos tener.

> Ejercicios: intentemos pensar que hara cada una de estas instrucciones antes de ejecutarlas.
round(decimal)
round(2/3)
round(decimal, 3)
round(decimal, 2)
round(decimal, 1)
round(decimal)

Hay muchas funciones que vienen con R y estan disponibles para que las usemos cuando lo instalamos.  Esta version de R se llama **R base** o **base R** (en ingles).  Es la minima funcionalidad que obtenemos con el lenguaje.  Pero R puede hacer muchisimas cosas mas extendiendo las funciones por medio de paquetes.

## Paquetes

Los paquetes son programados por otras personas que usan R, en general se refieren a un tema en particular, por ejemplo hay paquetes para hacer graficos y paquetes para entrenar modelos, paquetes para limpiar datos y paquetes para realizar informes, entre muchisimas otras cosas.

Un paquete puede contener funciones, documentacion y datos. 

<img src="paquete.png" alt="Una persona de palito teniendo un paquete. Del paquete salen tres flechas. Una a funciones, otra a documentación y otra a datos. Otra persona de palito está al lado de cada un de estas cosas y explica que es. Las funciones son porciones de código que hacen algo. La documentación nos explica que hace cada función y como podemos usarla. Hay paquetes que almacenan datos que pueden usarse en los ejemplos de las funciones. " />

install.packages("tidyverse")
library(tidyverse)



Esto es útil cuando estamos probando el código para ver si funciona pero lo perderemos todo cuando cerremos RStudio. Lo que tenemos que hacer es guardar el código que genera su análisis. Para ello utilizamos R Scripts y archivos RMarkdown.





