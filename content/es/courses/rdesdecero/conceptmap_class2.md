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

B[estructura de datos] -->|un solo dato| C[variable]; 
B -->|multiples datos| D[vector]; 
B -->|vector multidimensional| E[matríz];
C -->|del mismo tipo| F[vector atómico];
D -->|varios del mismo largo| G[data.frame];

{{< /diagram >}}

## Mapa Conceptual - Lección 2
### Estructuras de Datos

{{< diagram >}}

graph LR;

A[tibble] -->|un tipo de| B[data.frame];
A -->|tiene| C[columnas];
A -->|tiene| D[filas];
C -->|debe tener el mismo| E[tipo de dato];
E -->|cuantitativo| F[doble/double, entero/integer];
E -->|cualitativo| G[lógico/logical, caracter/character];

{{< /diagram >}}

## Mapa Conceptual - Lección 3
### Como ver la estructura de los datos

{{< diagram >}}

graph LR;

A[función] -->|muestra| B[la estructura de los datos];
A -->|muestra| B;
B --> C[view];
A -->|muestra| B;
B -->D[glimpse];
A -->|muestra| B;
B -->E[kable];

{{< /diagram >}}


> Si querés obtener más información sobre los Mapas Conceptuales y cómo enseñar podés consultar acá este libro https://teachtogether.tech/es/index.html y esta web https://www.metadocencia.org/
