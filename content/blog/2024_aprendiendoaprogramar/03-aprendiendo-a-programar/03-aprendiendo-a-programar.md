---
title: "Aprendiendo a Programar en 30 lecciones"
weight: 1
subtitle: "Tercer encuentro"
excerpt: "Mi sobrino de 14 años quiere aprender a programar y yo voy a enseñarle. En esta clase aprendimos que son los paquetes, repasamos el proceso de analizar datos y descargamos los datos que vamos a usar para el resto de las clases"
date: 2024-02-05
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

## Lenguaje de programacion e IDE

Vamos a usar R como lenguaje de programación y RStudio como una IDE (Integrated Development Environment), un Entorno Integrado de Desarrollo.  Estas son dos herramientas diferentes. 



copas <- read_csv("Data/WorldCups.csv")
jugadores <- read_csv("Data/WorldCupPlayers.csv")
partidos <- read_csv("Data/WorldCupMatches.csv")
View(copas)
