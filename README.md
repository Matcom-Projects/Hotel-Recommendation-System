# Hotel Recommendation System

### Integrantes:
Miguel Alejandro Yáñez Martínez C311
Darío Rodríguez Llosa C312

### Descripción del problema:

Desarrollar un nuevo método de clasificación que utilice las reseñas generadas por los usuarios para sugerir mejores opciones de compra.

#### Requerimientos:
Para el desarrollo general del programa se utilizó un procesador Intel(R) Core(TM) i5 de 11ª generación. Sin embargo, debido al alto costo computacional del entrenamiento del modelo, se empleó una máquina proporcionada por Google Colab, que ofrece acceso a recursos de computación en la nube, incluyendo GPU, para facilitar y acelerar el proceso de entrenamiento.
**Entrenamiento:**
GPU: NVIDIA T4 o superior
CPU:Intel(R) Xeon(R) o superior (en caso de no tener GPU)
#### Ejecución:
En caso de que solo se desee obtener el ranking, se debe ejecutar el archivo startup.sh. Si se requiere procesar un conjunto de datos, es necesario ejecutar cada celda del archivo data_preprocessing.ipynb. Para volver a entrenar el modelo, se debe seguir el mismo procedimiento con el archivo training.ipynb.