---
title: Máquina nocional
author: Yanina Bellini Saibene
summary: "Este articulo presenta el nuevo contenido sobre máquinas nocionales para el capitulo _Modelos mentales y evaluación formativa_ de Teaching Tech Together. Una _máquina nocional_ es un dispositivo pedagógico para ayudar a la comprensión de algún aspecto de los programas o la programación. Se utilizan para representar un entorno de aprendizaje simplificado y abstracto. No se refiere a una máquina real física, sino a una representación simplificada de un modelo conceptual que se utiliza con fines educativos."
date: '2024-01-04'
tags:
  - Spanish
  - Education
  - T3
  - 100DaysToOffload
---

{{< figure src="featured.svg">}}

## Máquina nocional

Una *máquina nocional* es un dispositivo pedagógico para ayudar a la comprensión de algún aspecto de los programas o la programación[^1]. Se utilizan para representar un entorno de aprendizaje simplificado y abstracto. No se refiere a una máquina real física, sino a una representación simplificada de un modelo conceptual que se utiliza con fines educativos.

[^1]: Fincher, Sally, Johan Jeuring, Craig S. Miller, Peter Donaldson, Benedict du Boulay, Matthias Hauswirth, Arto Hellas, et al. 2020. "Notional Machines in Computing Education: The Education of Attention."In *Proceedings of the Working Group Reports on Innovation and Technology in Computer Science Education*, 21--50. ITiCSE-WGR '20. New York, NY, USA: Association for Computing Machinery. <https://doi.org/10.1145/3437800.3439202>.

El grupo de trabajo "ITiCSE 2020 - Capturing and Characterising Notional Machines" realizó un extenso trabajo de revisión bibliográfica, entrevistas, registro y colección curada de máquinas nocionales. En este trabajo determinaron que una máquina nocional tiene *una finalidad pedagógica*, su función genérica es *llamar la atención* sobre algún *aspecto oculto* de los programas o de la informática, *o ponerlo en relieve*. La máquina también tendrá un *enfoque específico* dentro de los programas o la informática, y adoptará una *representación particular* que destaque un aspecto específico del enfoque[^1]. En ese mismo trabajo, se encontró que la mayoría de la bibliografía presenta estudios de uso de las máquinas nocionales en los niveles universitario de grado, para estudiantes principiantes (CS1/2) y clasificaron las máquinas nocionales en dos tipos: *basadas en analogías* y *basadas en representaciones*. También determinaron que las máquina se pueden usar como *parte del contenido* de la lección o como *herramienta de diagnóstico*.

### Máquinas nocionales basadas en analogías

Este tipo de máquinas utilizan un contexto con el que tus estudiantes están potencialmente familiarizados para explicar el contexto de programación. Esto permite que tus estudiantes razonen de manera familiar en el espacio análogo y transfieran ese razonamiento al espacio de programación[^1].

Este tipo de máquina nocional suelen ser sencillas y cortas. Muchas veces un ejemplo o un explicación. Como las analogía sobre cocinar y comer que usamos en este mismo capítulo para explicar la diferencia entre evaluación formativa y evaluación sumativa.

También pueden ser muy concretas, por ejemplo, docente y estudiantes pueden representar alguna parte de la máquina sobre la que se quiere llamar la atención o bien se pueden utilizar otros objetos concretos en el aula. Por ejemplo, Yanina, explica que son las variables y como se accede a su contenido utilizando un cajón como analogía. Luego expande sobre esa misma analogía para explicar que es un vector, utilizando una cajonera como ejemplo.

### Máquinas nocionales basadas en representación

En este caso las máquinas nocionales representan de una manera diferente el contexto de programación que se quiere enseñar. Existen diferentes formas de representación, como diagramas, juegos de rol y verbalizaciones[^1]. Muchas veces se hacen a mano, por ejemplo un diagrama que dibujamos en una pizarra (como los mapas conceptuales, al inicio de esta articulo hay un mapa resumiendo este contenido) , mientras que otras pueden ser generadas por otras herramientas, por ejemplo una visualización automática de la ejecución de un programa.

Las máquinas nocionales que se hacen _a mano_ tienen diversos impactos en la enseñanza ya que requieren que el/la docente haga el trabajo de la máquina para explicar como funciona (enseñanza activa) y también relentiza la instrucción, permitiendo que le puedan seguir mejor.

### Uso de máquinas nocionales

