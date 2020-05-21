---
date: "2020-05-21"
draft: false
type: page
linktitle: Packaging interactive tutorials
summary: Mini tutorial to generate graphics in R celebrating Florence Nightingale
title: Packaging interactive tutorials 
authors: 
    - admin
type: post
weight: 1
tags: 
  
---

On May 12, #30díasdegráficos (30 days of plots) with R, started. This is an initiative of the Spanish-speaking community of R to remember Florence Nightingale and learn about data visualization.

The challenge: create and share a graphic a day. More info on how to participate [here](https://github.com/cienciadedatos/datos-de-miercoles/blob/master/30-dias-de-graficos-2020.md)

Since I could not participate making the graphics for each day, I generated this **mini tutorial** using the `learnr` package (my new favorite package) where I explain how to make a series of graphics with` ggplot2`. If you like it, I promise to improve it and add graphics to it. If you want to collaborate [here is the repo](https://github.com/yabellini/tutorialgRaficosFN)

My goals to generate this tutorial were:

 * learn how to generate a tutorial package developed in learnr
* include in the tutorial a series of pedagogical tools described in the book [Teaching Tech Together](teachtogether.tech/)
* that you could take advantage of the new Tutorial panel that comes in the [new version of RStudio](https://rstudio.com/products/rstudio/download/preview/).
* learn how to change the tutorial styles based on [this post](https://education.rstudio.com/blog/2020/05/learnr-for-remote/)
* to make a contribution to the celebration of Florence Nightingale 

That is why the tutorial includes a concept map with the topics it covers, two learner personas wich represent the people I thought about when I build the tutorial, the license, a series of explanations and exercises to make plots with R-and the sources.

To install the package you have to download the [.tar.gz](https://github.com/yabellini/tutorialgRaficosFN/blob/master/TutorialgRaficosFN_0.1.0.tar.gz) or [.zip (only for Windows)](https://github.com/yabellini/tutorialgRaficosFN/blob/master/TutorialgRaficosFN_0.1.0.zip) file and install the `tutorialgRaficosFN` package from the option **Tools -> Install Packages -> Install from -> Package Archive File (.zip; .tar.gz)**. If you have the latest version of RStudio it will appear in your Tutorial panel.

If you don't have the latest version then you have to install the [learnr package](https://rstudio.github.io/learnr/index.html) and then run the Tutorial like this:

`learnr::run_tutorial("graficos", package = "TutorialgRaficosFN")`


Here's what the tutorial looks like when it's running:

 {{< figure src="/img/learnr_conceptmap_ggplot.png" alt="Mapa conceptual del tutorial de gráficos">}}
 
 {{< figure src="/img/learnr_contenido_ggplot.png" alt="Ejemplo del contenido del tutorial">}}


I hope this is useful and fun .... I had fun and learned a lot building it.
