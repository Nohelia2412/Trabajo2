import streamlit as st

st.write("""### Marco Teórico """)

st.write("""### ¿Que es el análisis de Correlación? """)

st.write("""El análisis de correlación es el primer paso para construir modelos explicativos y predictivos más complejos. """)

st.write(""" A menudo nos interesa observar y medir la relación entre 2 variables numéricas mediante el análisis de correlación. Se trata de una de las técnicas más habituales en análisis de datos y el primer paso necesario antes de construir cualquier <modelo explicativo o predictivo más complejo Para poder tener el  Datset hay que recolectar información a travez de encuentas. A menudo nos interesa observar y medir la relación entre 2 variables numéricas mediante el análisis de correlación. Se trata de una de las técnicas más habituales en análisis de datos y el primer paso necesario antes de construir cualquier modelo explicativo o predictivo más complejo. Para poder tener el  Datset hay que recolectar información a travez de encuestas.""")
st.write("""Conocer los datos y la tipología de las variables: bien de tipo cuantitativo o cualitativo. Dado que en función del tipo de las variables del conjunto de datos, se aplicarán una serie de coeficientes u otros.""")

st.write("""Método para su aplicación""")
st.write("""
Conocer qué método es el más adecuado para su aplicación: de nada vale conocer el script que ejecuta una correlación, si no se puede basar matemáticamente cómo desarrollar los cálculos.
Conocer, comprender e interpretar los resultados que los indicadores ofrecen: parte fundamental del análisis, basada en la diferencia existente entre los conceptos de causalidad y correlación que subyace en el análisis, y que suelen confundirse. El mero cálculo de un coeficiente, no determinado por una causalidad, no tiene porqué ser válido. Es decir «la existencia de correlación, no implica causalidad», como se refleja en esta viñeta:
 
Lo primero, un «conjunto de datos. En dicho conjunto el requisito es tener mínimo dos «variables» (éste es el nombre técnico), según unas técnicas u otras se han denominado «dominios», «campos» de una base de datos y similares.Conocer las bases matemáticas y estadísticas del análisis de datos, en concreto:""")


st.write("""### MATRIZ DE CORRELACION """)

st.write(""" Es una tabla que indica los coeficientes de conexión entre los factores,se utiliza para bosquejar información, como contribución a una investigación más desarrollada. Normalmente, un marco de relación es “cuadrado”, con factores similares que aparecieron en las líneas y secciones. Aplicaciones de una matriz de correlación medición de la relación La mayoría de los marcos de relación utilizan la Conexión de Minuto de Artículo de Pearson (r). Codificación de los factores En el caso de que también tengas información de un resumen, tendrás que elegir cómo codificar la información antes de procesar las conexiones. Tratamiento de las cualidades que faltan La información que utilizamos para procesar las conexiones a menudo contiene cualidades que faltan. Esto puede deberse a que no hemos recogido esta información o a que no tenemos la menor idea de las reacciones. Existen diferentes procedimientos para manejar las cualidades perdidas cuando se procesan las redes de conexión. La mejor práctica es, en su mayor parte, utilizar numerosas atribuciones.
 """)



