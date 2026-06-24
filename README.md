# Proyecto Render - Prediccion de concreto

Aplicacion Flask sencilla para predecir `concrete_compressive_strength` usando un modelo Gradient Boosting entrenado con el dataset Concrete Compressive Strength.

## Archivos principales

- `app.py`: aplicacion Flask.
- `modelo_concreto.pkl`: modelo entrenado.
- `requirements.txt`: dependencias para Render.
- `Procfile`: comando de arranque.
- `templates/index.html`: formulario web.
- `static/style.css`: estilos azules sin iconos.
- `URL_Render.txt`: archivo para pegar la URL publica despues del despliegue.

## Render

1. Subir esta carpeta a GitHub.
2. Crear un nuevo Web Service en Render.
3. Usar Python como entorno.
4. Build command: `pip install -r requirements.txt`
5. Start command: `gunicorn app:app`
