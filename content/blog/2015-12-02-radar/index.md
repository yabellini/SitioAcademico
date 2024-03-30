---
date: "2015-12-02"
draft: false
summary: Resumen de las actividades relacionadas con el radar meteorologico de la EEA Anguil del Area de Informacion Agropecuaria y AgroTICs de la EEA Anguil
title: "Radar Meteorológico: mirando al cielo pensando en la tierra"
authors: Yanina Bellini Saibene
categories:
  - Español
  - Data Science
  - Agro
  - Remote Sensing
tags: 
  - Teledetección
  - Agro
  - Ciencia de Datos
---

{{< figure src="featured.jpg" alt="Radar Meterologico y dos imagenes generadas por el software desarrollado en la EEA Anguil">}}

Los radares meteorológicos son sensores activos de teledetección que emiten pulsos de energía electromagnética hacia la atmósfera en el rango de frecuencias de las microondas.  Las partículas contenidas en la atmosfera interceptan y devuelven parte de esa energía al radar, la cual es medida y se denomina reflectividad.  Indica la intensidad de los ecos recibidos y depende de los parámetros físicos del objeto a medir, como su tamaño, forma, orientación y composición.  

El radar ubicado en INTA Anguil es de industria alemana marca Gematronik modelo Meteor 600C. Posee sistema doppler y es de doble polarización. Opera en banda C a una frecuencia de 5,64 Ghz y longitud de onda de 5,4 cm [11].  La información registrada por el radar es recolectada a través de escaneos volumétricos y los datos son almacenados en archivos separados llamados volúmenes.  Los datos contienen las distintas variables medidas.  Se distinguen dos tipos de datos: a) Datos “crudos” y b) Datos con algún nivel de procesamiento o “productos”.  La cantidad de información registrada y sus posibles aplicaciones plantean desafíos en cuanto al procesamiento de la información recolectada (tanto en línea, como la generación de productos), ii) su almacenamiento (presentando problemática de grandes datos), iii) la generación de los metadatos correspondientes y iv) los servicios de acceso a datos.

Durante este año las investigaciones se concentraron en validar el producto de Precipitación acumulada (Tesis de maestría Ing. Laura Belmonte, UNS, aprobada con 10) y generar [modelos de estimación de granizo en superficie y daño en cultivos por medio de técnicas de Data Mining](https://prezi.com/t_hpyc6dpw1j/maestria-en-explotacion-de-datos-y-gestion-del-conocimiento/) (tesis de maestría Lic. Yanina Bellini Saibene, Austral, aprobada con 10).  


Los primeros productos son: 

* Desarrollo [software libre](https://github.com/INTA-Radar) que permite [descargar los archivos del radar, transformarlos de un formato propietario (que implica el uso de un software comercial) a dos formatos estándares (ASCII y GeoTIFF) y procesarlos, generando también más productos](http://inta.gob.ar/documentos/desarrollo-y-uso-de-herramientas-libres-para-la-explotacion-de-datos-de-los-radares-meteorologicos-del-inta) a partir de los datos crudos.

* [Sistema de información con los datos de campo de ocurrencia de granizo](http://rian.inta.gov.ar/daniogranizo/). [Trabajo completo](http://inta.gob.ar/documentos/har-hail-archive-desarrollo-de-un-sistema-de-informacion-y-base-de-datos-sobre-granizo-en-la-region-semiarida-pampeana-central)
