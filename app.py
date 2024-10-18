import os
import requests
import json
from flask import Flask, request, redirect, url_for, render_template, flash

# Configurar Flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['SECRET_KEY'] = 'your_secret_key'

# Asegúrate de que exista la carpeta de subida
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Ruta para subir y reemplazar el archivo
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Verifica si se subió un archivo
        if 'file' not in request.files:
            flash('No se seleccionó ningún archivo.')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No se seleccionó ningún archivo.')
            return redirect(request.url)

        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Llamada a la API para reemplazar el archivo, pasando filename como argumento
            replace_audio_file(filepath, file.filename)

            flash('El archivo de audio ha sido reemplazado exitosamente.')
            return redirect(request.url)

    return render_template('index.html')

# Función para hacer la solicitud a la API de Cisco y reemplazar el archivo
def replace_audio_file(filepath, filename):
    url = 'https://api.wxcc-us1.cisco.com/organization/{YOUR ORG ID}/audio-file/{ID FILE TO REMLACE}'
    token = '{Your TOKEN}'  # Aquí deberías agregar tu token de autenticación

    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json',
        # No incluimos el 'Content-Type', ya que requests lo manejará automáticamente al enviar archivos multipart
    }

    # JSON data correctly formatted
    audio_file_info = {
        "blobId": "",  # Asegúrate de que esto esté bien según los requisitos del API
        "contentType": "audio/mpeg",  # Ajusta el content type según el archivo
        "createdTime": 0,
        "id": "",  # Si necesitas pasar un ID válido
        "lastUpdatedTime": 0,
        "name": filename,  # Asegúrate de usar el nombre correcto del archivo
        "organizationId": "{YOU ORG ID}",
        "version": 1
    }

    with open(filepath, 'rb') as audio_file:
        files = {
            'audioFile': (filename, audio_file, 'audio/mpeg'),  # Especifica el tipo MIME correctamente
            'audioFileInfo': (None, json.dumps(audio_file_info), 'application/json')  # Enviar correctamente el JSON
        }

        response = requests.put(url, headers=headers, files=files)

        if response.status_code == 200:
            print('Archivo reemplazado exitosamente.')
        else:
            print(f'Error: {response.status_code}, {response.text}')

if __name__ == '__main__':
    app.run(debug=True)
