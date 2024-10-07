<<<<<<< Updated upstream
.startup.sh
#!/bin/bash


# Instalar las dependencias desde requirements.txt (si no existe, crea uno con 'pip freeze > requirements.txt')
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

# Obtener la ruta del directorio donde está ubicado el script
SCRIPT_DIR=$(dirname "$0")
# Cambiar al directorio donde está tu aplicación Flask
# Cambiar al directorio donde está tu aplicación Flask
cd "$SCRIPT_DIR"

cd src/Webapp/

# Exportar la variable de entorno FLASK_APP y ejecutar la aplicación en modo de desarrollo
export FLASK_APP=main.py
export FLASK_ENV=development

# Ejecutar la aplicación Flask
flask run --host=0.0.0.0 --port=5000
=======
:: .\startup.sh
python main.py
>>>>>>> Stashed changes