st.write("""### Correlación parcial
El procedimiento Correlaciones parciales permite estudiar la relación lineal existente entre dos variables controlando el posible efecto de una o más variables extrañas. Un coeficiente de correlación parcial es una técnica de control estadístico que expresa el grado de relación lineal existente entre dos variables tras eliminar de ambas el efecto atribuible a terceras variables.
Por ejemplo, se sabe que la correlación entre las variables inteligencia y rendimiento escolar es alta y positiva. Sin embargo, cuando se controla el efecto de terceras variables como el número de horas de estudio o el nivel educativo de los padres, la correlación entre inteligencia y rendimiento desciende, lo cual indica que la relación entre inteligencia y rendimiento está condicionada, depende o está modulada por las variables sometidas a control.
### ¿Cómo se mide la correlación?
Tenemos el coeficiente de **correlación lineal de Pearson** que se *sirve para cuantificar tendencias lineales*, y el **coeficiente de correlación de Spearman** que se utiliza para *tendencias de aumento o disminución, no necesariamente lineales pero sí monótonas*. 
### Correlación de Pearson
El coeficiente de correlación lineal de Pearson mide una tendencia lineal entre dos variables numéricas.
Es el método de correlación más utilizado, pero asume que:
- La tendencia debe ser de tipo lineal.
- No existen valores atípicos (outliers).
- Las variables deben ser numéricas.
- Tenemos suficientes datos (algunos autores recomiendan tener más de 30 puntos u observaciones).
 
Los dos primeros supuestos se pueden evaluar simplemente con un diagrama de dispersión, mientras que para los últimos basta con mirar los datos y evaluar el diseño que tenemos.
En estadísticas , el coeficiente de correlación de Pearson también referido como de Pearson r , el Pearson coeficiente de correlación momento-producto ( PPMCC ), o la correlación bivariada, es una medida de correlación lineal entre dos conjuntos de datos. Es la covarianza de dos variables, dividida por el producto de sus desviaciones estándar.; por lo tanto, es esencialmente una medida normalizada de la covarianza, de modo que el resultado siempre tiene un valor entre -1 y 1. Al igual que con la covarianza en sí, la medida solo puede reflejar una correlación lineal de variables e ignora muchos otros tipos de relación o correlación. Como ejemplo simple, uno esperaría que la edad y la altura de una muestra de adolescentes de una escuela secundaria tuvieran un coeficiente de correlación de Pearson significativamente mayor que 0, pero menor que 1 (ya que 1 representaría una correlación irrealmente perfecta).

### Gráfica de dispersión
Es un tipo de ```diagrama``` que se utiliza para __observar y analizar__ la existencia de una __correlación__ entre ```dos variables``` cuantitativas, donde una depende de la otra mediante una relación determinada para verificar o comprobar una hipótesis. Brinda una visualización de ```datos compacta```, que la hace apropiada para estudiar resultados cuantiosos de __encuestas y pruebas__.
 
Como su nombre indica, consiste en una ```colección de puntos``` esparcidos en el plano cartesiano XY, donde se desea distinguir un __patrón o comportamiento__ en el conjunto de datos para comprender su ```distribución```.
### Cómo se interpreta la correlación
El signo nos indica la dirección de la relación, como hemos visto en el diagrama de dispersión.
- un valor positivo indica una relación directa o positiva,
- un valor negativo indica relación indirecta, inversa o negativa,
- un valor nulo indica que no existe una tendencia entre ambas variables (puede ocurrir que no exista relación o que la relación sea más compleja que una tendencia, por ejemplo, una relación en forma de U).
La magnitud nos indica la fuerza de la relación, y toma valores entre $-1$ a $1$. Cuanto más cercano sea el valor a los extremos del intervalo ($1$ o $-1$) más fuerte será la tendencia de las variables, o será menor la dispersión que existe en los puntos alrededor de dicha tendencia. Cuanto más cerca del cero esté el coeficiente de correlación, más débil será la tendencia, es decir, habrá más dispersión en la nube de puntos.
- si la correlación vale $1$ o $-1$ diremos que la correlación es “perfecta”,
- si la correlación vale $0$ diremos que las variables no están correlacionadas.
""")

st.write(""" ![imagen.png](https://user-images.githubusercontent.com/25250496/204172549-2ccf3be3-a2b3-4b49-9cd4-adb66e28621d.png) """)

