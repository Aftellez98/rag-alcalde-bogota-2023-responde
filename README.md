# BogotaInteligente - Sistema de Pregunta y Respuesta para Programas de Gobierno

## Descripción

BogotaInteligente es un sistema de pregunta y respuesta centrado en programas de gobierno que emplea técnicas avanzadas de procesamiento de lenguaje natural (PLN) y aprendizaje profundo para proporcionar respuestas precisas y contextualmente relevantes a preguntas específicas sobre programas gubernamentales. Este sistema aborda el desafío de acceder a información específica y relevante sobre programas y políticas gubernamentales, superando las barreras comunes que enfrentan los ciudadanos, como la vastedad de documentos en formato PDF, la necesidad de entender el contexto y la dificultad para extraer respuestas precisas de manera rápida.Es importante denotar que este maneja una exactitud del 72.6%.

## Cómo funciona

El sistema BogotaInteligente sigue un proceso detallado para proporcionar respuestas a las preguntas de los usuarios:

1. **Lectura de PDFs con LangChain:** El modelo utiliza LangChain, un framework específico para el procesamiento de lenguaje natural que facilita la lectura de documentos PDF. Esto permite al sistema acceder a la información contenida en documentos gubernamentales.

2. **Segmentación en Párrafos con Expresiones Regulares:** La segmentación implica dividir el texto en unidades más pequeñas, que en este caso son párrafos. Para dividir el texto, se emplean expresiones regulares de LangChain, lo que facilita la organización de la información en unidades manejables.

3. **Cálculo de Embeddings con OpenAI:** Los embeddings son representaciones vectoriales que capturan el significado semántico del texto. A cada párrafo se calcula su respectivo embedding usando la función de embeddings de OpenAI, lo que permite al sistema entender el contenido en términos de significado y contexto.

4. **Función de Distancia:** Actualmente, se utiliza una función de producto punto para medir la similitud entre la pregunta y los embeddings de los párrafos. A la pregunta también se le calcula su embedding. Luego, los tres párrafos más cercanos según la función de distancia se seleccionan como los más relevantes para responder la pregunta, lo que garantiza respuestas contextualmente relevantes.

5. **Respuestas Generativas:** Para generar respuestas coherentes y contextualmente relevantes, se utiliza ChatGPT 3.5 Turbo de OpenAI. En esta etapa, se aplica un proceso de limpieza del texto para garantizar que la respuesta final sea clara y relevante. Esto permite proporcionar respuestas que no solo son precisas sino también comprensibles para los usuarios.

## Cómo ejecutar el sistema

Para utilizar BogotaInteligente y obtener respuestas a tus preguntas sobre programas de gobierno, sigue estos pasos:

1. Asegúrate de tener Python instalado en tu sistema.

2. Descarga el código fuente del sistema desde este repositorio.

3. Abre una terminal o consola de comandos.

4. Ejecuta el siguiente comando para instalar las dependencias necesarias:

   ```shell
   pip install -r requirements.txt

5. Navega hasta la ubicación donde descargaste el código.

6. Ejecuta el archivo `main.py` en la consola. El sistema te presentará una pregunta y te solicitará información sobre los candidatos a los que se refiere la pregunta.

7. Ingresa la pregunta y la información sobre los candidatos solicitada.

8. El sistema procesará tu pregunta y te proporcionará una respuesta precisa y contextualmente relevante sobre los programas de gobierno de los candidatos.

BogotaInteligente está diseñado para ayudarte a acceder fácilmente a información gubernamental importante y tomar decisiones informadas.

---

Nota: Asegúrate de contar con los requisitos necesarios, como las bibliotecas y modelos de lenguaje mencionados en el código fuente, para garantizar el funcionamiento adecuado del sistema.