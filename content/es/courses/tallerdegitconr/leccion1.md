---
title: Lección 1 - Conceptos básicos de Git
linktitle: Lección 1 - Conceptos básicos de Git
toc: true
type: docs
date: "2020-01-05T00:00:00+01:00"
draft: false
menu:
  tallerdegitconr:
    name: Lección 1 - Conceptos básicos de Git
    weight: 4

# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 4
---


## Lección 1 - Conceptos básicos de Git

### Primer paso: ¿Qué es versionar código?

* El versionado almacena todas las modificaciones realizadas en el código.
* Permite acceder a versiones anteriores de cualquier archivo.
* Garantiza el trabajo en equipo de manera eficiente.
* Acciones útiles: regresar a una versión anterior de tu proyecto, comparar cambios, ver quien realizó y para que una modificación, recuperar archivos perdidos…. Y MUCHO MAS ! 


### ¿Cómo empezamos?

Opciones:

* Creamos un repositorio local y luego lo publicamos en el servidor remoto
* Creamos el repositorio en el servidor remoto y luego lo descargamos en nuestro directorio local.
* Bajamos un repositorio existente desde el servidor remoto, mediante el comando :  `git clone <remote>`

### Comandos básicos: 

#### Add

**Sinopsis :** `git add`

**Descripción:**
Agrega el archivo o directorio al Staging Area.

**Opciones:**

``` 
git add <file-path>
git add -all
git add -u
git add .

```

#### Commit

**Sinopsis:** `git commit` 

**Descripción:**  
Agrega/guarda los cambios al repositorio local.

**Opciones:** 

``` 
git commit -m “Primer commit”
git commit -am “Primer commit”
git revert “hash_commit”

```  
#### Pull

**Sinopsis:** `git pull`

**Descripción:** 
Actualiza el repositorio local con el repositorio remoto.

 **Opciones:** 
```
  git pull <remote>

```


