---
title: Evaluación de herramientas digitales e información remota en rotaciones de cultivos extensivos en la región semiárida
author: Yanina Bellini Saibene
summary: "Esta fue una propuesta de vinculacion universidad/centro de investigacion industria a la cual aplicamos INTA Anguil y TECRO.  El proyecto fue gano el subsidio, pero finalmente no fue implementado en gran parte por la pandemia. Me parece que compartir el texto de una propuesta exitosa puede ser de utilidad a otros equipos academia-industria que quieran trabajar juntos."
date: '2024-03-29'
categories:
  - English
  - Open Data
  - Open Science
  - AgTech
  - 100DaysToOffload
tags:
  - Spanish
  - Open Data
  - Open Science
  - AgTech
  - 100DaysToOffload
---

  

### Breve descripción del proyecto

_Describir de qué se trata el proyecto (1 a 3 líneas)._: **Evaluación de herramientas digitales e información remota en rotaciones de cultivos extensivos en la región semiárida**


### Nombre y principales antecedentes de la empresa

_Destacar las experiencias previas en proyectos de investigación, desarrollo e innovación y en la vinculación con el ámbito académico, haciendo especial énfasis en los antecedentes relacionados con el presente proyecto (no más de 15 líneas)._

El equipo de TECRO ha trabajado en la Comisión Nacional de Energía Atómica (CNEA) para la Organización Australiana de Ciencia y Tecnología Nuclear (ANSTO) en el desarrollo de un simulador para el reactor nuclear OPAL, ubicado en las afueras de Sydney, Australia. También tienen experiencia docente universitaria en cátedras en la Facultad de Ingeniería de de la Universidad Nacional de La Pampa. Han colaborado con otros grupos de INTA (AER General Pico) en la realización de vuelos con Drones para el seguimiento de ensayos (determinación de calidad en trigo) y han sido contratados para el desarrollo de software para la Red de Información Agropecuaria Nacional, coordinada por el grupo de AgroTICs de la EEA Anguil.


### Nombre y principales antecedentes del grupo de investigación 

_Destacar las experiencias previas en temas relacionados con el proyecto y en la vinculación con el sector productivo (no más de 15 líneas)._

El equipo interdisciplinario de Ingenieros Agrónomos e Informáticos tiene un promedio de 15 años trabajando en la región semiárida. El grupo de tecnologías de cultivos es responsable de la realización de ensayos de las redes de evaluación de cultivares e híbridos de girasol, maíz, sorgo y trigo llevando adelante la implantación, registro y seguimiento de ensayos de cultivos (fina y gruesa), para aspectos de manejo, sanidad y producción. Estas actividades siempre se realizan en convenio con las empresas y asociaciones de productores correspondientes. El grupo de AgroTICs tiene experiencia en el desarrollo de soluciones digitales aplicadas al agro. En lo relacionado al trabajo con información geo referenciada y de sensores remotos se destacan GeoINTA, modelos de estimación de ocurrencia de granizo y daño en cultivos utilizando datos de radar meteorológico con técnicas de minería de datos, el desarrollo de software para el procesamiento de imágenes de radar, uso de imágenes de radar meteorológico como recurso para la planificación agropecuaria, uso de imágenes satelitales para la evaluación de emergencias agropecuarias, evaluación de productos satelitales de variables de interés agrometeorológico. Muchas de estas actividades se realizan en convenio con la parte privada (Bolsas y Cámaras Arbitrales de Cereales, Compañías de seguros, asociaciones de productores, etc.).


### Breve justificación del proyecto

_Describir el problema o la oportunidad que dio origen al proyecto._

En regiones semiáridas, la disponibilidad de agua y de nitrógeno son los principales factores que afectan la producción de cultivos (Bono et al., 2017; Cossani et al., 2010).  La variabilidad del ambiente edáfico dentro de la región, lleva a identificar zonas homogéneas dentro de un campo para realizar un manejo sitio- específico del cultivo. Con el objetivo de ser más eficientes en el uso del agua, nutrientes y recursos (Khosla et al., 2008). Hay distintas técnicas usadas para identificar zonas de manejo, por ejemplo, a través de la altimetría (Farrell et al., 2018), la materia orgánica, los contenidos de P (Gili et al., 2017) y la profundidad del perfil. 

