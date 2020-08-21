---
title: Mapa Conceptual - Clase 1
linktitle: Mapa Conceptual
toc: true
type: docs
date: "2020-01-05T00:00:00+01:00"
draft: false
menu:
  rdesdecero:
    name: Mapa Conceptual - Clase 1
    weight: 3

# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 1
---


## Mapa conceptual - lección 1
### Ejemplos de uso del lenguaje R 
#### con el trabajo de todas científicas de datos de latinoamérica. 

{{< diagram >}}
graph LR;
A[Lenguaje R] -->|tiene| B[multiple usos];
B -->|No solo| C[estadística];
B --> D[Análisis de texto];
B --> E[Análisis de audio];
B --> F[Informes, tableros de control, presentaciones];
B --> G[Aplicaciones web];
B --> H[Internet de las cosas];
B --> I[Modelado];
B --> J[Teledetección y mapeo];

{{< /diagram >}}

## Mapa conceptual - lección 2
### RStudio IDE

{{< diagram >}}
graph LR;
A[Lenguaje R] -->|lo usamos a través de| B[RStudio IDE];
B -->|tiene| C[consola];
B -->|tiene| D[entorno/historia];
B -->|tiene| E[scripts];
B -->|tiene| F[paneles];
F --> G[archivos];
F --> H[gráficos];
F --> I[paquetes];
F --> J[ayuda];
F --> K[visor];
F --> L[tutorial]

{{< /diagram >}}

## Mapa conceptual - lección 3
### R base, packages, function, parameters, variables

{{< diagram >}}
graph LR;
A[Lenguaje R] -->|formado por| B[R base];
A -->|formado por| C[Paquetes];
C -->|tiene| D[funciones];
B -->|tiene| D;
D -->|puede tener| E[argumentos];
A -->|trabaja con| F[estructura de datos];
F -->|una son| G[las variables] ;

{{< /diagram >}}


## Mapa conceptual - lección 4
### Mensajes, erroress y warnings (advertencias)

{{< diagram >}}

graph LR;

A[Consola] -->|ejecuta| B[código de R];
B -->|puede devolver| C[un mensaje];
B -->|puede devolver| D[una advertencia (warnings)];
B -->|puede devolver| E[un error];
C -->|está todo bien| F[informativo/código ejecutado];
D -->|algo pasó| G[informativo/código ejecutado];
E -->|algo salió mal| H[código no ejecutado];

{{< /diagram >}}


## Mapa conceptual - lección 5
### Cómo obtener ayuda

{{< diagram >}}

graph LR;

A[Ayuda] -->|como preguntar| B[de manera eficiente];
A -->|usar la documentación en| C[el panel de ayuda de RStudio];
A -->|buscar en| D[Google];
A -->|consultar| E[Cheat Sheet];
A -->|consultar| F[CRAN Task Views];
A -->|buscar/preguntar| G[Comunidad R-Studio];
A -->|buscar/preguntar| H[StackOverflow];
A -->|buscar/preguntar| I[Twitter];
A -->|preguntar/unirte| J[Comunidad R];
B -->|usar| K[sessionInfo];
B -->|usar| L[dput];

{{< /diagram >}}

## Mapa conceptual - lección 6
### Comunidad R: R-Ladies

{{< diagram >}}

graph LR;

A[Comunidad R] -->|tiene| B[Usuarios de Grupos de R];
C[R-Ladies] -->|es un tipo de| B;
C -->|tiene| D[Capítulos];
D -->|uno de ellos es| E[R-Ladies Santa Rosa];
A -->|está creciendo mucho| F[en América Latina] ;
F -->|organizamos| G[LatinR];
F -->|traducimos| H[R4DS];
F -->|traducimos| J[Guías rápidas de RStudio];
F -->|llevamos adelante| I[DatosDeMiercoles];
F -->|llevamos adelante| K[Paquetes Datos/Dados];

{{< /diagram >}}

