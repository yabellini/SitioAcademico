---
title: "AgroMet Package"
subtitle: ""
excerpt: "The {agromet} package includes a series of functions to calculate climatic and hydrological indices and statistics from tidy data."
date: 2019-07-02
author: "Yanina Bellini Saibene"
featured: true
draft: false
tags:
  - package
categories:
  - R
  - package
# layout options: single or single-sidebar
layout: single-sidebar
links:
- icon: github
  icon_pack: fab
  name: code
  url: https://github.com/AgRoMeteorologiaINTA/agromet
#- icon: newspaper
#  icon_pack: far
#  name: Blog post
#  url: https://education.rstudio.com/blog/2020/07/palmerpenguins-cran/
---

<img src='featured.jpg' align="right" height="500" alt='Hex sticker of the package. Shows a rainf of 0 and 1 and a field with the word AgroMet.'/>

The {agromet} package includes a series of functions to calculate climatic and hydrological indices and statistics from tidy data. For example `thresholds()` allows to count the number of observations that meet a certain condition and `average_days()` returns the first and last day of the average year of occurrence of an event.

Other functions such as `spi()` function as function wrappers for other packages and seek to be compatible with the handling of tidy data.

Finally, the package includes a `map()` georeferenced data graphing function with INTA's own style and logo.