Los contenidos de clorofila y nitrógeno son importantes indicadores del estado fisiológico de las plantas debido a su importante rol en la fotosíntesis (Carter and Miller, 1994; Lichtenthaler, 2004), posibilitando el desarrollo de estrategias de manejo de N. Identificando las variaciones dentro del sitio, se incrementa la eficiencia en el uso del nitrógeno, reduce el impacto ambiental y mejorar la calidad del producto a lograr (Khosla et al., 2008). Herramientas de sensores remotos, GPS y aplicaciones de tasa variable permiten tomar decisiones durante el ciclo del cultivo. Para ello, es necesario buscar indicadores que posibiliten estimar parámetros biofísicos como área foliar, índice de área foliar y biomasa, y parámetros bioquímicos como contenidos de agua, N en hoja y pigmentos de la hoja a escala local y regional usando sensores aéreos o espaciales (Main et al., 2011; Ramoelo et al., 2015). 

Existen diversos índices de vegetación que pueden utilizarse para cuantificar el estado de un cultivo como: Normalized Difference Vegetation Index, Soil Adjusted Vegetation Index, Atmospherically Resistant Vegetation Index, Enhanced Vegetation Index, Green Chlorophyll Index, Structure Insensitive Pigment Index y Normalized Burn Ratio y existen estudios previos en diversos lugares del mundo y Argentina sobre el uso de estos índices en distintos cultivos. **Sin embargo, en regiones semiáridas, los detectores de reflectancia de las hojas pueden confundir los síntomas de deficiencia con nitrógeno con las deficiencias de agua y no todos los índices han sido calculados y probados en condiciones controladas de campo. Por lo tanto, se propone evaluar diferentes índices, para poder seleccionar aquellos índices o sus combinaciones que permitan diferenciar los distintos tipos de estreses que pueden alterar el normal crecimiento del cultivo en regiones semiáridas.**


### Antecedentes del proyecto

_Indicar si existen antecedentes nacionales e internacionales que permitan sustentar el enfoque o la solución propuesta._

Los índices mencionados han sido utilizados ampliamente con sensores remotos en satélites, algunos de ellos también con cámaras a bordo de drones, abarcando experiencias en el mundo y en Argentina.  La mayoría de las Start Up de AgTech que ofrecen información de imágenes satelitales incorpora el cálculo de muchos de estos índices en sus plataformas y el acceso masivo a Google Earth Engine permite realizar estos cálculos a nivel histórico de manera sencilla y accesible.  Estas plataformas no tienen incorporado imágenes de drones, que cuentan con una resolución espacial de mayor detalle que los satélites disponibles gratuitamente. Sobre trabajos más regionales, situados en la provincia de La Pampa podemos mencionar (Farrell, M. et al, 2018) que analiza 4 índices para un cultivo de maíz al norte provincial (zona no semiárida) y encuentra buenos resultados para detectar diferencias en la humedad del suelo y la fertilidad. Además, tanto (NIR /VERDE) -1 y el NDVI verde tuvieron la mejor correlación con el rendimiento del cultivo.  No se cuenta con información sobre ensayos de la región de estudio (EEA Anguil, Ruta Nacional Nº 5, Km 580).

### Financiamiento público o privado obtenido para etapas preliminares del proyecto

_Indicar si los participantes han obtenido financiamiento público o privado para etapas preliminares del proyecto o directamente vinculadas al mismo y, en caso afirmativo, mencionar cuáles fueron las fuentes de financiamiento._

No hemos recibido porque se inicia con este proyecto.  Durante la realización del mismo los sueldos y estipendio de beca del personal del equipo de trabajo investigador provienen de INTA y CONICET (beca doctoral)

