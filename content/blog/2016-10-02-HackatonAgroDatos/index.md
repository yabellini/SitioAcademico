---
date: "2016-10-02"
draft: false
summary: "La investigadora pampeana Yanina Bellini Saibene recibió un diploma en Tecnópolis como una de las ganadoras del Primer Hackaton de Agro Datos organizado por el Programa de Ciencias de Datos de la Fundación Manuel Sadosky, dependiente del Ministerio de Ciencia y Tecnología de la Nación por el trabajo Yvytu, identificación de eventos climáticos con impacto agropecuario en noticias locales."
title: Mención para la EEA Anguil en el Hackatón de AgroDatos
authors: Yanina Bellini Saibene
weight: 1
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

La investigadora pampeana Yanina Bellini Saibene recibió un diploma en Tecnópolis como una de las ganadoras del "Primer Hackaton de Agro Datos" organizado por el Programa de Ciencias de Datos de la Fundación Manuel Sadosky, dependiente del Ministerio de Ciencia y Tecnología de la Nación por el trabajo "Yvytu: identificación de eventos climáticos con impacto agropecuario en noticias locales".

## ¿Qué es un Hackatón?

Un Hackatón es un encuentro de diversas disciplinas que en un tiempo determinado (en este caso 12 horas) intentan resolver una serie de problemas.  En un hackatón de AgroDatos las disciplinas que convergen son: la informática, ciencias agropecuarias, comunicación, diseño, geógrafos, entre otras, durante 12 horas para trabajar con datos del sector agropecuario.

Los productos y resultados esperados son propuestas de visualizaciones y formas útiles de navegar por los datos, análisis estadísticos novedosos a partir del cruzamiento de diversas fuentes de datos y prototipos de aplicaciones móviles para el sector.  Se seleccionaron como ganadores las propuestas más interesantes, originales, innovadoras y con potencial impacto en la producción

## ¿Quiénes participaron?

Yanina Bellini Saibene, investigadora en temas de Minería de Datos, del grupo de Información Agropecuaria y AgroTICs de la EEA Anguil, junto con Pablo Dobou, docente del FAMAF de la Universidad de Córdoba, e investigador en temas de Procesamiento de Lenguaje Natural desarrollaron la propuesta de identificar eventos climáticos con impacto agropecuario (granizo, heladas e inundaciones) en noticias locales.  La idea general es entrenar un modelo que, a partir del título de una noticia, pueda clasificarla como “Granizo”, “Inundación” o “Helada” y a partir del origen del diario, o la mención en la noticia, poder mapear los lugares donde ocurrieron estos eventos.

## ¿Por qué hacer Data Mining de Eventos Climáticos usando las noticias?

Los eventos climáticos severos, como el granizo, son de corta duración, intensos y localizados por lo que son difíciles de registrar e identificar a escalas regionales. 
Tampoco existe un sistema nacional que los registre, hay muchas diversas fuentes diseminadas (distintas escalas, detalles, formas de medición y disponibilidad). 
Los medios de comunicación y redes sociales son aceptados académicamente como fuente de verdad de campo para analizar este tipo de fenómeno y en el interior del país, la importancia de este tipo de eventos hace que se reflejen en las noticias.

## ¿Cómo se trabajó?

Para realizar esta tarea, se utilizó una técnica de entrenamiento supervisado.  Esto significa que se entrena al modelo con un conjunto de datos previamente etiquetado, esto significa, por ejemplo, que el clasificador ve muchos títulos que corresponden a noticias de granizo y muchos títulos que corresponden a noticias que no son sobre granizo.

En este caso el dataset tenía más de 27.000 noticias y contenía el título, la fuente y la etiqueta que indica el evento, siguiendo con el ejemplo, Granizo o No Granizo.  Estos datos se presentaron al software libre dbacl (http://dbacl.sourceforge.net/) de estadística Bayesiana, que a partir de ver que palabras se usan en un título de granizo y cuales en un título que no es granizo “aprende” a diferenciarlas.

Clasificar a partir de palabras, tiene muchas particularidades, por ejemplo, uno de los inconvenientes que tiene el software es diferenciar las palabras que tienen más de un significado, en nuestro caso la palabra Piedra, en ocasiones hace referencia a la caída de granizo y en otras no (Ej: un título que decía “Le tiraron piedras”).  Cuando el clasificador dice que una noticia es sobre granizo, cuando en realidad no lo es, se dice que el modelo “confunde” y clasifica de forma incorrecta la noticia (falso positivo).  A medida que se cuenta con más datos y más noticias, el clasificador se puede ir mejorando para que no cometa estos errores.

Finalmente, se geolocalizaron más de 150 fuentes de información para poder armar los mapas de los lugares donde se detecta una noticia referida a uno de estos eventos y se armó un software (llamano API) que permite usar el clasificador, por lo que se pasa un título como parámetro y el software devuelve si es o no granizo.  Este software se puede acceder desde el repositorio libre: https://github.com/DrDub/yvytu

## ¿Cuáles son las posibles aplicaciones?

- Conocer posibles eventos que afecten de forma negativa a la producción agropecuaria por provincia/localización.

- Tener disponible un set de datos de ocurrencia de eventos climáticos adversos.

- Utilizar estos set de datos para mejorar/generar modelos de riesgo/ocurrencia.

- Poner foco en aquellos problemas que pueden resultar importantes (punto de vista empresario, gubernamental, etc).

> Publicado originalmente en la web de la EEA INTA Anguil.
