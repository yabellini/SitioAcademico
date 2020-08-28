---
title: Lección 7 - Extraer información del raster
linktitle: Lección 7 
toc: true
type: docs
date: "2020-01-05T00:00:00+01:00"
draft: false
menu:
  gee_cai2019:
    name: Lección 7 - Extraer información del raster
    weight: 8

# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 8
---

## Extraer información del raster

Earth Engine permite extraer rápidamente información de las imágenes seleccionadas, exportarla o analizarla desde la plataforma.

Para extraer información de nuestra imagen vamos a utilizar geometría de puntos la cual contendrá:

*	Clase 1: desmontes ocurridos en el periodo 2010-2016
*	Clase 2: Cultivos existentes en 2010  y 2016
*	Clase 3: Bosque en 2010 y 2016

Copiar el siguiente código y pegarlo en el Scripts

Esto generará FeatureCollections con información de los puntos que son cargadas en el código al inicio.
Al pegar esta sección de código y apoyar el mouse sobre este, preguntará si queremos convertir a registros importados, a lo que le indicamos “Convert”. De esta manera ubica el código de los puntos agregados en una sección diferente (al inicio, en imports):
 

Para extraer la información primero debemos unificar todas las clases en un solo FC
// Extracción de información
// Unir muestras por clase en un único FeatureCollection    
// podemos hacerlo de varias formas Ej:

var puntos = ee.FeatureCollection([Cambios1016,Cultivos,BosqueEstable]).flatten();
print ('Puntos',puntos)

// Otra forma de unificar
//var puntos2 = Cambios1016.merge(Cultivos).merge(BosqueEstable);
//print ('puntos2',puntos2);

Luego utilizaremos sampleregion para extraer información. Hay que indicar la imágen a utilizar (“stack_completo”), los atributos del vector (FeatureCollection) que se desean mantener (atributo “clase”) y la escala (resolución de la imagen):
// extraer información:
var training = stack_completo.sampleRegions({
  collection: puntos,
  properties: ['clase'],
  scale: 30
});

// Los puntos ahora tendran la informacion de cada banda de la imagen stack
print (' puntos de muestras',training);

// exportar tabla con información
Export.table.toDrive({
	'collection': training,
	'description': 'muestrasCAI',
	'fileNamePrefix': 'muestrasCAI',
	'fileFormat': 'CSV'}
);
