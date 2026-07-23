library(httr2)
library(tidyverse)
library(keyring)

token <- key_get("slack")

# Función para obtener una página de canales
obtener_pagina <- function(cursor = NULL) {
  req <- request("https://slack.com/api/conversations.list") |>
    req_url_query(
      exclude_archived = "true",
      limit            = 200        # máximo permitido por Slack
    ) |>
    req_headers(Authorization = paste("Bearer", token))
  
  # Agregar cursor solo si existe
  if (!is.null(cursor)) {
    req <- req |> req_url_query(cursor = cursor)
  }
  
  req |> req_perform() |> resp_body_json()
}

# Iterar hasta que no haya más páginas
todas_las_paginas <- list()
cursor <- NULL

repeat {
  respuesta         <- obtener_pagina(cursor)
  todas_las_paginas <- c(todas_las_paginas, respuesta$channels)
  
  cursor <- respuesta$response_metadata$next_cursor
  
  # Si el cursor viene vacío, ya no hay más páginas
  if (is.null(cursor) || cursor == "") break
}

# Convertir a data frame
canales <- todas_las_paginas |>
  map_df(~ tibble(
    id          = .x$id,
    nombre      = .x$name,
    tipo        = if_else(.x$is_private, "privado", "público"),
    estado      = if_else(.x$is_archived, "archivado", "activo"),
    descripcion = .x$purpose$value,
    topic       = .x$topic$value
  ))

glimpse(canales)