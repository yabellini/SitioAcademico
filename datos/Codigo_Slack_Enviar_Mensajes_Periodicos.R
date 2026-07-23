library(httr2)
library(tidyverse)
library(keyring)

token <- key_get("slack")

respuesta <- request("https://slack.com/api/conversations.list") |>
  req_url_query(
    exclude_archived = "true",
    limit            = 200        # máximo permitido por Slack
  ) |>
  req_headers(Authorization = paste("Bearer", token)) |>
  req_perform() |>
  resp_body_json()

# Convertir a data frame
canales <- respuesta$channels |>
  map_df(~ tibble(
    id          = .x$id,
    nombre      = .x$name,
    tipo        = if_else(.x$is_private, "privado", "publico"),
    descripcion = .x$purpose$value,   # <-- nuevo
    topic       = .x$topic$value      # <-- nuevo
  ))


glimpse(canales)

canales_finales <- canales |>
  # Keep only public channels
  filter(tipo == "publico") |>
  # Exclude #general (this is the channel where messages will be posted)
  filter(nombre != "general") |>
  # Exclude channels without a description (no useful information to share)
  filter(!is.na(descripcion) & descripcion != "") |>
  # Clean up descriptions: remove internal Slack references (<#...>) and long URLs
  mutate(
    Description = str_remove_all(descripcion, "<#[^>]+\\|?[^>]*>"),
                                   descripcion = str_remove_all(descripcion, "<https?://[^>]+>"),
                                 descripcion = str_squish (descripcion)
    ) |>
      select(nombre, descripcion) |>
      # Sort alphabetically to post in a consistent order
      arrange(nombre)
    

head(canales_finales)    
    

canales <- canales |>
  filter(tipo == "public") |>
  # Excluir #general (es el canal donde se van a postear los mensajes)
  filter(nombre != "general") |>
  # Excluir canales sin descripción (no hay info útil que compartir)
  filter(!is.na(Description) & Description != "") |>
  # Limpiar descripciones: quitar referencias internas de Slack (<#...>) y URLs largas
  mutate(
    Description = str_remove_all(Description, "<#[^>]+\\|?[^>]*>"),
    Description = str_remove_all(Description, "<https?://[^>]+>"),
    Description = str_squish(Description)
  ) |>
  select(Name, Description) |>
  # Ordenar alfabéticamente para postear en orden consistente
  arrange(Name)


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

glimpse(mensajes)

proximo_lunes <- today() + days(7)

mensajes_programados <- mensajes |>
  mutate(
    semana   = row_number() - 1,
    fecha_envio = proximo_lunes + weeks(semana)
  )

head(mensajes_programados)


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