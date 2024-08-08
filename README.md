# GIIA-IDESIE-L35

Versión local ejecutable en PC.

## Instalación
Para ejecutarlo en local, en nuestro PC:
1. Instalar [Anaconda](https://docs.anaconda.com/anaconda/install/windows/)
2. Copiar los archivos de la rama `local_PC_version` en el ordenador, por ejemplo en `C:\Users\USUARIO\ia`
3. Editar el archivo `.env` y rellenar las API keys
4. Ejecutar Anaconda Prompt y situarse en la carpeta donde están los archivos, por ejemplo: `cd ia` para ir a la subcarpeta `ia` del directorio donde estamos. Otro ejemplo: `cd C:\Users\USUARIO\ia`
5. Instalar los requisitos `pip install -r requirements.txt`

## Ejecución
1. Ejecutar Anaconda Prompt y situarse en la carpeta donde están los archivos, por ejemplo: `cd ia` para ir a la subcarpeta `ia` del directorio donde estamos. Otro ejemplo: `cd C:\Users\USUARIO\ia`
2. Ejecutar en la consola de Anaconda Prompt `streamlit run main.py` para ejecutar un servidor local de Streamlit. Se abrirá una pestaña del navegador con la web creada.
