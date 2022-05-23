---
date: "2022-05-23"
draft: false
summary: Necesitaba leer mas de 200 archivos markdown todos ubicados en diferentes carpetas y recuperar información de su YAML.  Aqui el detalle de como hice esta tarea.
title: Leyendo muchos archivos markdown de varias carpetas y extrayendo datos de su YAML
authors: Yanina Bellini Saibene
categories:
  - R
  - Español
tags: 
  - Technical tips

# Foto de Ilya Pavlov en Unsplash
---

## Contexto

Quienes han trabajado con sitios web armados con plantillas de Hugo saben que muchos de los blog post o cursos o charlas son carpetas que dentro contienen al menos un archivo markdown (extensión .md), que generalmente se llama `index.md` o `_index.md`.

Como muchos archivos markdown o rmarkdown, estos tienen al inicio un encabezado YAML.  El encabezado está entre tres guiones `---` y tiene parámetros.

Por ejemplo, el YAML de un blog post se puede ver de esta manera:

```
date: "2020-05-23"
draft: false
title: Leyendo muchos archivos markdown 
authors: Yanina Bellini Saibene
```

## El problema

Necesito obtener la fecha, el título y el evento de mis charlas, blog post, publicaciones para un reporte para mi trabajo. Todos estos datos están en mi sitio web, en más de 250 archivos markdown todos en diferentes carpetas. Necesito leerlos a todos y extraer información de su encabezado YAML, generar una tabla con esos datos y almacenarlo en un archivo CSV.

## La solución

La primero que hice fue separar el problema en pedacitos mas pequeños. 

* Paso 1: obtener el nombre de todos los archivos.

* Paso 2: Para cada archivo

  * Paso 2.a: leer los archivos dentro de cada carpeta

  * Paso 2.b: recuperar los valores de interés

  * Paso 2.c: grabar esos valores en una tabla

* Paso 3: grabar la tabla en un CSV  


Luego busqué por soluciones a cada paso, esto fue lo que encontré:

### Paso 1 - Obtener todos los archivos

El paquete `fs` tiene una función que recupera todas los archivos con un patrón determinado y que busca en todas las subcarpetas de una carpeta que le indiquemos. 

``` {r EVAL = FALSE}
file_list <- fs::dir_ls(path = "content/talk/", recurse = TRUE, type = "file", glob = "*.md")
```
Esto nos provee con un listado con todos los archivos a leer. Ahora genero un `tibble` para almacenar la información que quiero recuperar:

```
datos <- tibble(fecha = character(), titulo = character())
```

## Paso 2

Ahora debo recorrer todos los archivos para obtener los datos que necesito con este código.

```
for (documento in file_list){
  doc <- yaml::yaml.load_file(input = file.path(documento))
  datos <- tibble::add_row(datos, fecha = doc$date, titulo = doc$title)  
}

```

Me dio error con los archivos de los blog post porque no todo el contenido del archivo es YAML, pero pude recuperar la información de las charlas y los proyectos sin problemas, porque el texto en el rmarkdown es poco y en general sin caracteres especiales.

## Paso 3

Para grabar la información a un CSV uso

```
write_csv(datos, "fechas_eventos.csv")

```

## Lo que viene

Tengo que ver como hago esto mismo para los blog post sin que me de error.