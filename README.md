# S30 - Unidad 1. Evidencia de Aprendizaje 2
## Manejo de archivos CSV, JSON y TXT

Este proyecto implementa tres clases separadas y coordina el flujo desde Jupyter:

- `manejador_csv.py`: importa un CSV con `csv.reader`, modifica datos y guarda otro CSV con encabezados usando `csv.writer`.
- `manejador_json.py`: importa un JSON con `json.load`, modifica datos y guarda otro JSON con `json.dump`.
- `generador_resumen_txt.py`: genera `resumen.txt` con las URL de origen, rutas, modificaciones, métodos y cantidades de registros.
- `actividad_ae2.ipynb`: coordina las clases y muestra los resultados antes y después.

## Importante sobre los datos

La carpeta `datos/` contiene archivos pequeños de ejemplo para que el código se pueda probar inmediatamente. **Para cumplir completamente la consigna, descarga manualmente un CSV y un JSON desde Hugging Face, conserva los originales y reemplaza los archivos de ejemplo.** Después actualiza en el notebook las variables `URL_CSV_ORIGEN` y `URL_JSON_ORIGEN` con las URL específicas de los archivos que realmente descargaste.

CSV de referencia en Hugging Face:
https://huggingface.co/datasets/scikit-learn/iris/blob/main/Iris.csv

Una opción de archivo JSON en Hugging Face:
https://huggingface.co/datasets/PhdDz/Paper_1_BioASQ-dataset/blob/main/train.json

El JSON que usa esta implementación debe ser una lista de objetos para aplicar el método `actualizar_valor` tal como está escrito. Si el archivo descargado tiene otra estructura, adapta la selección del campo/registro en el notebook o utiliza otro JSON de Hugging Face que sea una lista de objetos.

## Requisitos

Python 3.10 o superior y Jupyter.

```bash
python -m pip install -r requirements.txt
```

## Ejecución

1. Abre esta carpeta en VS Code.
2. Abre `actividad_ae2.ipynb`.
3. Ejecuta las celdas en orden, desde arriba.
4. Comprueba `datos/datos_modificados.csv`, `datos/datos_modificados.json` y `resumen.txt`.
5. Guarda el notebook con sus salidas.
6. Publica los archivos en una carpeta `AE2` del repositorio GitHub y registra commits descriptivos.

## Cambios de demostración incluidos

- CSV: se actualiza `Iris-setosa` a `Iris-setosa (revisado)` en el campo `Species`.
- JSON: se actualiza el nombre del primer producto y se agrega el campo `estado_revision`.

Estos cambios son demostrativos y pueden ajustarse a los archivos originales que descargues.
