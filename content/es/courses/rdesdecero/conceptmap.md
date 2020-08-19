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
A[R Languaje] -->|we use it through| B[RStudio IDE];
B -->|has| C[console];
B -->|has| D[enviroment/history];
B -->|has| E[scripts];
B -->|has| F[panels];
F --> G[files];
F --> H[plots];
F --> I[packages];
F --> J[help];
F --> K[viewer];

{{< /diagram >}}

## Mapa conceptual - lección 3
### R base, packages, function, parameters, variables

{{< diagram >}}
graph LR;
A[R Languaje] -->|formed by| B[R base];
A -->|formed by| C[Packages];
C -->|has| D[Functions];
B -->|has| D;
D -->|can have| E[parameters];
A -->|work with| F[data estructures];
F -->|one is| G[variables] ;

{{< /diagram >}}


## Mapa conceptual - lección 4
### Mensajes, errors, warnings

{{< diagram >}}
graph LR;
A[Console] -->|executed| B[R code];
B -->|can give| C[mensages];
B -->|can give| D[warnings];
B -->|can give| E[errors];
C -->|all ok| F[informative/code executed];
D -->|something happened| G[informative/code executed];
E -->|something went wrong| H[code not executed];

{{< /diagram >}}


## Mapa conceptual - lección 5
### How to get help

{{< diagram >}}
graph LR;
A[Help] -->|how to ask| B[efficiently];
A -->|use R documentation in| C[RStudio help panel];
A -->|search in| D[Google];
A -->|consult| E[Cheat Sheet];
A -->|consult| F[CRAN Task Views];
A -->|search/ask| G[R-Studio Community];
A -->|search/ask| H[StackOverflow];
A -->|search/ask| I[Twitter];
A -->|ask/join| J[R Community];
B -->|using| K[sessionInfo];
B -->|using| L[dput];
{{< /diagram >}}

## Mapa conceptual - lección 6
### R Community: R-Ladies

{{< diagram >}}
graph LR;
A[R Community] -->|has| B[R User Groups];
C[R-Ladies] -->|are a type of| B;
C -->|has| D[Chapters];
D -->|one of them| E[R-Ladies Santa Rosa];
A -->|grow in| F[LatAm] ;
F -->|organize| G[LatinR];
F -->|translate| H[R4DS]
F -->|carry on| I[DatosDeMiercoles];
{{< /diagram >}}