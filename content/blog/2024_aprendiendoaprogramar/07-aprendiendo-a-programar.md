---
title: "Septimo Encuentro. Aprendiendo a Programar en 30 lecciones"
weight: 7
subtitle: "Septimo encuentro"
excerpt: "Mi sobrino de 14 años quiere aprender a programar y yo voy a enseñarle. En esta clase mas teorica que de costumbre vemos algunos conceptos relacionados con visualizacion de datos."
date: 2024-04-18
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

En esta clase mas teorica que de costumbre vemos algunos conceptos relacionados con visualizacion de datos.

## ¿Por qué visualizar datos? 

La visualización es una herramienta fundamental. Una buena visualización te mostrará el patrón de los datos, cosas que tal vez no esperabas o te hará surgir nuevas preguntas. También puede ayudarte a replantear tus preguntas o darte cuenta si necesitas recolectar datos diferentes.

![](DataSaurus.gif)

Este conjunto de datos muestra que la visualizacion de datos es fundamental.  Las estadisticas descriptivas son todas iguales, pero cuando graficamos los datos vemos que su forma y los patrones son muy diferentes.  Incluso tenemos un **dinosaurio** (si un dinosaurio) en los datos. 

Podemos dividir los objetivos de la visualizacion en dos:

### Explorar un conjunto de datos

![](ggplot2_exploration_es.png)

El objetivo es familiarisarse con los datos que tenemos para analizar.  Aunque ya fuimos viendo algunas maneras de conocer los datos, siempre, siempre debemos visualizar. 

### Comunicar resultados usando un conjunto de datos.

![](ggplot2_obra_maestra.png)

En este caso la visualizacion es parte de la ultima etapa del proceso de analisis de datos, la comunicacion.  Es una parte crítica, porque es cuando vas a mostrar tus resultados a otras personas y necesitas que puedan comprenderlos y encontrarlos útiles para utilizarlos. 


## ¿Con qué podemos visualizar?

* **Tablas**: los datos se expresan en formato de texto (letras y números) y se organizan en filas y columnas. Sirven para mostrar **valores individuales** o cuando los **valores cuantitativos** deben ser **precisos**.

* **Gráficos**: Los datos se expresan usando símbolos y geometrías.Se muestran en relación con uno o más ejes y escalas que asignan significado a los elementos del gráfico. Sirven para mostrar **la forma de los datos: patrones, tendencias y características sobresalientes**.

## ¿Hay un gráfico correcto?

No hay una receta para contestar esta pregunta.  Pero si podemos seguir algunas ideas generales para poder tener el mejor grafico posible para el objetivo que tenemos, ya sea entender mejor nuestros datos o comunicar un punto con nuestros datos.

Las ideas generales son:

- Identificar cuál es la naturaleza de los datos
- Identificar qué queremos comunicar
- Identificar cuál es la mejor manera de comunicarlo 
- Generar el gráfico
- Darle formato pensando en el público

> ### Ejercicio 1: mirar y analizar graficos.
> Mira y analizar esta serie de graficos publicados en diarios, TV y redes sociales. Contesta:
> - Hay algo raro en los graficos?
> - Que te parece que pudo ocurrir?

### Tipos de gráficos > Tipo de datos

**Variables cuantitativas** 

- Datos continuos (números enteros o reales)
- Pueden ser discretizados con algún criterio (mayores que 15)

![](continuous_discrete.png)


**Variables categóricas**

* **Nominales**: elementos discretos y sin orden. No pueden representar valores cuantitativos

_[Córdoba, Salta, Buenos Aires, Formosa, Entre Ríos, Santa Cruz]_

* **Ordinales**: los elementos tienen un orden natural. No representan valores cuantitativos 

_[Pequeño, Mediano, Grande]_

* **Intervalos**: los elementos tienen un orden y pueden representar valores cuantitativos. 

_[0-10, 10-15, 15-20, <20]_

![](nominal_ordinal_binary.png)

### Algunas herramientas

* [Seleccionador de gráficos con plantillas](http://labs.juiceanalytics.com/chartchooser/index.html) 

* Herramientas para hacer gráficos en línea: [Raw Graphs](http://rawgraphs.io/) y [Data Wrapper](https://www.datawrapper.de/)
  
> ### Ejercicio 2: Usar las herramientas on line
> En el primer sitio web utiliza el selector de tipos de grafico y descarga una plantilla en Excel y la otra en PowePoint

## Analizando un grafico

> ### Ejercicio 3: Florence Nightingale
> Mirar este video: https://www.youtube.com/watch?v=VTdVPNvwULM
> Reflexionar:
> - Porque Florence creo ese grafico ?
> - Que demostro con esa visualizacion ?
> - Para que la uso el entrevistado ?

## Conclusion

Las visualizaciones son una poderosa herramienta que tenemos entre nuestros recursos. En un mundo con cada vez mayor cantidad de informacion saber como acceder a ella, como poder analizarla y entenderla sin intermediarios es un superpoder.  

Poder generar visualizaciones que nos ayuden a mostrar y apoyar nuestro argumento tambien puede ser una herramienta poderosa para lograr cambios positivos para nosotros y quienes nos rodean. 