st.write("""
**Distancia Euclidiana**: La distancia euclidiana es la generalización del __`teorema de Pitágoras`__.
### Correlación de Spearman
El coeficiente de correlación lineal de Spearman mide la fuerza y la dirección de la asociación entre dos variables clasificadas.
Se emplea como alternativa no paramétrica al coeficiente de Pearson cuando los valores son ordinales, o bien, cuando los valores son continuos pero no satisfacen la condición de normalidad.
El coeficiente de Spearman requiere que la relación entre las variables sea monótona, es decir, que cuando una variable crece la otra también lo hace o cuando una crece la otra decrece
### Correlación de Kendall
El coeficiente de correlación lineal de Kendall mide la intensidad de una relación lineal entreb dos variables, que no pudieran no tener relación causal entre si, y sin embargo estar relaciodas.
Es otra alternativa al coeficiente de correlación de Pearson cuando no se cumple la condición de normalidad. Se utiliza cuando el número de observaciones es pequeño o los valores se acumulan en una región por lo que el número de ligaduras al generar el ranking es alto.
### Coeficientes de correlación lineal
Son estadísticos que cuantifican la asociación lineal entre dos variables numéricas. Existen diferentes tipos, de entre los que destacan el Pearson, Spearman y Kendall. Todos ellos comparten que:
- Su valor está comprendido en el rango [+1 , -1]. Siendo +1 una correlación positiva perfecta y -1 una correlación negativa perfecta.
- Se emplean como medida de la fuerza de asociación entre dos variables (tamaño del efecto):
- **0** :asociación nula
- **0.1** : asociación pequeña.
- **0.3**: asociación mediana.
- **0.5**: asociación moderada.
- **0.7**: asociación alta.
- **0.9**: asociación muy alta.
Desde el punto de vista práctico, las principales diferencias entre estos tres coeficientes son:
- La correlación de Pearson funciona bien con variables cuantitativas que tienen una distribución normal o próxima a la normal.
- La correlación de Spearman se emplea con variables cuantitativas.En lugar de utilizar directamente el valor de cada variable, los datos son ordenados y reemplazados por su respectivo orden ranking.
- Al igual que la correlación de Spearman, utiliza la ordenación de las observaciones ranking. Es recomendable cuando se dispone de pocos datos y muchos de ellos ocupan la misma posición en el rango.
#### Covarianza
Mide el grado de variación conjunta de dos variables aleatorias.
## ¿Que es NUMPY?
Es una librería de Python especializada en el cálculo numérico y el análisis de datos, especialmente para un gran volumen de datos.Incorpora arrays lo que permite representar colecciones de datos de un mismo tipo en varias dimensiones, y funciones muy eficientes para su manipulación.Además cuenta con múltiples herramientas para manejar matrices de una forma muy eficiente.

El módulo Numpy introduce en escena un nuevo tipo de objeto, ndarray (n dimensional array), caracterizado por:

- Almacenamiento eficiente de colecciones de datos del mismo tipo
- Conjunto de métodos que permiten operar de forma vectorizada sobre sus datos
- Las formas más habituales de crear un nuevo array son:

A partir de otras colecciones de datos de Python, como listas o tuplas
Desde cero mediante funciones específicas
Leyendo los datos de un fichero
### ¿Qué es la imputación?
Es llenar los espacios vacios de la base de datos imcompleta con valores con valores admisibles y así obtener un archivo completo para poder analizarlo. Se habla de la imputación como un proceso de `fabricación de datos`. La imputación nos ayuda a:
- Facilitar los procesos posteriores de análisis de datos.
- Facilitar la consistencia de los resultados entre distintos tipos de análisis.
Las técnicas de imputación se clasifican en:
### Procedimientos tradicionales de imputación
#### Análisis con datos complejos:
El ***listwise*** es el método que se utiliza con mayor frecuencia, consta de una manera de proceder en donde se trabaja únicamente con las observaciones que contienen la información completa.
#### Análisis con los datos disponibles:
El procedimiento ***Available-case (AC)***; en comparación con el anterior este utiliza distintos tamaños de muestra; este método asume un patrón MCAR en los datos obtenidos; las observaciones que no tienen datos se eliminan.
####  Reponderación:
Los ponderadores se interpretan como el número de unidades de la población que representa a cada elemento de muestra; los algoritmos completaran con estimaciones compatibles.
### Imputación simple
#### - Imputación por el método de la media:
Es un procedimiento sencillo, consiste en sustituir el valor ausente por la media de los valores válidos, presenta dos variantes:
- Imputación por media no condicional: Consiste en estimar la media de los valores observados.
- Imputación por media condicional: Consiste en agrupar los valores observados y no observados en clases e imputar los valores faltantes por la media de los valores observados en la misma clase.
#### - Imputación con variables ficticias
Consiste en crear una variable indicador para identificar las observaciones con datos faltantes.
#### - Imputación por regresión
Consiste en estimar los valores ausentes en base a su relación con otras variables mediante análisis de regresión.Se incluyen en dicho grupo aquellos procedimientos de imputación que asignan a los campos a imputar valores en función del modelo: 
### Imputación múltiple
+ Es la imputación más recomendada.
+ Para la estimación de valores perdidos se realiza un modelo de regresión múltiple para predecir valores faltantes en función de múltiples variables.
+ Utiliza muestreos aleatorios de la distribución condicional de la variable de destino dadas otras variables.
+ La información que se añade para remplazar predecir los valores perdidos puede contener cualquier variable que sea potencialmente predictiva, incluyendo variables medidas a futuro.
+ Requiere especificarse en el modelo de regresión para observar cómo cambia la estimación.
## ¿Qué es la regresión lineal?
La regresión lineal o ajuste lineal es un modelo matemático que se usa para hallar la aproximacion de la relación de dependencia de la variable Y con la variable X
Es usada en muchos ámbitos para predecir un comportamiento que tenga que ver con 2 variables, en caso no se pueda aplicar se dice que no hay correlaci{on entre las variables estudiadas.
**Regresión Lineal**: La regresión lineal se usa para encontrar una __`relación lineal entre el objetivo y uno o más predictores`__.
""")
st.write("""![que-es-la-regresion-lineal-y-para-que-sirve](https://user-images.githubusercontent.com/25250496/204172072-0fabbfdf-1c4c-4f9b-8f42-505d98b18b71.png)""")
st.write("""### ¿Qué es Pandas?

Pandas es una librería de código abierto que ofrece unas estructuras muy poderosas y flexibles que facilitan la manipulación y tratamiento de datos.Las principales funciones de pandas son :cargar datos, modelar, analizar, manipular y prepararlos.

### Estructuras de datos Pandas:
  Cuenta con dos estructuras estas son:

- Series: array unidimensional etiquetado capaz de almacenar cualquier tipo de dato.
- DataFrame: estructura bidimensional con columnas que pueden ser también de cualquier tipo. Estas columnas son a su vez Series.
### ¿Como analizar datos con Pandas?
- head(n): Esta función devuelve las primeras n filas de nuestro DataFrame.
- tail(n): Devuelve las n últimas filas de nuestro DataFrame.
- describe(): Esta función da estadísticas descriptivas incluyendo aquellas que resumen la tendencia central, dispersión y la forma de la distribución de los datos.""")

