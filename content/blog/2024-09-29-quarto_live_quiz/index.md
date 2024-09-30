---
title: "Adding Multiple choice quiz to Quarto Live Tutorials"
author: 
- Yanina Bellini Saibene
summary: "Adding multiple choice to a Quarto Live interactive tutorial" 
date: '2024-09-29'
categories:
  - Education
  - 100DaysToOffload
  - Open Source Software
tags:
  - Education
  - 100DaysToOffload
  - Open Source Software
---

[Quarto Live](https://r-wasm.github.io/quarto-live/) allows you to have [Embed WebAssembly](https://webassembly.org)-powered **code blocks and exercises** into a Quarto document with HTML-based output formats.  This is a great feature to create interactive tutorials with code exercises for teaching and learning R and Python.

Before Quarto Live [I build interactive tutorials with the `learnr` R package](https://learning-learnr.netlify.app). `learnr` provide a function called `quiz` that allows you to add multiple choice questions to your tutorials. This is how a multiple choice questions looks in learnr: 

{{< figure src="learnr_quiz.png" alt="Example of a multiple choice question created with the quiz function">}}

I was wondering if I could do the same with Quarto Live. This blog post present a my first attempt to add multiple choice questions to a Quarto Live document.

## Trying with the quiz function first

My first attempt was to use the quiz function from the learnr package but I got an error message related with the shiny runtime that each quiz question is executed. 

I don't know enough about Quarto and Shiny working together to try to troubleshot that error so I decided to try another approach.

{{< figure src="quiz_in_quarto.png" alt="quiz function in the Quarto Live document and error message">}}

## Interactivity in Quarto Live

[The Quarto Live extension](https://r-wasm.github.io/quarto-live/getting_started/installation.html) provides the interactive code blocks with syntax highlighting, and auto-complete. This code blocks can be transform in exercises with hints, solutions and custom grading algorithms.

This is how a _fill in the blanks_ exercise looks in Quarto Live:

{{< figure src="exercise_example.png" alt="fill in the blanks example exercise">}}

Quarto Live also provide integration with [Observable JavaScript](https://observablehq.com/@observablehq/observable-javascript) (OJS) so that interactive code cells update reactively with ojs cells.

I use it this feature to create a multiple choice question.  I like this type of questions to check for understanding of the content and provide differents type of exercises during a tutorial. 

## Multiple choice question in Quarto Live

I have a [tutorial to teach to create plots in R using ggplot2](https://learning-learnr.netlify.app/courses/treintadiasdegraficos/) package. [I migrate it to Quarto Live](https://github.com/yabellini/graficosEnR) and need it to add a multiple choice question to check if the student understand the concept of geometries in ggplot2.

The question: _How do you think the geometries for line and area charts could be named?_

I wanted to show the question and the options and then provide a feedback based on the answer selected. 

I adapted the [examples provided in the Quarto Live documentation about OJS reactivity](https://r-wasm.github.io/quarto-live/interactive/reactivity.html) to create the multiple choice.

We can create a reactive input using a ojs code block with a radio button group as input. The radio button group is created with the `Inputs.radio` function for the variable `respuesta` (answer in Spanish). 

The options for the radio buttons are provided as an array and the default value is defined in `value:` and correspond to the option "Ninguna de las anteriores" (None of the above). We set a default option to avoid an error on the output HTML.

``` r
```{ojs}
//| echo: false
viewof respuesta = Inputs.radio(
  [ "geom_line() y geom_bar()", "geom_linea(), geom_sup()", 
  "geom_area(), geom_histogram()", "geom_line(), geom_area()", 
  "Ninguna de las anteriores"],
  { value: "Ninguna de las anteriores", label: "Marca tu respuesta" }
);

html`${await do_respuesta(respuesta)}`

```

Now, I can pass the user selection to a function that evaluates the answer and provides a feedback. The last sentence in the code do exactly that: call the function `do_respuesta` passing the user selection (stored in `respuesta`), evaluates the answer and provides a feedback. The feedback is shown using HTML templating in OJS.

The template `awaits` the result of the `do_respuesta` function and dynamically updates the content. If we don't add the `awaits` the output show the promise object instead of the feedback.  

## The function that evaluates the answer

The function is created in a webr chunk of code. It should take reactive inputs as arguments, and be exported to OJS by setting the `define` code cell option. Here the exported function is named `do_respuesta()`. 

I hide the code cell from the rendered Quarto document output using the `edit: false` and `output: false` options.

The function provides different feedback based on the answer selected. I use HTML formatting to improve the readability and highlight the correct answer. `strong` shows the message in bold and `em` in italic.  

``` r
```{webr}
#| edit: false
#| output: false
#| define:
#|   - do_respuesta

do_respuesta <- function(respuesta) {
  if (respuesta == "geom_line() y geom_bar()") {
    return("<strong>Buen trabajo!</strong> `geom_line()` es para gráficos de líneas y `geom_bar()` es para gráficos de barras.")
  } else {
    return("<em>Vuelve a intentar</em>. En general a la palabra `geom_` se le agrega el nombre de la geometría en Inglés.")
  }
}
```

This is how the multiple choice question looks in the Quarto Live document:

{{< figure src="quartolive_quiz.png" alt="multiple choice question in the Quarto Live document">}}

In the Quarto document, the function definition has to be before the OJS code block that uses it.

## Conclusion

I was able to create a multiple choice question in a Quarto Live document using the OJS reactivity feature and the webr capability to create R code including functions. 

My tutorials can have multiple choice questions. Yay! 

It doesn't look as nice as the learnr quiz but I'm glad with the result of this first attempt. I will continue exploring the possibilities of Quarto Live to create interactive tutorials and exercises.
