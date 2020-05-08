---
title: Concept Map - Class 2
linktitle: Concept Map
toc: true
type: docs
date: "2020-01-05T00:00:00+01:00"
draft: false
menu:
  rdesdecero:
    name: Concept Map - Class 2
    weight: 4

# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 1
---


## Concept Map - Lesson 1
### Data structures. 


{{< diagram >}}

graph LR;

B[data estructures] -->|a single data| C[variables]; 
B -->|multiple data| D[vector]; 
B -->|multidimentional vector| E[matrix];
C -->|same type| F[atomic vector];
D -->|same length| G[data.frame];

{{< /diagram >}}

## Concept Map - Lesson 2
### Data structures

{{< diagram >}}
graph LR;
A[tibble] -->|a type of| B[data.frame];
A -->|has| C[columns];
A -->|has| D[rows];
C -->|must be the same| E[type of data];
E -->|cuantitative| F[double, integer];
E -->|cualitative| G[logical, character];
{{< /diagram >}}

## Concept Map - Lesson 3
### Function to see data set structure

{{< diagram >}}
graph LR;
A[function] -->|show data structure| B[type name of data];
A -->|show data structure| C[view()];
A -->|show data structure| D[glimpse()];
A -->|show data structure| D[kable()];
{{< /diagram >}}


## Concept Map - Lesson 4
### Mensajes, errors, warnings



## Concept Map - Lesson 5
### How to get help