st.write("""
## Escala de Likerd
### ¿Qué es la escala Likert?
Se utiliza para medir qué tan de acuerdo están los encuestados con una variedad de afirmaciones.Esta es ideal para medir reacciones, actitudes y comportamientos de una persona. A diferencia de una simple pregunta de “sí” / “no”, la escala de Likert permite a los encuestados calificar sus respuestas.

La escala de Likert es uno de los tipos de escalas de medición utilizados principalmente en la investigación de mercados para la comprensión de las opiniones y actitudes de un consumidor hacia una marca, producto o mercado meta. Nos sirve principalmente para realizar mediciones y conocer sobre el grado de conformidad de una persona o encuestado hacia determinada oración afirmativa o negativa.

Las respuestas pueden ser ofrecidas en diferentes niveles de medición, permitiendo escalas de 5, 7 y 9 elementos configurados previamente. Siempre se debe tener un elemento neutral para aquellos usuarios que ni de acuerdo ni en desacuerdo.
""")
st.write("""### CSV (Valores Separados por Comas):

Es el formato más común de importación y exportación de hojas de cálculo y bases de datos. Es cualquier archivo de texto en el cual los caracteres están separados por comas, haciendo una especie de tabla en filas y columnas. Las columnas quedan definidas por cada punto y coma (;), mientras que cada fila se define mediante una línea adicional en el texto. De esta manera, se pueden crear archivos CSV con gran facilidad.

### ¿Para qué sirve un archivo CSV?

Los archivos CSV sirven para manejar una gran cantidad de datos en formato tabla, sin que ello conlleve sobrecoste computacional alguno. Es tremendamente sencillo generar una tabla a partir de un documento de texto, con tan solo delimitar cada celda requerida con un punto y coma o con una coma).

### Gráfica de calor
Un gráfico de calor se usa para visualizar la relación numérica existente entre dos variables de categorías.Esta consiste en una cuadrícula rectangular compuesta de dos variables de categorías,cada celda de la cuadrícula se simboliza con un valor numérico. tiene limitaciones? Las variables de un gráfico de calor no pueden tener más de 3.000 valores únicos por eje. Si una de las variables o ambas exceden el límite de 3.000 valores, puede usarse un filtro, por ejemplo, un filtro predefinido, para reducir el tamaño del dataset.""")

st.write("""![linea 2](https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png)""")
