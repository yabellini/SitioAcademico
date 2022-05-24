---
title: "Creando una página web bilingüe en R"
summary: Esta es la segunda entrega de una serie de post sobre como generar un sitio web estático con R.
date: "2020-12-17"
authors: 
  - Pamela Pairo
  - Natalia Morandeira
  - Yanina Bellini Saibene
categories:
  - Education
  - Español
tags:
  - blogdown
  - Hugo
  - Portfolio
  - Netlify
  - website
  - R
  - Technical tips
  - Multilingual
---

{{< figure src="/img/spoon_web.jpg">}}
*<span>Photo by <a href="https://unsplash.com/@joannakosinska?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Joanna Kosinska</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>*

En la [nota anterior](https://yabellini.netlify.app/es/post/hacerweb1/) te comentamos algunas ventajas de tener una página web personal. También, resumimos en un esquema los 3 partes en las que se puede dividir el proceso. A continuación nos explayaremos en cada parte y construiremos la página web personal.

<img src="/img/esquema_1.png" width="90%"/>

## En GitHub: crear un repositorio público  

Comenzaremos con la creación de un repositorio en GitHub para luego crear un proyecto en RStudio con control de versiones. De esta manera podremos ir registrando todos cambios realizados para crear la página web. En esta parte, asumimos que tenés instalado Git y tenés una cuenta en GitHub. Si no es el caso, podés instalarte Git [desde esta página](https://git-scm.com/downloads) y hacerte una cuenta en Github [aquí](https://github.com/). Si estás realizando tus primeros pasos en Git, en este [nota](https://yabellini.netlify.app/es/post/githubconr/) encontrarás más información que te ayudará a incursionarte en Git.^[Para información mas detallada sobre el uso de Git te sugerimos consultar el libro de Jenny Bryan (en inglés), [_Happy Git and GitHub for UseR_](https://happygitwithr.com/)]

Vamos a comenzar creando un nuevo repositorio público en nuestra cuenta de GitHub, siguiendo los pasos que figuran a continuación.

<img src="/img/repo.png" width="90%"/>

Para ello, no es necesario que el nombre del repositorio sea el nombre del dominio de la página web. Por último, copiamos el URL HTTPS de nuestro repositorio para clonarlo en RStudio.

<img src="/img/repo1.png" width="90%"/>

## En RStudio: nuevo proyecto, la instalación de _blogdown_ y _Hugo_, y la configuración bilingüe.
<br>

Continuamos creando un proyecto con control de versiones utilizando la URL HTTPS del repositorio creado. *File > New Project > Version Control > Git*.

En el proyecto ya creado, proseguimos con la descarga del paquete `blogdown`.

```{r instalación blogdown,eval=FALSE, echo=TRUE}
install.packages(blogdown)
```

Una vez instalado `blogdown`, procedemos con la instalación de _Hugo_, de la siguiente manera:

```{r hugo, eval=FALSE, echo=TRUE}
blogdown::install_hugo()
```

_Hugo_ es el generador de sitios estáticos en el que se basa `blogdown`. En su [página web](https://themes.gohugo.io/) se pueden encontrar una gran variedad de plantillas de sitios web. Por ejemplo, la plantilla **academic** tiene varias utilidades interesantes para páginas webs académicas. 

Ahora vamos a instalar a modo de ejemplo la plantilla **academic**.  En el parámetro `theme` se debe colocar el nombre de la plantilla de hugo elegida  

```{r hugo academic, eval=F, echo=TRUE}
library (blogdown)

blogdown::new_site(theme = "wowchemy/starter-academic", theme_example = TRUE)
```

Luego de esperar pocos minutos para la instalación de todas las carpetas y archivos que conforman la plantilla **academic**, obtendremos la primera versión de nuestro sitio web.

### Personalizando tu sitio web 

Si tenés instalada la última versión de `blogdown`, la plantilla se previsualizará de forma automática en el panel _Viewer_.  En cambio, si tenés una versión anterior, entonces hay que ejecutar las siguiente linea de código para tener un visualización del sitio web localmente.


```{r remedy03, eval=FALSE, echo=TRUE}

blogdown::serve_site()
blogdown::stop_server()# para dejar de visualizar el contenido generado

```

Veremos lo siguiente en _Viewer_ (o en un navegador):

<img src="/img/hugo-academic.png" width="90%"/>

Ya tenemos nuestra página web, ahora lo que queda es reemplazar la información de la página por la nuestra y organizarla según nuestros intereses. A medida que modifiquemos cada archivo vamos a poder visualizar automáticamente los cambios en el _Viewer_ y o en el navegador.

A continuación se muestra los principales archivos y carpetas que constituyen la página web.

```
├── config.toml       
|── config/default
   ├── menus.toml     
   ├── params.toml    
   └── languages.toml
|── content
|── themes
```

En el archivo _**config.toml**_ se encuentran los metadatos de nuestra página. Dentro de este archivo modificaremos el título de la página web y la URL.

Dentro de la carpeta **config/_default** se encuentran tres archivos.toml que definen la configuración de la página web.

+ _**params.toml**_: combinación de colores de la página (_theme_)^[Se pueden elegir otros _themes_  [aquí](https://wowchemy.com/docs/customization/) o si te animás podes crearte el tuyo], tamaño de la letra (_font_size_). En este archivo también se agrega la información de contacto (email, dirección laboral, cuenta de twitter, GitHub, ResearchGate).

+ _**menus.toml**_: opciones del menú de navegación (Notas, Proyectos, Cursos, Publicaciones, etc). Podrás cambiar los nombres o quitar aquellas opciones que no querés que aparezcan.

+ _**languages.toml**_: se define el o los idiomas del sitio web.

En la carpeta _content_ se localiza el contenido de nuesta página web en subcarpetas. Por ejemplo, si se quiere cambiar la información de la biografia, hay que seguir la siguiente ruta _content > authors > admin_ y modificar el archivo _index.md_. Podremos cambiar la foto de la página reemplazando _**avatar.jpg**_ por una foto nuestra.

```
|── content
   ├── authors     
   ├── courses
   ├── home
   ├── post
   ├── project
   └── publication
```

Desde **_content/home_** se podrán activar y editar cada una de las opciones del menú de navegación (widgets) de la página web. Para que se visualice el widget, es necesario que aparezca _active= true_

### Configuración de la página web bilingüe

Para configurar el sitio web en dos idiomas (español e inglés a modo de ejemplo) tenemos que crear dos subcarpetas llamadas _en_ y _es_ dentro de la carpeta _content_. Las nuevas subcarpetas deben tener cada una el contenido que había previamente en la carpeta _content_.^[En el caso de que se elijan otros idiomas, las subcarpetas a crearse deben respetar las siglas según se muestra [aquí](https://www.w3schools.com/tags/ref_language_codes.asp)]

```
|── content
   ├── es     <- Español
   ├── en     <- Inglés
    
```
Luego, en el archivo _**languages.toml**_ descomentar y agregar las siglas del segundo idioma e indicar la carpeta donde está su contenido.


```{r, eval= FALSE, echo=TRUE}

[en]
  languageCode = "en-us"
  contentDir = "content/en"  # Uncomment for multi-lingual sites, and move English content into `en` sub-folder.
  title = "English site"

# Uncomment the lines below to configure your website in a second language.
[es]
 languageCode = "es"
 contentDir = "content/es"
  title = "Sitio en español"

  [es.params]
   description = "Sitio en español"
  [[es.menu.main]]
    name = "es"
    url = "#about"
    weight = 1
```

Además, se deben crear dos nuevos archivos _**menus.es.toml**_ y _**menus.en.toml**_. 

```
|── config/default
   ├── menus.es.toml     <- Español
   ├── menus.en.toml     <- Inglés
   ├── params.toml    
   └── language.toml    
```

Finalmente en _**config.toml**_ debemos elegir el idioma por defecto del sitio web. Por ejemplo si queremos que quede en español _defaultContentLanguage = “es"_

Para visibilizar que la página web es bilingüe, conviene ir a _**params.toml**_ y verificar que en _show_language_ diga TRUE.

<img src="/img/params.png" width="90%"/>

## Publicar tu página web en internet (Deploy)

Una vez que la página web este editada de acuerdo a nuestros intereses, lo que resta es publicarla y compartirla al resto de la comunidad. Te indicamos dos opciones para ello que difieren en el servicio de host que utilizan. En ambos casos, son servicios gratuitos y permiten tener sitios estáticos. En el caso de Netlify, tu página web tendrá el siguiente dominio: _nombreweb.netlify.app_ En el caso de Github Pages: _nombreweb.github.io_

**Netlify** y **GitHub pages** son servicios de host en la nube que nos permite tener un sitio estático de forma gratuita y sencilla. Basicamente, ambos se conecta con el repositorio remoto en GitHub para publicar el sitio en la web.

### Utilizando **Netlify** 

Primero debemos poner una copia del archivo _**netlify.toml**_ localizado en  _theme > starter-academic_ en la carpeta base del proyecto. En dicho archivo debemos especificar la versión utilizada de Hugo. 

```{r, eval=TRUE, echo=TRUE}

blogdown::hugo_version()

```

El archivo _**netlify.toml**_ corregido con la versión de Hugo debería quedar así:

```{r, eval= FALSE, echo=TRUE}

[build.environment]
  HUGO_VERSION = "0.78.1" #Aqui va el número de tu versión de Hugo
  HUGO_ENABLEGITINFO = "true"

```

Además verificamos en el archivo _**config.toml**_ esté especificado el theme utilizado. En nuestro caso es _starter-academic_.

```{r, eval= FALSE, echo=TRUE}

theme = "starter-academic"

```

Ahora sí podemos publicar nuestra página web.
Primero, debemos ingresar a la página de [**Netlify**](https://www.netlify.com/). Cliqueamos en _Sign Up_ y luego en _GitHub_ para conectar **Netlify** con GitHub.

<img src="/img/netlify1.png" width="90%"/>

Luego, elegimos el repositorio remoto donde está la información de la página web mediante la siguiente ruta _New site from Git > GitHub_
Obtendrás algo similar a la siguiente figura pero autocompletado con tu información.

<img src="/img/netlify2.png" width="90%"/>

En opciones avanzadas (_Show advanced_) escribir la versión de Hugo que utilizaste para crear tu sitio web.

<img src="/img/netlify3.png" width="90%"/>

Cliqueamos en _Deploy Site_ y ¡¡¡listo!!! `r emo::ji("party")` Notaremos que **Netlify** asigna aleatoriamente el nombre de la página web. Para cambiarlo tendremos que ir a _Domain Settings > Options > Edit site name_
Podrás editar el contenido de tu página web sin la necesidad de repetir los pasos anteriores ya que **Netlify** al estar vinculado con GitHub lo actualizará automáticamente.

### Utilizando GitHub Pages 

A diferencia de Netlify, este servidor es parte de Github, por lo que no necesitamos conectarnos a una nueva cuenta. Dentro del repositorio remoto debemos ir a _Settings_

<img src="/img/githubpages.png" width="100%"/>

Luego, buscamos la sección de **GitHub Pages** y seleccionamos en la rama (_Branch_) donde se encuentra nuestro contenido web. Tener en cuenta que el dominio de nuestra página web será el nombre del repositorio, el cual puede ser cambiado después de haber sido creado.

<img src="/img/githubpages2.png" width="90%"/>

Para información más detallada te recomendamos visitar la página de [**GitHub Pages**](https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/creating-a-github-pages-site#creating-your-site).

🔊 ¡Ahora solo queda que difundas tu sitio a la comunidad!

## Bonus track

Para agregar una nueva nota dentro de la página web tenemos que ir a _Addins_ y seleccionar _New Post_. Se abrirá una ventana donde podremos completar la información del título, les autores, etiquetas, fecha, categorias y seleccionar la ubicación de la nueva nota.

<img src="/img/post.png" width="90%"/>

### En la ultima versión de `blogdown` 

En el caso de estar trabajando con la última versión de `blogdown`, recomendamos seguir los consejos provistos por [Alison Hill](https://twitter.com/apreshill) en su [presentación para L.A. R Users Group](https://alison.netlify.app/larug-download/#1)  para configurar la versión de Hugo y buenas prácticas para la construcción de una página web.

## Fuentes 

+ [_**blogdown: Creating Websites with R Markdown**_](https://bookdown.org/yihui/blogdown/)  Yihui Xie, Amber Thomas, Alison Presmanes Hill

+ [_**Up & Running with blogdown**_](https://alison.rbind.io/post/2017-06-12-up-and-running-with-blogdown/) Alison Presmanes Hill

+ [_**Blogging in R with Blogdown**_](https://www.youtube.com/watch?v=f6kyYjCVAs0) dictado por Rebecca Barter para RLadies- Bucarest 

+ [_**Becoming an R blogger**_](http://www.rebeccabarter.com/blog/2020-02-03_blogger/) Rebecca Barter

+ [_**wowchemy**_](https://wowchemy.com/docs/get-started/)

+ [_**A Spoonful of Hugo: The netlify.toml File**_](https://alison.rbind.io/post/2019-02-19-hugo-netlify-toml/) Alison Presmanes Hill