Durante una lección se pueden utilizar como dispositivos explicativos para acomodar el contenido al nivel de conocimiento actual de tus estudiantes y evitar una carga cognitiva innecesaria. En general una lección o un curso suele tener un repertorio de varias máquinas nocionales que sirven a objetivos de aprendizaje específicos de forma individual o para ir construyendo una máquina nocional basada en otra. También se utilizan para diagnosticar conceptos erróneos en tus estudiantes al exponer su modelo mental. Por ejemplo, Greg utiliza un test muy sencillo para determinar si sus estudiantes tienen un modelo mental de ejecución secuencial (tienen una formación en programación) o evaluación constante (tienen una formación en planillas de cálculo).

> ## Máquina Nocional: ¿Cómo se puede saber?
> 
> Después que el siguiente código se ejecute:
> 
> A = 1
> 
> B = A
> 
> A = 99
> 
> Cuál es el valor de B?
> 
> Alguien que piense en Excel va a contestar "99", porque todo el punto de hacer B = A es hacer B igual a A, mientras que alguien que tiene su pensamiento formado por un lenguaje de progrmaación como Java o Python, va a contestar que B es todavía igual a 1. 

Otro ejemplo para el diagnóstico sobre que tanto están aprendiendo tus estudiaste utilizado por Greg es tener su propia máquina nocional y compararla con la de sus estudiantes mientras el curso avanza.  
Por ejemplo, Greg usa esta versión caricaturizada de la realidad siempre que enseña Python. Después de 25 horas de instrucción y 100 horas de trabajar por su cuenta, espera que la mayor parte del grupo tenga un modelo mental que incluya todas o la mayoría de estas características.


> ## Máquina nocional: Python
>
> 1.  Ejecutar programas en el momento en la memoria, la cual se divide en la pila de llamadas y la cola de montículo (*heap* en inglés).
>
> 2.  La memoria para los datos siempre es asignada desde la cola del montículo.
>
>3.  Cada conjunto de datos se almacena en una estructura de dos partes. La primera parte dice de qué tipo de datos se trata y la segunda parte es el valor real.
>
>4.  Booleanos, números y caracteres de texto nunca son modificados una vez que se crean.
>
>5.  Las listas, conjuntos y otras colecciones almacenan referencias a otros datos en lugar de almacenar estos valores directamente. Pueden ser modificados una vez que se crean, es decir, una lista puede ser ampliada o nuevos valores pueden ser agregados a un conjunto.
>
>6.  Cuando un código se carga a la memoria, Python lo convierte a una secuencia de instrucciones que son almacenadas como cualquier otro tipo de dato. Este es el motivo por el que es posible asignar funciones a variables y luego pasarlas como parámetros.
>
>7.  Cuando un código es ejecutado, Python sigue las instrucciones paso a paso, haciendo lo que cada instrucción le indica de a una por vez.
>
>8.  Algunas instrucciones hacen que Python lea datos, haga cálculos y cree nuevos datos. Otras, controlan qué instrucciones va a ejecutar, como los bucles y condicionales; también hay instrucciones que le indican a Python que llame a una función.
>
>9.  Cuando se llama a una función, Python coloca un nuevo marco de pila en la pila de llamadas.
>
>10. Cada marco de pila almacena los nombres de las variables y las referencias a los datos. Los parámetros de las funciones son simplemente otro tipo de variable.
>
>11. Cuando una variable es utilizada, Python la busca en el marco de la pila superior Si no la encuentra allí, busca en el último marco en la memoria global.
>
>12. Cuando la función finaliza, Python la borra del marco de la pila y vuelve a las instrucciones que estaba ejecutando antes de llamar a la función. Si no encuentra un "antes," el programa ha finalizado.

## Ejercicios

Estos son los ejercicios que acompañan este tema. 

### Tus máquinas nocionales (grupos pequeños/20')

En grupos pequeños, escriban una descripción de la máquina nocional que quieren que sus estudiantes usen para entender cómo corren sus programas. ¿En qué difiere una máquina nocional para un lenguaje basado en bloques como _Scratch_ de la máquina nocional para _Python_? ¿Y en qué difiere de una máquina nocional para hojas de cálculo o para un buscador que está interpretando HTML<sup>Sigla de HyperText Markup Language en inglés</sup> y CSS<sup>Sigla de Cascading Style Sheets en inglés</sup> cuando renderiza una página web?

### Colección de máquinas nocionales (grupos pequeños/20')

En grupos pequeños visiten el sitio [Notional Machines](https://notionalmachines.github.io/) y selecciones Máquinas nocionales basadas en analogías. Revisen el catálogo e identifiquen cuales conocian y cuales no. Seleccionen una para usar en su próxima clase y revisenla en detalle. Compartan con su grupo porqué seleccionaron esa máquina nocional.

Si hay alguna máquina nocional que conozcan y no está en el catálogo utilicen el formato de la web para describirla.

