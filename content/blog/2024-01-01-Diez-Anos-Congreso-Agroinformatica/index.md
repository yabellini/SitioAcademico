---
date: "2024-01-01"
title: "Diez Años del Congreso Argentino de Agroinformática: Un Análisis Histórico del Alcance Geográfico y Redes de Colaboración"
authors: "Sandro da Silva Camargo, Leonardo Bidese de Pinho, Marcelo Horacio Bosch, Claudio Machado, Yanina Bellini Saibene"
summary: "Este trabajo relata un proceso para identificar y analizar la red de colaboración entre instituciones en el ámbito de la investigación en agroinformática en Argentina, destacando la relevancia del INTA y del CONICET como catalizadores de la investigación en esta área."
---

## Resumen

Para permitir el intercambio de competencias y recursos, la colaboración en investigación se ha tornado fundamental para el progreso científico. Este trabajo relata un proceso para identificar y analizar la red de colaboración entre instituciones en el ámbito de la investigación en agroinformática en Argentina, a partir de los trabajos publicados en los anales de las diez ediciones del Congreso Argentino de Agroinformática, así como reconocer el alcance geográfico del evento. La metodología se basó en la aplicación de técnicas de Análisis de Redes Sociales, que permitieron identificar las instituciones más participativas en el contexto de la Agroinformática en Argentina. Fueron analizados 270 trabajos con 1112 autorias de 702 autores distintos. Los resultados enfatizan la relevancia del Instituto Nacional de Tecnología Agropecuaria (INTA) y del Consejo Nacional de Investigaciones Científicas y Técnicas (CONICET) como catalizadores de la investigación en esta área. Se espera que los resultados aquí presentados aporten elementos para ayudar a los organismos gubernamentales a establecer políticas para fortalecimiento de la investigación y desarrollo de la Agroinformática Argentina.

## Palabras Clave

Colaboración Científica, Asociación Científica, Colaboración Tecnológica, Asociación Tecnológica.

## Introducción

La colaboración en investigación se ha convertido en una actividad fundamental para el progreso de la ciencia por mejorar la comunicación entre grupos de investigadores, por permitir el intercambio de experiencias y competencias y por facilitar la producción y diseminación de nuevos conocimientos científicos. La forma más evidente de colaboración es la coautoría en publicaciones, que son un poderoso instrumento para el análisis de colaboraciones y asociaciones científicas y tecnológicas, haciendo posible obtener la comprensión de los patrones de cooperación entre individuos y organizaciones.

## Materiales y Métodos

### Fuente de Datos

El presente trabajo utilizó como base los trabajos publicados en los Anales de todas ediciones del CAI y también los datos informados por los autores en el sistema de envío de trabajos. La base de Datos contenía los siguientes campos: Nombre de la Persona, Rol (típicamente autor), ID de la Persona en el Paper, Tipo de Presentacion (Exposicion Oral, Full Paper, Extended Abstract, Poster o Comunicacion Oral), Año de la Edición, Id del Paper, Genero de la Persona (Hombre o Mujer), Institución, Dependencia de la Institución, Ciudad, Provincia y País. Además, los anales de la 3a hasta la 10a ediciones están disponibles en los sitios de los eventos.

### Visualización Georreferenciada

Para la visualización interactiva de datos georeferenciados se utilizó la API (Application Programming Interface) Google Charts, que es un servicio gratuito ofrecido por Google. Para esta visualización, fueron utilizados los campos Ciudad, Provincia y País.

### Redes de Colaboración

Para la representación de las colaboraciones en forma de una red social, se utilizó la herramienta Gephi 0.9.1, que es una herramienta gratuita y de código abierto para la creación, análisis y explotación de redes complejas. La aplicabilidad de las Redes Sociales para análisis de colaboración en una red de investigación se debe al hecho de que las redes son una metáfora ampliamente utilizada para representar los miembros de una comunidad y sus ligaciones.

## Resultados y Discusión

Se realizó un análisis sobre los países de las instituciones de todos los autores de cada trabajo, a fin de visualizar el alcance geográfico del evento. La Figura 1 muestra los países de las instituciones que ya publicaron trabajos en el CAI. La cantidad de autorias de cada país se muestra en la Tabla 1. Se puede ver que instituciones de diversos países de América del Sur ya publicaron en el CAI y, eventualmente, algunas instituciones de otros continentes. En la última edición, hay un porcentaje importante de trabajos de Brasil y Estados Unidos.

Como cerca de 87% de las autorias procede de la Argentina, se realizó un análisis específico sobre las provincias y ciudades de las instituciones de los autores de este país. La Tabla 2 presenta las cantidades de autorias por provincia. Así se identifica una gran concentración en el desarrollo de trabajos publicados con autores de las provincias de Buenos Aires, Córdoba, Santa Fe y La Pampa, que tuvieron trabajos publicados en todas las ediciones del evento. La Figura 3a presenta un boxplot de la distribución, por provincia, de los autores de los trabajos. Bajo un análisis estadístico, la cantidad de autores de estas provincias son consideradas como valores atípicos superiores, o sea, numéricamente distante del resto de los datos.

Otras 14 provincias tuvieron trabajos publicados en algunas ediciones del CAI, como puede ser analizado en la Tabla 2. De los 971 autores de instituciones argentinas, 21 no declararon su provincia en el momento del envío del trabajo. Las provincias de Formosa, La Rioja, Salta, Santa Cruz y Tierra del Fuego no tuvieron trabajos publicados en la historia del CAI.

Bajo una perspectiva más detallada, se analizaron las ciudades de los autores, según el resultado presentado en la Figura 2. Se encontraron autores en 57 ciudades argentinas distintas. La Figura 3b presenta un boxplot de la distribución de las ciudades de las instituciones de los autores de los trabajos. Las ciudades cuya frecuencia de autorias son consideradas outliers son: Córdoba (145 autorias), Santa Fe (118), Anguil (95), Buenos Aires (71), Castelar(59) y San Juan (49).

## Conclusiones

El análisis de las redes de colaboración científica en el ámbito de la agroinformática en Argentina muestra un crecimiento significativo en la participación de instituciones y autores a lo largo de las diez ediciones del CAI. La relevancia del INTA y del CONICET como catalizadores de la investigación en esta área es evidente, lo que refleja la importancia de estas instituciones en el desarrollo de la agroinformática en el país. Además, el análisis geográfico del evento revela una concentración de trabajos en la región de la Pampa Húmeda, lo que sugiere la necesidad de expandir el alcance del congreso a otras regiones del país para fomentar una mayor diversidad en la investigación y desarrollo en agroinformática en Argentina.
