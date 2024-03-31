import pandas as pd
import zipfile
import os

# Nombre del archivo ZIP
archivo_zip = 'data.zip'

# Extraer el archivo ZIP
with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
    zip_ref.extractall()  # Extraer todos los archivos en el directorio actual



def procesar_carpeta(carpeta):
    # Directorio principal
    directorio_principal = carpeta

    # Lista para almacenar los datos
    datos = []

    # Recorrer los subdirectorios
    for sentiment in os.listdir(directorio_principal):
        # Obtener la ruta completa del subdirectorio
        ruta_subdirectorio = os.path.join(directorio_principal, sentiment)
    
        # Verificar si es un directorio
        if os.path.isdir(ruta_subdirectorio):
            # Recorrer los archivos de texto en el subdirectorio
            for archivo in os.listdir(ruta_subdirectorio):
                # Verificar si es un archivo de texto
                if archivo.endswith('.txt'):
                    # Leer el contenido del archivo
                    with open(os.path.join(ruta_subdirectorio, archivo), 'r', encoding='utf-8') as file:
                        # Leer la frase
                        phrase = file.read().strip()
                    
                        # Agregar la frase y la etiqueta a la lista de datos
                        datos.append([phrase, sentiment])

    # Crear un DataFrame de pandas con los datos
    df = pd.DataFrame(datos, columns=["phrase", "sentiment"])
    return df



# Directorios de train y test
directorio_train = 'train'
directorio_test = 'test'

# Procesar la carpeta de entrenamiento
df_train = procesar_carpeta(directorio_train)

# Procesar la carpeta de prueba
df_test = procesar_carpeta(directorio_test)

# Guardar los DataFrames como archivos CSV
df_train.to_csv('train_dataset.csv', index=False)
df_test.to_csv('test_dataset.csv', index=False)




