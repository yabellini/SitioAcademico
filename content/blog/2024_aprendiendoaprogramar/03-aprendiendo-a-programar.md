---
title: "Tercer Encuentro. Aprendiendo a Programar en 30 lecciones"
weight: 3
subtitle: "Tercer encuentro"
excerpt: "Mi sobrino de 14 años quiere aprender a programar y yo voy a enseñarle. En esta clase aprendimos que son los paquetes, repasamos el proceso de analizar datos y descargamos los datos que vamos a usar para el resto de las clases"
date: 2024-03-05
draft: false
categories:
  - Español
  - rstats
  - Education
  - 100DaysToOffload
tags: 
  - Education
  - rstats
  - Español
  - 100DaysToOffload
---

## Ordenando nuestro trabajo

Proyectos

## Objetivo final de nuestro curso

## Leyendo y observando datos

read_csv("Data/pinguinos.csv")
pinguinos <- read_csv("Data/pinguinos.csv")
pinguinos
View(pinguinos)
View(pinguinos)
pin_xls <- readxl::read_excel("Data/pinguinos.xlsx")
str(pinguinos)
glimpse(pinguinos)
View(pinguinos)



## Ejercicio: analizando los datos que vamos a usar como ejemplo.

copas <- read_csv("Data/WorldCups.csv")
jugadores <- read_csv("Data/WorldCupPlayers.csv")
partidos <- read_csv("Data/WorldCupMatches.csv")
View(copas)
