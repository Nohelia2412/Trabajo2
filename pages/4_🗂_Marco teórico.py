import streamlit as st
    
    
    st.write("""###Base Teorica""")

    st.write("""###Analisis de correlacion""")
    st.markdown ( 'El análisis de conexiones es el primer paso para construir modelos explicativos y predictivos más complejos.' )

 
    st.markdown ( 'A menudo nos interesa observar y medir la relación entre 2 variables numéricas mediante el análisis de transmisión.' )

    st.markdown ( 'Se trata de una de las técnicas más habituales en análisis de datos y el primer paso necesario antes de construir cualquier modelo explicativo o predictivo más complejo.' )

    st.markdown ( 'Para poder tener el Datset hay que recolectar información a travez de encuentas.' )

    st.markdown ( "<h2 style='color: black;'>¿Qué es la conexión?</h2>" , unsafe_allow_html = True )

    st.markdown ( 'La coincidencia es un tipo de asociación entre dos variables numéricas, específicamente evalúa la tendencia (creciente o decreciente) en los datos.' )

    st.markdown ( 'Dos variables están asociadas cuando una variable nos da información acerca de la otra. Por el contrario, cuando no existe asociación, el aumento o disminución de una variable no nos dice nada sobre el comportamiento de la otra variable.' )
 
    st.markdown ( 'Dos variables se correlacionan cuando muestran una tendencia creciente o decreciente.' )

    st.markdown ( "<h2 style='text-align: color: black;'>¿Cómo se mide la conexión?</h2>" , unsafe_allow_html = True )

    st.markdown ( 'Tenemos el coeficiente de correlación lineal de Pearson que se sirve para cuantificar tendencias lineales, y el coeficiente de correlación de Spearman que se utiliza para tendencias de aumento o disminución, no obstante lineales pero sí monótonas.' )

    st.markdown ( "<h2 style='text-align: color: black;'>Correlación de Pearson</h2>" , unsafe_allow_html = True )


    st.markdown ( 'El coeficiente de correlación lineal de Pearson mide una tendencia lineal entre dos variables numéricas.' )

    st.markdown ( 'Es el método de conexión más utilizado, pero asume que:.' )
    st.markdown ( '- La tendencia debe ser de tipo lineal.' )
    st.markdown ( 'No existen valores atípicos (outliers' )
    st.markdown ( '- Las variables deben ser numéricas.' )
    st.markdown ( '- Tenemos suficientes datos (algunos autores recomiendan tener más de 30 puntos u observaciones).' )

    st.markdown ( 'Los dos primeros supuestos se pueden evaluar simplemente con un diagrama de dispersión, mientras que para los últimos basta con mirar los datos y evaluar el diseño que tenemos.' )

    st.markdown ( "<h2 style='text-align: color: black;'>Cómo se interpreta la conexión</h2>" , unsafe_allow_html = True )

    st.markdown ( 'El signo nos indica la dirección de la relación, como hemos visto en el diagrama de dispersión.' )
    st.markdown ( '- un valor positivo indica una relación directa o positiva.' )
    st.markdown ( '- un valor negativo indica relación indirecta, inversa o negativa.' )
    st.markdown ( ' - un valor nulo indica que no existe una tendencia entre ambas variables (puede ocurrir que no exista relación o que la relación sea más compleja que una tendencia, por ejemplo, una relación en forma de U).' )


    st.markdown ( 'La magnitud nos indica la fuerza de la relación, y toma valores entre $-1$ a $1$. Cuanto más cercano sea el valor a los extremos del intervalo ($1$ o $-1$) más fuerte será la tendencia de las variables, o será menor la dispersión que exista en los puntos alrededor de dicha tendencia .')
    st.markdown ( '- si la conexión vale $1$ o $-1$ diremos que la conexión es “perfecta”.' )
    st.markdown ( '- si la conexión vale $0$ diremos que las variables no están correlacionadas.' )

    st.imagen ( "https://user-images.githubusercontent.com/25250496/204172549-2ccf3be3-a2b3-4b49-9cd4-adb66e28621d.png" )

    st.markdown ( "<h2 style='text-align: center; color: black;'>Fórmula Coeficiente de Correlación de Pearson</h2>" , unsafe_allow_html = True )

    st.imagen ( 'https://www.questionpro.com/blog/wp-content/uploads/2019/07/analisis-de-correlacion-2.jpg' )


    st.markdown ( 'Distancia Euclidiana: La distancia euclidiana es la generalización del teorema de Pitágoras.' )

    st.imagen ( 'http://3.bp.blogspot.com/-YU7iwu9rMIk/TuZLXuWM_8I/AAAAAAAAGNU/DqsQeCkheMk/s1600/Pit%25C3%25A1goras.png' )

    st.markdown ( 'Regresión Lineal: La regresión lineal se usa para encontrar una relación lineal entre el objetivo y uno o más predictores.' )

    st.imagen ( 'https://user-images.githubusercontent.com/25250496/204172072-0fabbfdf-1c4c-4f9b-8f42-505d98b18b71.png' )

    st.markdown ( "<h2 style='text-align: color: black;'>Marco teórico</h2>" , unsafe_allow_html = True )

    st.markdown ( "<h2 style='text-align: color: black;'>¿Que es machine learning?</h2>" , unsafe_allow_html = True )

    st.markdown ( 'Machine learning: Es una rama de la inteligencia artificial que es autónoma ya que puede realizar predicciones a partir de procesamiento de datos. Esta tecnología está presente en un sinfín de aplicaciones como las recomendaciones de Netflix o Spotify, las respuestas inteligentes de Gmail o el habla de Siri y Alexa. El ‘machine learning’ es un maestro del reconocimiento de patrones, y es capaz de convertir una muestra de datos en un programa informático capaz de extraer inferencias de nuevos conjuntos de datos para los que no ha sido entrenado previamente Aunque ahora esté de moda, gracias a su capacidad para derrotar a jugadores del Go o resolver cubos de Rubik, su origen se remonta al siglo pasado. “La estadística es sin duda la base fundamental del aprendizaje automático, que básicamente consiste en una serie de algoritmos capaces de analizar grandes cantidades de datos para deducir cuál es el resultado más óptimo para un determinado problema”, añade Espinoza.' )
    

    st.imagen ( 'https://www.atriainnovation.com/wp-content/uploads/2021/02/portada.jpg' )

    st.markdown ( "<h2 style='text-align: color: black;'>LIBRERIAS PARA CIENCIA DE DATOS:</h2>" , unsafe_allow_html = True )


    

    st.markdown ( 'Conjuntos de archivos de código que han sido creados para desarrollar software de manera sencilla. Gracias a ellas, los desarrolladores pueden evitar la duplicidad de código y minimizar errores con mayor agilidad .Estas librerías son altamente prácticas a la hora de implementar flujos de Machine Learning.' )

    

    st.markdown ( "<h2 style='text-align: color: black;'>¿Qué es NUMPY?</h2>" , unsafe_allow_html = True )
            
    
    st.markdown ( 'Es una librería de Python especializada en el cálculo numérico y el análisis de datos, especialmente para un gran volumen de datos.Incorpora arrays lo que permite representar colecciones de datos de un mismo tipo en varias dimensiones, y funciones muy eficientes para su manipulación.Además cuenta con múltiples herramientas para manejar matrices de una forma muy eficiente.')

    st.imagen ('https://aprendeconalf.es/docencia/python/manual/img/arrays.png')
    
    st.markdown ("<h2 style='text-align: color: black;'>¿Qué es PANDAS?</h2>" , unsafe_allow_html = True )                

    st.markdown ( 'Pandas es una librería de código abierto que ofrece unas estructuras muy poderosas y flexibles que facilitan la manipulación y tratamiento de datos.Las principales funciones de pandas son :cargar datos, modelar, analizar, manipular y prepararlos.' )

    st.imagen ('https://profile.es/wp-content/media/Estructuras-de-datos-en-Pandas-1.png')
    
    st.markdown ( "<h2 style='text-align: color: black;'>¿Qué es matplotlib?</h2>" , unsafe_allow_html = True  )
    st.markdown ('Es una biblioteca para la generación de gráficos en dos dimensiones, a partir de datos contenidos en listas en el lenguaje de programación Python. Permite crear y personalizar los tipos de gráficos más comunes, entre ellos:')
    st.markdown ( '- Diagramas de barras' )
    st.markdown ( '- Histogramas' )
    st.markdown ( '- Diagramas de sectores' )
    st.markdown ( '- Diagramas de areas' )

    st.imagen ( 'https://matplotlib.org/3.1.1/_static/logo2_compressed.svg' )

    st.imagen ('https://miro.medium.com/max/1400/1*JTEqCz-VU16nkkUwzyWp_w.png')
    
    st.markdown ( "<h2 style='text-align: color: black;'>Seaborn:</h2>" , unsafe_allow_html = True )

    st.markdown ( 'Es una librería para Python que permite generar fácilmente gráficos. Seaborn está basada en matplotlib y proporciona una interfaz de alto nivel . Tiene como objetivo convertir la visualización en una parte central de la exploración y comprensión de los datos, generando atractivas gráficas con sencillas funciones que ofrecen una interfaz semejante, facilitando el paso de unas funciones a otras.' )
    

    st.imagen ( 'https://livecodestream.dev/post/how-to-build-beautiful-plots-with-python-and-seaborn/featured.jpg' )

    st.markdown ( "<h2 style='text-align: color: black;'>¿Qué es la escala Likert?</h2>" , unsafe_allow_html = True )

    st.markdown ( 'Se utiliza para medir qué tan de acuerdo están los encuestados con una variedad de afirmaciones.Esta es ideal para medir reacciones, actitudes y comportamientos de una persona. A diferencia de una simple pregunta de “sí” / “no”, la escala de Likert permite a los encuestados calificar sus respuestas.' )

    st.markdown ( 'La escala de Likert es uno de los tipos de escalas de medición utilizados principalmente en la investigación de mercados para la comprensión de las opiniones y actitudes de un consumidor hacia una marca, producto o mercado meta. Nos sirve principalmente para realizar mediciones y conocer sobre el grado de conformidad de una persona o encuestado hacia determinada oración afirmativa o negativa.' )
    st.markdown ( 'Las respuestas pueden ser ofrecidas en diferentes niveles de medición, permitiendo escalas de 5, 7 y 9 elementos configurados previamente. Siempre se debe tener un elemento neutral para aquellos usuarios que ni de acuerdo ni en desacuerdo.' )

    st.markdown (  "<h2 style='text-align: color: black;'>CSV (Valores Separados por Comas):</h2>" , unsafe_allow_html = True  )


    st.markdown ( 'Es el formato más común de importación y exportación de hojas de cálculo y bases de datos. Es cualquier archivo de texto en el cual los caracteres están separados por comas, haciendo una especie de tabla en filas y columnas. Las columnas quedan definidas por cada punto y coma (;), mientras que cada fila se define mediante una línea adicional en el texto. De esta manera, se pueden crear archivos CSV con gran facilidad.' )

    st.imagen ( 'https://acf.geeknetic.es/imgri/imagenes/tutoriales/definiciones/2020/6/Archivo-CSV-qrdy.jpg?f=webp' )

    
    
    st.markdown ( "<h2 style='text-align: color: black;'>DATOS FALTANTES</h2>" , unsafe_allow_html = True )

   
    st.markdown ('Son aquellos que no constan debido a cualquier acontecimiento, como por ejemplo errores en la transcripción de los datos o la ausencia de disposición a responder a ciertas cuestiones de una encuesta. Los datos pueden faltar de manera aleatoria o no aleatoria.')

    st.markdown ("<h2 style='text-align: color: black;'>METODOS DE IMPUTACION</h2>" , unsafe_allow_html = True )

    st.markdown ('Los métodos de imputación consisten en estimar los valores ausentes en base a los valores válidos de otras variables y/o casos de la muestra. La estimación se puede hacer a partir de la información del conjunto completo de variables o bien de algunas variables especialmente seleccionadas. Usualmente los métodos de imputación se utilizan con variables métricas (de intervalo o de razón), y deben aplicarse con gran precaución porque pueden introducir relaciones inexistentes en los datos realas.')

    

    st.markdown ('Sustitución por la Media. Consiste en sustituir el valor ausente por la Media de los valores válidos. Este procedimiento plantea inconvenientes como:')
    st.markdown ('-Dificulta la estimación de la Variáncia.')

    st.markdown ('-Distorsiona la verdadera distribución de la variable,')
    st.markdown ('Distorsiona la correlación entre variables dado que añade valores constantes.')

    st.markdown ('Sustitución por constante. Consiste en sustituir los valores ausentes por constantes cuyo valor viene determinado por razones teóricas o relacionadas con la investigación previa. Presenta los mismos inconvenientes que la sustitución por la Media, y solo debe ser utilizado si hay razones para suponer que es más adecuado que el método de la media.')

    st.markdown ("<h2 style='text-align: color: black;'>¿Qué es un framework?</h2>" , unsafe_allow_html = True )

    st.markdown ('Es una especie de plantilla, un esquema conceptual, que simplifica la elaboración de una tarea, ya que solo es necesario complementarlo de acuerdo a lo que se quiere realizar.')

    st.imagen ( 'https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png' )