###  Objetivos generales y específicos del proyecto

_Tener en cuenta que los objetivos específicos deben estar insertos en los generales, y que son los objetivos específicos los que se espera lograr llevando a cabo las actividades en las distintas etapas a describir en el punto siguiente._

1) determinar índices sensibles al estado nutricional e hídrico en distintos estados fenológicos de cultivos:

  1.1. Implantación de los ensayos de cultivos de gruesa en dos ambientes en la EEA Anguil.

  1.2. Vuelos con drone durante fechas críticas y de probable utilidad para la toma de decisión para el manejo del cultivo y a diferentes alturas.

  1.3. Registro a campo de las variables de interés.

  1.4. Descarga de información satelital en el mismo momento que los vuelos.

  1.5. Procesamiento de las imágenes en diferentes índices.

  1.6. Correlación de los índices con las variables registradas a campo.

2) Poder utilizar, a través de índices, estrategias de manejo que permitan aumentar la eficiencia del uso de recursos, agua y nutrientes.

  2.1. Determinar la utilidad de cada índice calculado.

  2.2. Determinar las mejores fechas y alturas para los vuelos.

  2.3. Generación de una primer versión de una guía de uso de índices espectrales para cultivos de cosecha gruesa en zonas semiáridas

  

### Descripción de las etapas y plan de trabajo del proyecto

3.  

Para cada etapa: a) describirla técnicamente; b) hacer referencia a los objetivos específicos que la originan; c) enumerar las principales actividades que la componen; d) indicar cuál es la participación de la empresa y del grupo de investigación en cada una de las actividades; e) mencionar cuáles son los recursos ya disponibles que se utilizarán; f) describir cuáles son los respectivos hitos o entregables. Incluir también un diagrama de Gantt de las etapas del proyecto, indicando las posibles interdependencias.

El pro yecto contempla siete etapas que se detallan en la tabla 1 y el diagrama de gantt correspondiente.  La **Etapa 1.a** permite realizar la implnatación de los ensayos en la EEA Anguil sobre los cuales se realizarán los vuelos y toma de datos correspondientes.  Corresponden a dos ambientes semiáridos.  

La **Etapa 1.b.** permite generar el entorno de procesamiento de las imágenes con los indices de interés para el estudio.

Las **etapas 2 a 6** corresponden al registro de datos a campo y vuelos correspondientes a estados fenológicos claves en el desarrollo del cultivo: vegetativo, prefloración, floración, posfloración y madurez.  Estas 5 fechas de registro de datos con drone y a campo proveerá las herramientas para analizar cada índice en cada fecha, para analizar su utilidad y posibilidad de uso para decisciones de manejo posteriores.

La **etapa 7** permite analizar todas las fechas e indices para poder generar una guia de recomendación y el informe de resultados final. 

Tabla 1. Etapas y actividades principales

