---
title: "Learning to code in 30 lessons"
weight: 1
subtitle: "First class"
excerpt: "My 15 year old nephew wants to learn to program and I'm going to teach him. This is the first blog post of our journey together detailing how to set up the environment we will be using for the rest of the classes."
date: 2024-02-05
draft: false
categories:
  - Education
  - 100DaysToOffload
  - English
  - rstats
tags: 
  - Education
  - 100DaysToOffload
  - English
  - rstats
---

My 15 year old nephew wants to learn how to program and I'm going to teach him. This is the first blog entry of our journey together. 

The idea of the first meeting was to chat about what I could teach him and to agree when we would get together. Because of his enthusiasm we also set up the whole environment to be able to have the classes.

## Learning objective

The overall objective at the end of the course is for Juan Cruz to be able to read data files, analyze and process them to make proper aggregations and visualizations, generate a report with his results and publish it on the web. All this with good practices to be able to share and reproduce his work.

## Work environment

We start by installing the software we need:

### Installing R

These steps correspond to **Windows**

- Go to <https://cran.r-project.org/bin/windows/base/> and download the installer by clicking on the big link that says *"Download R x.x.x for Windows"*.

- Once downloaded, double click on the file and follow the installer instructions.

- Once the installation is finished, you will see an icon like this on your desktop or in the installed programs: {{< figure src="r-logo.jpeg" height="20px" >}}}

- When you run it, you should see something like this:

![](r-en-windows.png) 

If you see a window like this it means that you already have R installed, but read on! **There are still a few steps left** to take full advantage of it: we need to install **RTools**.

### Installing RTools

To install some R packages on Windows you will need to install an additional program called rtools. 

1. Go to https://cran.r-project.org/bin/windows/Rtools/ and download the latest version installer, at this moment it is Rtools43. Click on Rtools43 and in the new page click on [Rtools43 installer](https://cran.r-project.org/bin/windows/Rtools/rtools43/files/rtools43-5948-5818.exe).  

2. Execute the installer and follow the instructions. 

3. Open the R console, type this in the console and press enter:

```{r, eval = FALSE}
Sys.which("make")
```

It should come out something like this:
````{r, echo=FALSE}
c(make = "C:\rtools40\usrtmake.exe")
```

### Installing RStudio

- Go to the Posit website and download RStudio for desktop: https://download1.rstudio.org/electron/macos/RStudio-2023.12.1-402.dmg.

- Once downloaded, as usual, double click on the file and follow the installation steps.

- Once the installation is finished, you should see a window like this when you run RStudio:


![](rstudio-principal.png) 

### Create a GitHub account.

- Go to https://github.com/.

- Click on Register or Sign up.

- Follow the prompts to create your personal account.

- One of the steps involves checking that you are a person and then validating the email address you used to create the account. 

## First exercise

Create the profile on github:

1 - create a repo with the same name as your github user.

2 - Add a README.md file to it. 

3 - Think about what you want to put in your profile and modify the readme with that information. Have it ready for the next class.
