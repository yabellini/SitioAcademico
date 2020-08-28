---
title: Lección 6 - Manejo de datos rasters
linktitle: Lección 6 
toc: true
type: docs
date: "2020-01-05T00:00:00+01:00"
draft: false
menu:
  gee_cai2019:
    name: Lección 6 - Manejo de datos rasters
    weight: 7

# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 7
---

## Manejo de datos rasters

En la plataforma existe una gran cantidad de fuentes de información entre las que se incluye tanto información de base como imágenes satelitales, bases de datos meteorológicas, como productos generados: Modelos Digitales de Elevación (DEMs), Máscaras de cuerpos de agua y áreas urbanas, etc.

En este caso vamos a seleccionar un producto y lo vamos a filtrar (acotar) a las necesidades particulares (intervalo de tiempo y área de interés), ya que generalmente el alcance es global y se disponen largas series temporales.
Una de las características más interesantes de la plataforma GEE es la capacidad de analizar catálogos completos de imágenes satelitales o productos cartográficos sin la necesidad de descargarlos. Para buscar y acceder a los catálogos disponibles, basta con explorar en el cuadro de búsqueda que se encuentra sobre el editor.

Entre los productos de sensores remotos más interesantes se puede mencionar la colección completa de imágenes MODIS, Landsat (4, 5,7 y 8), Sentinel 1 y 2, ASTER, además de productos como el mapa de cambios forestales global de Hansen (Hansen Global Forest Change), FIRMS: Fire Information for Resource Management System, el mapa global de cultivos y fuentes de riego (Global Cropland Extent and Watering Source), el mapa global de aguas superficiales (JRC Global Surface Water Mapping Layers), entre otros.

Cada producto tiene un código asociado (ImageCollection ID) y una nomenclatura de bandas. El buscador del Code Editor permite ver las colecciones disponibles, el ID y las bandas, presenta una breve explicación del producto y el origen del mismo.