|     |                                                                                       |     |                  |     |               |     |
|-----|---------------------------------------------------------------------------------------|-----|------------------|-----|---------------|-----|
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       **Actividades**                                                                        |     |                  
                                                                                                     **Fecha Inicio**  |     |               
                                                                                                                              **Fecha fín**  |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       **Implantación de ensayos**                                                            |     |                  
                                                                                                     **Etapa 1.a**     |     |               |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Preparación barbecho                                                                   |     |                  
                                                                                                     28-nov            |     |               
                                                                                                                              05-dic         |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Determinación de cobertura y residuos                                                  |     |                  
                                                                                                     06-dic            |     |               
                                                                                                                              10-dic         |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Siembra                                                                                |     |                  
                                                                                                     10-dic            |     |               
                                                                                                                              12-dic         |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Fertilización                                                                          |     |                  
                                                                                                     20-dic            |     |               
                                                                                                                              22-dic-19      |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       **Desarrollo cálculos índices**                                                        |     |                  
                                                                                                     **Estapa 1.b**    |     |               |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Relevar paquetes de R y librerías de Python que calculan los índices                   |     |                  
                                                                                                     28-nov            |     |               
                                                                                                                              05-dic         |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Desarrollar el cálculo de aquellos índices que no se encuentren disponibles            |     |                  
                                                                                                     06-dic            |     |               
                                                                                                                              10-dic         |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Generar un pipeline automatizado de trabajo para el cálculo de los índices de interés  |     |                  
                                                                                                     05-dic            |     |               
                                                                                                                              22-dic-19      |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       **Registro de datos a campo - Primera fecha**                                          |     |                  
                                                                                                     **Etapa 2**       |     |               |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Primer corte biomasa: estado vegetativo                                                |     |                  
                                                                                                     15-ene            |     |               
                                                                                                                              20-ene         |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Toma de imagen por Drone                                                               |     |                  
                                                                                                     15-ene            |     |               
                                                                                                                              20-ene         |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Interpretación y análisis de imágenes                                                  |     |                  
                                                                                                     20-ene-20         |     |               
                                                                                                                              20-feb-20      |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Control de malezas                                                                     |     |                  
                                                                                                     18-ene-20         |     |               
                                                                                                                              20-ene-20      |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       **Registro de datos a campo - Segunda fecha**                                          |     |                  
                                                                                                     **Etapa 3**       |     |               |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Segundo corte biomasa: pre floración                                                   |     |                  
                                                                                                     10-feb-20         |     |               
                                                                                                                              15-feb-20      |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Toma de imagen por Drone                                                               |     |                  
                                                                                                     10-feb-20         |     |               
                                                                                                                              15-feb-20      |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Interpretación y análisis de imágenes                                                  |     |                  
                                                                                                     15-feb-20         |     |               
                                                                                                                              15-mar-20      |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       **Registro de datos a campo - Tercera fecha**                                          |     |                  
                                                                                                     **Etapa 4**       |     |               |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Tercer corte biomasa: floración                                                        |     |                  
                                                                                                     15-mar-20         |     |               
                                                                                                                              20-mar-20      |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Toma de imagen por Drone                                                               |     |                  
                                                                                                     15-mar-20         |     |               
                                                                                                                              20-mar-20      |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Interpretación y análisis de imágenes                                                  |     |                  
                                                                                                     20-mar-20         |     |               
                                                                                                                              02-abr-20      |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Medición de Radiación                                                                  |     |                  
                                                                                                     16-mar-20         |     |               
                                                                                                                              18-mar-20      |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Spad                                                                                   |     |                  
                                                                                                     16-mar-20         |     |               
                                                                                                                              18-mar-20      |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       **Registro de datos a campo - Cuarta fecha**                                           |     |                  
                                                                                                     **Etapa 5**       |     |               |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Cuarto Corte de Biomasa: posfloración                                                  |     |                  
                                                                                                     01-abr-20         |     |               
                                                                                                                              05-abr-20      |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Toma de imagen por Drone                                                               |     |                  
                                                                                                     01-abr-20         |     |               
                                                                                                                              05-abr-20      |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Interpretación y análisis de imágenes                                                  |     |                  
                                                                                                     05-abr-20         |     |               
                                                                                                                              05-may-20      |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       **Registro de datos a campo - Quinta fecha**                                           |     |                  
                                                                                                     **Etapa 6**       |     |               |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Quinto Corte de biomasa: Madurez                                                       |     |                  
                                                                                                     25-abr-20         |     |               
                                                                                                                              30-abr-20      |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Toma de imagen por Drone                                                               |     |                  
                                                                                                     25-abr-20         |     |               
                                                                                                                              30-abr-20      |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Interpretación y análisis de imágenes                                                  |     |                  
                                                                                                     30-abr-20         |     |               
                                                                                                                              30-may-20      |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Estimación de componentes de rendimiento                                               |     |                  
                                                                                                     30-abr-20         |     |               
                                                                                                                              15-may-20      |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       **Elaboración final**                                                                  |     |                  
                                                                                                     **Etapa 7**       |     |               |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Correlación entre imágenes y datos de campo                                            |     |                  
                                                                                                     15-may-20         |     |               
                                                                                                                              30-jun-20      |     |
