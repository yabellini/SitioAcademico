---
title: "Schedulling messages in Slack using promoutils"
author: Yanina Bellini Saibene
summary: "How we schedulle weekly messages on the rOpenSci Slack to reminder our members about the Slack channels availables for them"
date: '2026-06-18'
categories:
  - English
  - Open Science
  - RStats
tags:
  - English
  - Open Science
  - RStats
---

Slack is one of the apps where online communities communicate.  Interactions are organized into topic-based _channels_. You can choose which channels to join so you can follow the conversations taking place in each one of those channels.  

Finding out which channels are available and joining the ones that are useful to you is one way to make the most of these workspaces. 

The list of channels changes over time, and by default when you join, you’ll only be part of a set of standard ones, such as the #general channel.  Also, if you’re not a member of a channel, by default, you won’t see it in the general list.

For this reason, we thought it would be helpful to remind our Slack members once a week about the channels exist and what they can be used for, while also inviting them to join the channels and participate in the conversations.  

## The full process

The idea is to:

1. get the list of public and active channels in the rOpenSci workspace, their name, description and topics,

2. generate one message for each channel

3. schedulle one message per week to publish on the general channel 

### Step 1: get the list of channel

Slack has an API that allow you to access information, like the list of channels in a workspace. 

You will need an API token for this step. [You can get one following Slack instructions](https://docs.slack.dev/apis/web-api/#authentication).

Once you have your token, store it securely with the package [keyring](https://cran.r-project.org/web/packages/keyring/index.html). You can use the function `key_set("Slack")`, and then paste the token in the popup window. You will access that token with `key_get("Slack")`

After you have your token ready to use, we can make a call to the API and get the list of active (non archived) channels:

``` r
library(httr2)
library(tidyverse)
library(keyring)

token <- key_get("slack")

respuesta<- request("https://slack.com/api/conversations.list") |>
  req_url_query(
    exclude_archived = "true",
    limit            = 200        # max allow by Slack
  ) |>
  req_headers(Authorization = paste("Bearer", token)) |>
  req_perform() |>
  resp_body_json()

```

> Note: I learned about the `slackr` package after I write this code. I need to explore if the package have a function to get the list of active channels. 

The `respuesta` object has a JSON with the list of non archived channels in rOpenSci workspace. Now we need to create a data frame with the useful information: id, name, description, topic and type (public or private).

``` r
canales <- respuesta$channels |>
  map_df(~ tibble(
    id          = .x$id,
    nombre      = .x$name,
    tipo        = if_else(.x$is_private, "privado", "publico"),
    descripcion = .x$purpose$value,   
    topic       = .x$topic$value      
  ))
  
> glimpse(canales)
Rows: 42
Columns: 5
$ id          <chr> "C026GALFB", "C026GCWKA", "C026GCWKC", "C027G1V0W", "C02K0…
$ nombre      <chr> "package-development", "general", "random", "docs", "build…
$ tipo        <chr> "público", "público", "público", "público", "público", "pú…
$ descripcion <chr> "Automated notifications from GitHub commits, issues, &amp…
$ topic       <chr> "Automated notifications from GitHub commits, issues, &amp…  
```

Now `canales` has a list of channels. We need to keep only public ones:

``` r
canales <- canales |>
  # Keep only public channels
  filter(tipo == "público")
``` 

### Step 2: generate one message for each channel

Now that we have all the channels we want to advertise in our Slack, we can generate a message for each one.

We clean the data to remove the `general` channel, because is the channel we will post all the messages, and exclude the channels without description, because we will use that information to explain what is the channel about. Finally we will clean the description from data that can break our message format (like internal Slack references and long URLs) and sort the channels alphabetically to post in a consistent order.

``` r
canales_finales <- canales |>
  filter(nombre != "general") |>
  filter(!is.na(descripcion) & descripcion != "") |>
  mutate(
    description = str_remove_all(descripcion, "<#[^>]+\\|?[^>]*>"),
    descripcion = str_remove_all(descripcion, "<https?://[^>]+>"),
    descripcion = str_squish (descripcion)
    ) |>
      select(nombre, descripcion) |>
      arrange(nombre)
      
> head(canales_finales)    
# A tibble: 6 × 2
  nombre    descripcion                                                         
  <chr>     <chr>                                                               
1 allcaps   ONLY ALL CAPS IN THIS ROOM. NO LOWER CASE                           
2 antarctic The <#C7UBC64Q4> channel is for friendly discussions about using R …
3 arrow     Discussion and support for Apache Arrow and the Arrow R package. Sh…
4 books     What you’re reading right now (or want to read next!)               
5 builds    Automated messages from Travis-CI and Appveyor, for daily builds an…
6 ci        CI related discussions        
```

Now, we need a varied opening phrases to avoid repetitive messages and then iterate trough the list of channels: 

``` r
aperturas <- c(
  "Did you know we have a channel for",
  "This week we'd like to highlight",
  "A reminder that we have a channel for",
  "Have you checked out",
  "Spotlight of the week:"
)

mensajes <- canales_finales |>
  mutate(
    apertura = sample(aperturas, n(), replace = TRUE),
    mensaje = str_glue(
      "{apertura} *#{nombre}*! :slack:\n\n",
      "_{descripcion}_\n\n",
      "Join the conversation and feel free to participate. "
    )
  ) |>
  select(nombre, mensaje)
```

The dataset `mensajes` now have the intro text for each channel we want to share in the Slack. 

``` r

> head(mensajes)
# A tibble: 6 × 2
  nombre    mensaje                                                           
  <chr>     <glue>                                                            
1 allcaps   Spotlight of the week: *#allcaps*! :slack:

_ONLY ALL CAPS IN THIS …
2 antarctic This week we'd like to highlight *#antarctic*! :slack:

_The <#C7UB…
3 arrow     Spotlight of the week: *#arrow*! :slack:

_Discussion and support f…
4 books     A reminder that we have a channel for *#books*! :slack:

_What you’…
5 builds    Have you checked out *#builds*! :slack:

_Automated messages from T…
6 ci        Spotlight of the week: *#ci*! :slack:

_CI related discussions_

Jo… 

```

### Step 3: schedulle one message per week

We need to add the date for each message. We used the `lubridate` package to calculate the _next monday_ as the date for publication for all messages: 

``` r
proximo_lunes <- today() + days(7)

mensajes_programados <- mensajes |>
  mutate(
    semana   = row_number() - 1,
    fecha_envio = proximo_lunes + weeks(semana)
  )

> glimpse(mensajes_programados)
Rows: 39
Columns: 4
$ nombre      <chr> "allcaps", "antarctic", "arrow", "books", "builds", "ci", …
$ mensaje     <glue> "Spotlight of the week: *#allcaps*! :slack:\n\n_ONLY ALL …
$ semana      <dbl> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, …
$ fecha_envio <date> 2026-07-29, 2026-08-05, 2026-08-12, 2026-08-19, 2026-08-2…
```

Now we can schedule the messages using the `slack_posts_write` function from `promoutils`. The `dry_run = TRUE` arguments simulate the scheduling of the message without a real publication.  It is a good idea to check everything works before to do the real scheduling. 

We use the promoutils' function with the `pwalk` function from the `purrr` package to iterate on all the messages:  

``` r
purrr::pwalk(
  list(
    body = mensajes_programados$mensaje,
    when = mensajes_programados$fecha_envio
  ),
  function(body, when) {
    slack_posts_write(
      body     = body,
      when     = when,
      channel  = "#general",
      dry_run  = TRUE  
    )
  }
)
```

The Slack API has a limit on how many days in the future you can schedule messages, so you can reach a limit in the number of messages that can be scheduled. You can use something like this code to register which rows were posted, to be able to continue scheduling messages without repetition. 

``` r
mensajes_programados <- mensajes_programados |>
  mutate(estado = if_else(row_number() <= 17, "Publicado", "Pendiente"))
```

