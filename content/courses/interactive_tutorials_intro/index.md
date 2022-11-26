---
title: "Introduction to interactive tutorials"
subtitle: ""
excerpt: "Learn how to use {learnr} and {gradethis} packages for build interactivew tutorials using R"
date: 2020-10-03
author: "Yanina Bellini Saibene and Paola Corrales"
featured: true
draft: false
tags:
  - Community
  - Education
  - MetaDocencia
  - R
  - packages
categories:
  - Community
  - Education
  - Español
  - R
# layout options: single or single-sidebar
layout: single-sidebar
links:
- icon: images
  icon_pack: fas
  name: slides
  url: https://docs.google.com/presentation/d/1pE8sp9jT7KSW-YRgd_z_60V0nx4zZuZyPRZy1BKuJ_g/edit?usp=sharing
- icon: youtube
  icon_pack: fab
  name: video
  url: https://youtu.be/BGmM_E6BrRI
- icon: github
  icon_pack: fab
  name: code
  url: https://github.com/yabellini/curso_learnr
  
---

### Objectives 

To introduce the {learnr} and {gradethis} packages and show how to use it to create interactive tutorials. These interactive tools allow the students to run R code directly in the tutorial, to answer to questions and to receive immediate feedback. 

### Intended public of this course

When we designed this workshop, we had in mind Josefina, Francisco and Alex as our learner personas. 

* _Josefina_: teaches R at University. She is interested in giving automated feedback to the R exercises given to her students. 

* _Francisco_: is a professional developer and wants to explore the interactive tutorials as possible part of the help and documentation of his packages. 

* _Alex_: wants to develop tutorials to publish them as shiny applications so that their students could start right away with R without painful installations. 


### _Not_ included in this workshop

Since we only have 3 hours, a lot of things will be out of reach of the workshop. Among other things, we will not learn:

* Programming techniques 
* Theory of pedagogy
* Rmarkdown 
* Package development

### Duration

This is a 3-hour workshop with intervals (ideally away from any screen) of approximately 5 minutes for every 50 minutes of content.

### Sample schedule 


|  Duration (min) |  Activity  |
| ---:  | :----------- |
 | 5  <img width="150"/>|  Time to connect and make sure your audio and video connection is good (if you don't have a camera it doesn't matter, but if you do, it helps)|
 | 10 |  Introduction to the course |
 | 15 |  What is an interactive tutorial? |
 | 15 |  How can I add questions to my tutorial? |
 | 10 |  Break |
 | 15 |  How can I include coding exercises in my tutorial? |
 | 15 |  How can I check the coding exercises in my tutorial? |
 | 15 |  How can I share my tutorials? |
 | 10 |  Where could I learn more about {learnr} tutorials? |
 | 5  | End of the workshop: summary and feedback |

#### Chapter 1

* Question: What is an interactive tutorial?
* Goals:
    - Understand the benefits of an interactive tutorial
    - Understand the basic different parts of the {learnr} tutorials
* Practice:
    - Analyze a {learnr} tutorial template and recognize the different parts. Modify options in the YAML and analyze the changes.

#### Chapter 2

* Question: How can I add questions to my tutorial?
* Goals:
    - Understand the different type of questions
    - Understand the basic components of multiple choice questions
    - Understand the basic components of text questions
* Practice: Modify some of the questions of the  tutorial provided for this exercise.

#### Chapter 3

* Question: How can I include coding exercises in my tutorial? 
* Goals:
    * Understand the basic components of the exercises
    * Understand the chunk exercise
    * Understand the chunk hint
    * Understand the chunk solution
    * Understand the default set up of the chunks
* Practice: Modify an exercise chunk in order to provide a hint and a solution

#### Chapter 4

* Question: How can I check the coding exercises in my tutorial?
* Goals:
    * Understand the different ways to check code exercises
    * Understand the advantages and shortages of the different options
* Practice: Modify an exercise checking test to provide more feedback.

#### Chapter 5

* Question: How can I share my tutorials?
* Goals:
    * Understand the different ways to publish/share a {learnr} tutorial 
    * Understand the advantages and shortages of the different options
* Practice: Publish the tutorial as a Shiny App

#### Chapter 6

* Question: Where can I learn more?
* Goals:
    * Details of sites to learn more about {learnr}
    * Details of the packages that can be combined with {learnr}
    * Details of repositories with code that generate learnr tutorials.


### Do you want to re-use any of our contents? Please, be our guest!

Our materials are available for free under this [license](https://creativecommons.org/licenses/by/4.0/deed.es). You can reuse or edit any material that appears here, the only thing we ask in return is that when you reuse our materials you include a reference to this website.

> This course was developed for MetaDocencia. (2021 and 2022)