|     |                                                                                       |     |                  |     |               |     |
|     |                                                                                       
       Elavoración de Indice y resultados                                                     |     |                  
                                                                                                     15-may-20         |     |               
                                                                                                                              30-jun-20      |     |
|     |                                                                                       |     |                  |     |               |     |

1.  

2.  Presupuesto

3.  

Describir y justificar el presupuesto solicitado por rubro. Para gastos en los rubros "Maquinarias y equipos", "Materiales e insumos" y "Otros", cuando un ítem a comprar o contratar iguale o supere el monto de \$40.000, y para gastos en el rubro "Servicios de terceros" que superen el monto de \$20.000, deberá adjuntarse un presupuesto de dicho ítem.

Nota: este presupuesto establecerá los montos máximos solicitados por rubro, los que podrán ser modificados en el proceso de evaluación. 

|     |                          |     |                 |     |
|-----|--------------------------|-----|-----------------|-----|
|     |                          |     |                 |     |
|     |                          
       **Rubro**                 |     |                 
                                        **Monto en \$**  |     |
|     |                          |     |                 |     |
|     |                          
       Materiales e insumos      |     |                 
                                        40.000           |     |
|     |                          |     |                 |     |
|     |                          
       Servicios de terceros     |     |                 
                                        20.000           |     |
|     |                          |     |                 |     |
|     |                          
       Maquinarias y equipos     |     |                 
                                        40.000           |     |
|     |                          |     |                 |     |
|     |                          
       Viajes y viáticos         |     |                 
                                        60.000           |     |
|     |                          |     |                 |     |
|     |                          
       Gastos de administración  |     |                 
                                        32.000           |     |
|     |                          |     |                 |     |
|     |                          
       Otros                     |     |                 
                                        20.000           |     |
|     |                          |     |                 |     |
|     |                          
       **TOTAL**                 |     |                 
                                        212.000          |     |
|     |                          |     |                 |     |

1.  

2.  Cronograma de desembolsos

3.  

Describir y justificar el cronograma de los desembolsos previstos. Nota: el financiamiento se efectivizará bajo la modalidad de reembolso de pago hecho, salvo en casos excepcionales --debidamente justificados- en los que se apruebe el pago de anticipos.

|     |            |     |                 |     |                                                            |     |
|-----|------------|-----|-----------------|-----|------------------------------------------------------------|-----|
|     |            |     |                 |     |                                                            |     |
|     |            
       **Etapa**   |     |                 
                          **Monto en \$**  |     |                                                            
                                                  **Entregable**                                              |     |
|     |            |     |                 |     |                                                            |     |
|     |            
       Etapa 1.a   |     |                 
                          72.000           |     |                                                            
                                                  Ensayos implantados.  Informe fotográfico correspondiente.  |     |
|     |            |     |                 |     |                                                            |     |
|     |            
       Etapa 1.b.  |     |                 
                          20.000           |     |                                                            
                                                  Código fuente en respositorio Git                           |     |
|     |            |     |                 |     |                                                            |     |
|     |            
       Etapa 2     |     |                 
                          20.000           |     |                                                            
                                                  Repositorio con planillas con datos de campo                
                                                  Imágenes de vuelos                                          
                                                  Informe de imágenes procesadas                              |     |
|     |            |     |                 |     |                                                            |     |
|     |            
       Etapa 3     |     |                 
                          20.000           |     |                                                            
                                                  Repositorio con planillas con datos de campo                
                                                  Imágenes de vuelos                                          
                                                  Informe de imágenes procesadas                              |     |
|     |            |     |                 |     |                                                            |     |
|     |            
       Etapa 4     |     |                 
                          20.000           |     |                                                            
                                                  Repositorio con planillas con datos de campo                
                                                  Imágenes de vuelos                                          
                                                  Informe de imágenes procesadas                              |     |
