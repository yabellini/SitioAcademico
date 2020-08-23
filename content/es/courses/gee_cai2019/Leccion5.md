---
title: Lección 5 - Operaciones Básicas sobre FeaturesCollection
linktitle: Lección 5 
toc: true
type: docs
date: "2020-01-05T00:00:00+01:00"
draft: false
menu:
  gee_cai2019:
    name: Lección 5 - Operaciones Básicas sobre FeaturesCollection
    weight: 6

# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 6
---


## Operaciones básicas 

A continuación se presetna el código necesario para realizar operaciones básicas sobre FC como listar atributos desde el primer feature, contar instancias, calcular area promedio...

```{js}
var mis_Desmontes = ee.FeatureCollection('users/hernanelena/Desmonte_anta')

Map.addLayer(mis_Desmontes, {}, 'Áreas Desmontadas');

Map.centerObject(mis_Desmontes);

print(mis_Desmontes.limit(1)); // Limitamos el # de features

print('Lista de atributos:',mis_Desmontes.first().propertyNames()); 

//Listar los atributos del primer feature
print('Cantidad: ', mis_Desmontes.size()); // # de features en la colección

// Contar cuántas instancias de cada clase hay
print('Clases Distintas:',  mis_Desmontes.aggregate_count_distinct('Fecha')); //fecha de desmonte

// Suma toda la columna area_ha
print('Superficie Total (Ha):', mis_Desmontes.aggregate_sum('Superf_ha'));

// superficie promedio
print('Superficie promedio (Ha):', mis_Desmontes.aggregate_mean('Superf_ha'));
```


### Filtrado de FC
Todos los objetos de tipo colección tienen una método de aplicación de filtros (.filter) que a menudo requieren como parámetro de un objeto del tipo ee.Filter.  
Importante: los filtros aplican sobre las instancias, es decir, sobre las filas.

var rectangulo_filtro =
	/* color: #d63000 */
	/* displayProperties: [
  	{
    	"type": "rectangle"
  	}
	] */
	ee.Geometry.Polygon(
    	[[[-63.872056453539074, -25.34231021433682],
      	[-63.872056453539074, -25.4124139888941],
      	[-63.81094500334376, -25.4124139888941],
      	[-63.81094500334376, -25.34231021433682]]], null, false);

var filtrados = mis_Desmontes.filterBounds(rectangulo_filtro);
Map.addLayer(rectangulo_filtro,{color: 'f4df42'},'Region a filtrar')
print('Cantidad de features después de filtrar:', filtrados.size());

var filtradasXarea = filtrados.filter(ee.Filter.lt('Superf_ha', 90));

print('Parcelas menores de 90 ha:', filtradasXarea.size());
Map.addLayer(filtradasXarea, {color: 'f54260'}, 'Menores de 90 ha')

Iteraciones sobre colecciones de features
Una forma simple de modificar cada uno de los Features de un FeatureCollection es utilizando la instrucción ee.FeatureCollection.map. Esta instrucción permite recorrer cada Feature y generar un FeatureCollection nuevo.
Veamos un ejemplo simple, supongamos que queremos incorporar al FeatureCollection de las parcelas de desmontes  un atributo que sea perímetro. Esto requiere que para cada elemento (de tipo Feature) de la colección hagamos el cálculo, eso sería:
var get_perimetro = function(elemento){
    	return elemento.set(
        	{perimetro: elemento.geometry().perimeter()}
    	);
}
var desmonte_con_perimetro = mis_Desmontes.map(get_perimetro);
print(desmonte_con_perimetro);

Otro ejemplo de map, supongamos que tenemos un CSV con coordenadas expresadas en grados decimales y queremos generar la geometría para cada Feature del FeatureCollection
