---
title: Mapas Conceptuales - Clase 2
linktitle: Mapas conceptuales
toc: true
type: docs
date: "2020-01-05T00:00:00+01:00"
draft: false
menu:
  rdesdecero:
    name: Mapas Conceptuales - Clase 2
    weight: 4

# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 1
---


## Mapa Conceptual - Lección 1
### Estructuras de datos. 


{{< diagram >}}

graph LR;

B[data estructures] -->|a single data| C[variables]; 
B -->|multiple data| D[vector]; 
B -->|multidimentional vector| E[matrix];
C -->|same type| F[atomic vector];
D -->|same length| G[data.frame];

{{< /diagram >}}

## Mapa Conceptual - Lección 2
### Estructuras de Datos

{{< diagram >}}
graph LR;
A[tibble] -->|a type of| B[data.frame];
A -->|has| C[columns];
A -->|has| D[rows];
C -->|must be the same| E[type of data];
E -->|cuantitative| F[double, integer];
E -->|cualitative| G[logical, character];
{{< /diagram >}}

## Mapa Conceptual - Lección 3
### Como ver la estructura de los datos

{{< diagram >}}
graph LR;
A[function] -->|show data structure| B[type name of data];
A -->|show data structure| C[view()];
A -->|show data structure| D[glimpse()];
A -->|show data structure| D[kable()];
{{< /diagram >}}