|     |            |     |                 |     |                                                            |     |
|     |            
       Etapa 5     |     |                 
                          20.000           |     |                                                            
                                                  Repositorio con planillas con datos de campo                
                                                  Imágenes de vuelos                                          
                                                  Informe de imágenes procesadas                              |     |
|     |            |     |                 |     |                                                            |     |
|     |            
       Etapa 6     |     |                 
                          20.000           |     |                                                            
                                                  Repositorio con planillas con datos de campo                
                                                  Imágenes de vuelos                                          
                                                  Informe de imágenes procesadas                              |     |
|     |            |     |                 |     |                                                            |     |
|     |            
       Etapa 7     |     |                 
                          20.000           |     |                                                            
                                                  Repositorio con planillas con datos de campo                
                                                  Imágenes de vuelos                                          
                                                  Informe de imágenes procesadas                              |     |
|     |            |     |                 |     |                                                            |     |

1.  

2.  Beneficios de las partes

3.  

Describir el grado de desafío tecnológico que el proyecto representa para la empresa, así como el grado en que los resultados del proyecto beneficiarán al grupo de investigación participante.

Tecro tiene experiencia en la elaboración de aplicaciones que condensan información georeferenciada sumada a la experiencia en la adquisición de dicha información mediante el uso de dispositivos UAV.  Dentro de su servicio de Drones se ofrece: AGRICULTURA DE PRECISIÓN (NVDI), EVALUACIÓN DE DAÑOS (INCENDIOS, GRANIZO, INUNDACIONES), SEGURIDAD Y MONITOREO, MAPEO Y RELEVAMIENTO, IMÁGEN Y VIDEOS AÉREOS, BÚSQUEDA Y RESCATE además del desarrollo de sistemas de información geográfica para aplicaciones de escritorio o web según las necesidades de los clientes.  Las pruebas a campo y la validación de diferentes índices orientados a la agricultura permitirá a la empresa ampliar el abanico de servicios en la temática de AGRICULTURA DE PRECISIÓN, agregándole valor con la mirada agropecuaria de cada índice ajustado a la zona de estudio.  También será de utilidad el intercambio con el INTA sobre posibles herramientas para el procesamiento de las imágenes.

Para el equipo de investigación permitirá avanzar en una temática de alta demanda del medio, conocer las posibilidades reales de un monitoreo con drone sobre cultivos de gruesa extensivos en la región, ganar capacidad en herramientas (equipamiento y software) para el procesamiento de este tipo de información y contar con una transferencia de los resultados de la investigación.

1.  

2.  Planes de adopción de los resultados del proyecto por parte de la empresa participante

3.  

Describir cuáles serán las fases subsiguientes de este desarrollo hasta la obtención del nuevo o mejorado producto o servicio y su puesta en el mercado. Indicar brevemente cómo se integra este proyecto a la estrategia comercial de la empresa.

El objetivo de la participación de la empresa en el proyecto es la posibilidad de analizar diferentes técnicas de trabajo optimizando el proceso de captura de imágenes y pos proceso orientado a la actividad y fin específico.

Se analizarán distintas resoluciones de imágenes y alturas de vuelo con el fin de optimizar costos, tiempo de captura y pos proceso sin perder calidad ni información en el producto final.

También nos ayudara a determinar los distintos periodos de captura de imágenes según los tiempos del cultivo.

En el proceso de captura de imágenes se utilizará:

Drone tipo multicoptero modelo DJI INSPIRE 2.

Camara Multiespectral Parrot Sequoia.

Camara RGB Zenmuse X4S.

En cuanto al pos proceso el proyecto nos ayudara a definir los distintos formatos de entregas del producto final según las necesidades del análisis a realizar en cada etapa.

De la realización del proyecto se provee proporcionar un servicio definido de adquisición de datos de calidad destinado a profesionales agronómicos.
