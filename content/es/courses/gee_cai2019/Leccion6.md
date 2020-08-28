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

### Explorando catálogo de datos

Una de las características más interesantes de la plataforma GEE es la capacidad de analizar catálogos completos de imágenes satelitales o productos cartográficos sin la necesidad de descargarlos. Para buscar y acceder a los catálogos disponibles, basta con explorar en el cuadro de búsqueda que se encuentra sobre el editor.

Entre los productos de sensores remotos más interesantes se puede mencionar la colección completa de imágenes **MODIS, Landsat (4, 5,7 y 8), Sentinel 1 y 2, ASTER**, además de _productos_ como el mapa de **cambios forestales global de Hansen (Hansen Global Forest Change), FIRMS: Fire Information for Resource Management System, el mapa global de cultivos y fuentes de riego (Global Cropland Extent and Watering Source), el mapa global de aguas superficiales (JRC Global Surface Water Mapping Layers)**, entre otros.

Cada producto tiene un código asociado (_ImageCollection ID_) y una nomenclatura de bandas. El buscador del _Code Editor_ permite ver las colecciones disponibles, el ID y las bandas, presenta una breve explicación del producto y el origen del mismo.

{{< figure src="Buscador.png" title="Busqueda de un recurso e importación en nuestro script" >}}


Para agregarla a nuestro script basta con pulsar el botón de _Import_, pero para efectos de este ejercicio lo agregaremos de forma manual copiando el ImagenCollection ID, en este caso _LANDSAT/LC8_, y copiando el siguiente comando, donde la función objeto _ee.ImageCollection_ indica que el elemento a ser añadido.

```{js}
// Seleccionado un producto de la colección. En este caso Landsat 8 Tier1 TOA Reflectance
var landsat8 = ee.ImageCollection('LANDSAT/LC08/C01/T1_RT_TOA');

```

Cada elemento de la colección instanciada en la variable Landsat8 es a su vez un objeto de tipo _ee.Image_.
A partir de aquí comenzaremos a utilizar filtros que permitan limitar la cantidad de imágenes dentro del área y el periodo que deseamos analizar. Para ello haremos uso de las funciones _.filterDate_ y _.filterBounds_. Donde _.filterDate_ indica la temporalidad de las imágenes y _.filterBounds_ indica los límites geográficos de las imágenes que deseamos analizar.

Para tener en cuenta:
*	Los filtros aplican sobre metadatos, valores de la imagen o utilizando geometrías.
*	Las selecciones aplican sobre las bandas.

Para filtrar primero definimos una región. Lo podemos hacer usando polígonos creados con las herramientas de GEE o invocando una que este por ejemplo en el ASSEST.  Agregar las siguientes líneas al código:


// área de estudio
var area_estudio = ee.FeatureCollection('users/hernanelena/yungas');
Map.addLayer(area_estudio)
Aplicaremos filtros y observaremos la consola.
//Filtrado de la colección Landsat8
var landsat8_filtrada=    landsat8
                 // filtro por el área de estudio
                .filterBounds(area_estudio)
                // filtro por rango de fechas
                .filterDate('2016-01-01', '2016-12-31')
                //filtro por mes                      	                     .filter(ee.Filter.calendarRange(6,10,"month"))
                //filtro por cobertura nubosa. En este caso menor al 20%
                .filterMetadata('CLOUD_COVER','less_than', 20);
                // filtro por path row
                //.filterMetadata('default:WRS_PATH','equals', 231)
                //.filterMetadata('default:WRS_ROW','equals', 86);
                       	 
// selección
print  ("Colección filtrada: ",landsat8_filtrada);


Seleccionar bandas de interés:
// Selección de bandas
var bandas = ['B2','B3','B4','B5','B6','B7']
landsat8_filtrada = landsat8_filtrada.select(bandas);
print  ("Colección filtrada con bandas filtradas: ",landsat8_filtrada);

Si nuestro deseo es realizar un apilamiento de imagenes L5, L7 y L8 para una futura clasificación, es conveniente normalizar los nombres de las bandas. Pues la B1 de Landsat 5 no es la misma que la B1 de Landsat 8. Para ello podemos hacer una función que cambie el nombre de las bandas. Esto se aplicará a las diferentes colecciones si fuera necesario:

//Funciones para cambiar nombre de bandas
var changeBandNameL5L7 = function(image) {
  return image.select(
  ['B1','B2', 'B3', 'B4', 'B5', 'B7'],  
  ['BLUE', 'GREEN', 'RED', 'NIR', 'SWIR1','SWIR2'])};

var changeBandNameL8 = function(image) {
  return image.select(
  ['B2', 'B3', 'B4', 'B5', 'B6', 'B7'],  
  ['BLUE', 'GREEN', 'RED', 'NIR', 'SWIR1','SWIR2'])};
  
var  l8= changeBandNameL8(landsat8_filtrada);
print (l8);

El objeto ee.ImageCollection implica un catálogo, un grupo de imágenes. Para poder generar nuevas bandas, o exportar se requiere convertirla al objeto ee.Image. Esto se puede hacer creando una imagen a partir de bandas de la colección o aplicando algoritmos de reducción a la colección (e.g:mediana, promedio o valor máximo de pixels). En este caso, vamos a obtener como resultado una única imágen para cada banda (ahora objeto ee.Image), la cual puede ser posteriormente exportada y permite generar índices a partir de sus bandas.
// Aplicar reducción de mediana 
// con .clip  recorto la imagen por el area de estudio
var stackL8 = l8.median().clip(area_estudio);

// ver imagen en mapa:
Map.addLayer( stackL8, {bands: ['NIR', 'SWIR1', 'GREEN'], min: [0,0,0], max:[1,1,1] } , "Landsat 8 " );
print ('Stack: ',stackL8);

StackL8 será una imagen de 6 bandas donde cada pixel es la mediana de los pixeles de la colección que habíamos filtrado (imágenes de 2016).
Supongamos que deseamos posteriormente realizar una clasificación supervisada para determinar desmontes ocurridos entre periodos 2010 y 2016.
Para esto deberemos realizar un mosaico único,  como en el ejemplo anterior, de 2010 y apilarla  con la de 2016.
