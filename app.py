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
    url = 'https://api.wxcc-us1.cisco.com/organization/d9cd7ecf-e6e1-49fb-ab07-a69cb49ea081/audio-file/e74871ca-c291-4704-ae5a-cf4102412ae0'
    token = 'eyJhbGciOiJSUzI1NiJ9.eyJjbHVzdGVyIjoiUDBBMSIsInByaXZhdGUiOiJleUpqZEhraU9pSktWMVFpTENKbGJtTWlPaUpCTVRJNFEwSkRMVWhUTWpVMklpd2lZV3huSWpvaVpHbHlJbjAuLkNqSVIyRHk4Y09tWDA5YTlBcURINVEuNWNpSDhUY0YyZkZhektOOHZUemJlLURaaEFTVWNVaTZMdi1VVUtnbTJSRVpoRGUtb2o5VlVHUGpNS0hLRUVrTkFkYWE0ZnZiNndwRkZVTlRwWmE1LV9Wb2JOODYzQ2NWd3NmeHFIQy1OUWJ6MkVOc2R0Ylk4dUZpMnhSOFFqUzlvNDAtYjRINE0tQnlkX3RYSG1uSzc1aDhmRndOQ1F5RVFKeWEyYjBhVThkM3JqSDJPUGFidWw5dUVVMGo1ODhwU3VzTldXa09sMGZ2TWwxRk00MGVwQjVyV0tFSkF5dVVOaGp4cEc2MVZkT0tkeHJJRlFfYjZ3eXpSNndYdEwteEEyZkR6bUJ2bUpBT2NCTnRCVDV4Y1NScTcwbDVyOFZ0cmJZQ1dGbTdvZkUyel9NMVNNSnpzU1gtdGktdGFrMmRGazQ5RUJMQU9vOGRkbHdISm5PcFBEaDVBdGpDVkhjRDMySkRudXZ1VWV2YzBmMjQwUFZYV29CcGNFZGt3dmNjSW1qTlM1REpvb1ZiVkpWQjF2VklNa3FNUXF5eWdrSmVyWEVCQ2Z5V195RjRaXy0wMW0yZG9xY0JqYXhMU0tBa2xYU2VTcmhwRnRhNlhIdjVqcXdObE1JTkhGVkRCQXhidEdQdzZ4MHNhak52YnNlbEF2aWg5bmh4Mk91UlUxWVVxYlNUUGp1dVNJVnA1c1pXOHNPQXdXTEREdjduTkYtRFR2SWRRYTlSVkplek1TOHAzS2Q1SVpzX1pTSWdlcnNGY0djRTNZb010b1gxNTdEN0oyNHlOYTRDcnRMaHJDS3VZOXJxTlNwTTJ1ZU4tdEpxYnEyREItcTZnWG96cDI4WXByRjdUUTFLNzhiNENILXloWjBSQWUwRGV0bmhjV0RkcFdoa1Y0bEk4QWlLTzNnV19MZVJGVkJFU2ZYXzl0aFFsbFl2WGVyQ0hBQk9UY0JTcU1jWjZlN0Nma2FNVVRVSlNjRjVLb0JnaU9RUTE5d01IdVNRUVM3c081WXNUbm9TWV9nQ2p4YklGM252RkxoN3o3Uk5ybVZVLUJKU0x5T3VtTm9HY25RWk9XNTNMS2ZiNldkYm5OZm5LeXhvVTN4eVRaYk1haHR3R05iNl9lSDJrdnZFRVBNUHNScGNpN1RZc0p2OFIyWU9aV3VGSDR3TVJjZVJYY3FfNTJqclh5M2Y1c0ZGSk5zdGhxc1dxUF9xNEZHS2FpSEpyTE1yYXhvNndVWkVfdG5XclRvbHlqVTF3a3N5ZVpBTVI3bHhKQjF6c3dXNkNxLWhvTHdnQllXT2NRWUU5NnptMGR3NVNuOXZDWWdKUlRPcklRWVh3VDhQeEowcENRRHdEOFdyZ2NVRld3SzVuczV5aFFvQ0NDck5TSno2dVYtZS00dG05WEsxUkNYc0tEVE0xZHphWmJfcjVVY0JYRWJwWnc3azFSUmhNTUF6WE9MZk1SNXhjWjBZMWdJOFViSm9zUU5UeTE5TlpPUTZOTWEySDFXNFpaQ2RlU2l2S3VuNnB1WnUteHBhbGJPeS1wWUxOc3hNVjJTczdRcDhIZXhYWk9hV2ZvVGRnTDlsNEtOczR4Nkx4a08tRzFBdlB6QmpJLUUxTmlIei4tT2Q5R0RaVTlmTTd1emxhUUE3d1F3IiwidXNlcl90eXBlIjoidXNlciIsInRva2VuX2lkIjoiQWFaM3IwWlRZek56STJaak10TTJVNU5DMDBOamRtTFdKalkyVXROakJtWXpoaU0yUmtPR1UzTW1VM09UbGxZbVV0T1RsayIsInJlZmVyZW5jZV9pZCI6IjhjNjEyZWMwLThiZWUtNDg1OC04YWNkLTgwZjgwNGVlZDE5NyIsImlzcyI6Imh0dHBzOlwvXC9pZGJyb2tlci1iLXVzLndlYmV4LmNvbVwvaWRiIiwidXNlcl9tb2RpZnlfdGltZXN0YW1wIjoiMjAyNDEwMTcwMTU4MDUuNzgwWiIsInJlYWxtIjoiZDljZDdlY2YtZTZlMS00OWZiLWFiMDctYTY5Y2I0OWVhMDgxIiwiY2lzX3V1aWQiOiI5ZGI1ZjlhYy00MmUwLTRlMTItOGZjZC1hNGRjMWNjNzFiMDQiLCJ0b2tlbl90eXBlIjoiQmVhcmVyIiwiZXhwaXJ5X3RpbWUiOjE3MjkyNjY0MzgxOTYsImNsaWVudF9pZCI6IkM1ODI1NGYzOGNlMDBlYzdhZmQxYjYwNjZmOTdlM2MyNjgwZjgxOWZhZWZlNjhhOTY1MjE5N2EzYTllMTg4N2M0In0.jNDrbhSkQUq-jcru1Hp-UQxzlPhBqVu04BkYWIn5X-l0_Fcpw89jhiG9qGG2389AdAkr5bh5sL9EirLkKM4-0GJMIl6h0Bcujr8uPsUNcysa5Kj8pok8EMw5z6YBLKXyRwEVj_J5rKGV5u831GKWkpGKhPjV-56ZwPPIo4PCrmAIzZEj6Mfn_jOECnxuz-1MSckfJaym3abSgibE6m4RMCy4Xrj8MG_akeK7BC1OWlbG0gs2eGHckrDTppRifWdczLuL7atI11jspcwo53BtJuIcTJmU2LA5XXS49e9mKJiq1cBDT_m-nxpoS7tGvnyveI4tFpOvyaBkP-VANWFRSA'  # Aquí deberías agregar tu token de autenticación

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
        "organizationId": "d9cd7ecf-e6e1-49fb-ab07-a69cb49ea081",
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
